#!/usr/bin/env python3
"""Golden-set eval runner for the dental booking bot.

Validates the dataset, reports the language/category mix against the
40%-Hindi / 30%-code-switch guardrail from AI_Product_Metrics.md, and grades
model output. Deterministic graders (exact_match, entity_match, faithfulness)
run here; llm_judge cases need a judge callable (see run()).

Usage:
    python eval_runner.py [golden_set.jsonl]      # validate + distribution + oracle self-check
"""
import json
import sys
from collections import Counter
from pathlib import Path

INTENTS = {"book_appointment", "reschedule_appointment", "cancel_appointment",
           "confirm_appointment", "faq_pricing", "faq_location", "faq_general",
           "greeting", "reminder_reply", "other", "multi_intent"}
REPLY_INTENTS = {"CONFIRM", "CANCEL", "RESCHEDULE", "OTHER"}
METHODS = {"exact_match", "entity_match", "llm_judge", "faithfulness"}
LANGUAGES = {"hindi", "hinglish", "english", "other"}
REQUIRED = {"id", "category", "metric", "language", "difficulty", "input", "expected", "grading"}


def load(path):
    rows = []
    for i, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise SystemExit(f"line {i}: invalid JSON: {e}")
    return rows


def validate(rows):
    ids = set()
    for r in rows:
        missing = REQUIRED - r.keys()
        assert not missing, f"{r.get('id','?')}: missing fields {missing}"
        assert r["id"] not in ids, f"duplicate id {r['id']}"
        ids.add(r["id"])
        assert r["language"] in LANGUAGES, f"{r['id']}: bad language {r['language']}"
        m = r["grading"]["method"]
        assert m in METHODS, f"{r['id']}: bad grading method {m}"
        exp = r["expected"]
        if r["grading"].get("field") == "intent":
            assert exp.get("intent") in INTENTS, f"{r['id']}: bad intent {exp.get('intent')}"
        if r["grading"].get("field") == "reply_intent":
            assert exp.get("reply_intent") in REPLY_INTENTS, f"{r['id']}: bad reply_intent"
        if m == "entity_match":
            assert "entities" in exp, f"{r['id']}: entity_match needs expected.entities"
            assert r["grading"].get("fields"), f"{r['id']}: entity_match needs grading.fields"
        if m == "llm_judge":
            assert r["grading"].get("rubric"), f"{r['id']}: llm_judge needs a rubric"
        if m == "faithfulness":
            sf = r["grading"].get("source_field")
            assert sf and sf in (r.get("state") or {}), f"{r['id']}: faithfulness needs state.{sf}"
    return len(rows)


def distribution(rows):
    lang = Counter(r["language"] for r in rows)
    cat = Counter(r["category"] for r in rows)
    n = len(rows)
    return lang, cat, n


# --- deterministic graders: return True (pass) / False (fail) ---------------

def _norm(v):
    return str(v).strip().lower().replace(" ", "")


def grade_exact(row, output):
    field = row["grading"]["field"]
    return _norm(output.get(field)) == _norm(row["expected"][field])


def grade_entities(row, output):
    want = row["expected"]["entities"]
    got = output.get("entities", {})
    return all(_norm(got.get(f)) == _norm(want[f]) for f in row["grading"]["fields"])


def grade_faithfulness(row, output):
    """Every source figure must appear in the summary; no other numbers may."""
    src = row["state"][row["grading"]["source_field"]]
    summary = output.get("summary", "")
    nums_in = {int(t) for t in _tokens(summary)}
    src_vals = set(src.values())
    return src_vals.issubset(nums_in) and nums_in.issubset(src_vals)


def _tokens(text):
    cur = ""
    for ch in text:
        if ch.isdigit():
            cur += ch
        else:
            if cur:
                yield cur
                cur = ""
    if cur:
        yield cur


def run(rows, model_fn, judge_fn=None):
    """model_fn(row)->dict output. judge_fn(row, output)->bool for llm_judge.
    Returns per-metric pass rates; llm_judge rows are 'skipped' without a judge."""
    results = []
    for r in rows:
        m = r["grading"]["method"]
        out = model_fn(r)
        if m == "exact_match":
            ok = grade_exact(r, out)
        elif m == "entity_match":
            ok = grade_entities(r, out)
        elif m == "faithfulness":
            ok = grade_faithfulness(r, out)
        elif m == "llm_judge":
            if judge_fn is None:
                results.append((r, None))
                continue
            ok = judge_fn(r, out)
        results.append((r, ok))
    return results


def _oracle(row):
    """A perfect model: echoes expected answers. Used to self-check graders."""
    exp = row["expected"]
    out = {}
    if "intent" in exp:
        out["intent"] = exp["intent"]
    if "reply_intent" in exp:
        out["reply_intent"] = exp["reply_intent"]
    if "entities" in exp:
        out["entities"] = exp["entities"]
    if row["grading"]["method"] == "faithfulness":
        src = row["state"][row["grading"]["source_field"]]
        out["summary"] = "Summary: " + ", ".join(str(v) for v in src.values())
    return out


def _report(rows):
    lang, cat, n = distribution(rows)
    print(f"\n{n} cases validated.\n")
    print("Language mix (guardrail: ~40% hindi, ~30% hinglish):")
    for k in ("hindi", "hinglish", "english", "other"):
        c = lang.get(k, 0)
        print(f"  {k:9} {c:3}  {c / n:5.0%}")
    print("\nCategory mix:")
    for k, c in sorted(cat.items()):
        print(f"  {k:26} {c:3}")
    det = run(rows, _oracle)
    graded = [ok for _, ok in det if ok is not None]
    judged = sum(1 for _, ok in det if ok is None)
    print(f"\nOracle self-check: {sum(graded)}/{len(graded)} deterministic graders pass "
          f"(expect 100%); {judged} llm_judge cases need a judge callable.")
    assert all(graded), "grader logic is inconsistent with the dataset"
    # guardrail sanity: Hindi-dominant content must not collapse to English-skewed
    assert lang.get("hindi", 0) / n >= 0.30, "Hindi share below floor — eval would mask Pune failures"
    assert (lang.get("hindi", 0) + lang.get("hinglish", 0)) / n >= 0.60, "non-English share too low"
    print("Guardrail check: PASS")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("golden_set.jsonl")
    rows = load(path)
    validate(rows)
    _report(rows)
