# Feature Prioritization Matrix

**Project:** AI-Powered Appointment Booking System for Indian Dental Clinics  
**Date:** May 12, 2026  
**Version:** 1.0  
**Document Owner:** Product Manager

---

## Executive Summary

This document prioritizes 25+ features using the **RICE scoring framework** (Reach × Impact × Confidence ÷ Effort) to determine MVP scope vs. future releases. The goal is to launch a working product in 16 weeks that delivers immediate value to small Indian dental clinics while laying groundwork for scale.

**Key Decisions:**
- **MVP Focus:** WhatsApp booking automation + SMS reminders = 80% of no-show reduction
- **Defer to V2:** AI voice calling (high effort, lower confidence for MVP)
- **Must Have:** Walk-in registration (critical for Indian clinics, often overlooked)
- **Won't Have (V1/V2):** Multi-location, patient portal, treatment plans (premature)

---

## RICE Scoring Framework

### Scoring Methodology

**RICE = (Reach × Impact × Confidence) ÷ Effort**

#### 1. Reach (How many clinics/users impacted per quarter?)
- **10 points:** 100% of clinics use this feature
- **7 points:** 70% of clinics use this feature
- **5 points:** 50% of clinics use this feature
- **3 points:** 30% of clinics use this feature
- **1 point:** <10% of clinics use this feature

#### 2. Impact (How much does it reduce no-shows/save time?)
- **3 points:** Massive impact - Core value proposition (e.g., WhatsApp booking)
- **2 points:** High impact - Significantly improves experience
- **1 point:** Medium impact - Nice to have improvement
- **0.5 points:** Low impact - Minimal value add

#### 3. Confidence (How sure are we it'll work?)
- **100%:** Proven in market (e.g., Practo has SMS reminders)
- **80%:** High confidence based on user research
- **50%:** Medium confidence - needs validation
- **20%:** Low confidence - experimental

#### 4. Effort (Engineering weeks required)
- Actual weeks (e.g., 2 weeks = 2, 8 weeks = 8)
- Includes design, development, testing, deployment
- Based on 1 full-stack engineer

**RICE Score Interpretation:**
- **>10:** Must have in MVP
- **5-10:** Should have in MVP (if capacity allows)
- **2-5:** V2 priority
- **<2:** V3 or Won't Have

---

## Feature Scoring Table

| # | Feature | Reach | Impact | Confidence | Effort (weeks) | RICE Score | Priority |
|---|---------|-------|--------|------------|----------------|------------|----------|
| 1 | WhatsApp Auto-Booking | 10 | 3 | 100% | 3 | **10.0** | Must Have (MVP) |
| 2 | SMS Reminders (24h before) | 10 | 2 | 100% | 1 | **20.0** | Must Have (MVP) |
| 3 | Walk-in Registration | 10 | 2 | 100% | 2 | **10.0** | Must Have (MVP) |
| 4 | Staff Mobile App (Android) | 10 | 3 | 80% | 4 | **6.0** | Must Have (MVP) |
| 5 | Basic Calendar (30-min slots) | 10 | 3 | 100% | 2 | **15.0** | Must Have (MVP) |
| 6 | Doctor Availability Editor | 10 | 2 | 100% | 2 | **10.0** | Must Have (MVP) |
| 7 | UPI Payment Links (advance) | 7 | 2 | 80% | 2 | **5.6** | Should Have (MVP) |
| 8 | Patient Phone Verification | 10 | 1 | 100% | 1 | **10.0** | Must Have (MVP) |
| 9 | Multi-language (Hindi + English) | 10 | 2 | 80% | 3 | **5.3** | Should Have (MVP) |
| 10 | WhatsApp Confirmation Messages | 10 | 1 | 100% | 0.5 | **20.0** | Must Have (MVP) |
| 11 | Doctor WhatsApp Daily Summary | 10 | 1 | 100% | 1 | **10.0** | Should Have (MVP) |
| 12 | Split-shift Scheduling | 10 | 2 | 100% | 1.5 | **13.3** | Must Have (MVP) |
| 13 | No-show Tracking | 7 | 1 | 100% | 1 | **7.0** | Should Have (MVP) |
| 14 | Basic Analytics Dashboard | 5 | 1 | 80% | 2 | **2.0** | Could Have (V2) |
| 15 | AI Voice Calling (Hindi/English) | 5 | 3 | 50% | 4 | **1.9** | Could Have (V2) |
| 16 | Patient History (notes) | 7 | 1 | 100% | 1 | **7.0** | Should Have (MVP) |
| 17 | Appointment Rescheduling (Self-serve) | 7 | 1 | 80% | 2 | **2.8** | Could Have (V2) |
| 18 | SMS Fallback (WhatsApp failures) | 10 | 0.5 | 100% | 0.5 | **10.0** | Must Have (MVP) |
| 19 | Holiday/Exception Management | 10 | 1 | 100% | 1 | **10.0** | Should Have (MVP) |
| 20 | Staff Role Management (ADMIN/STAFF) | 5 | 0.5 | 100% | 1 | **2.5** | Could Have (V2) |
| 21 | Multi-clinic Support (Database) | 3 | 0.5 | 100% | 0 | **∞** | Must Have (MVP)* |
| 22 | Regional Languages (Tamil, Bengali) | 3 | 1 | 50% | 4 | **0.4** | V3 |
| 23 | Patient Portal (Web login) | 5 | 1 | 50% | 6 | **0.4** | V3 |
| 24 | Treatment Plan Reminders | 3 | 1 | 50% | 3 | **0.5** | V3 |
| 25 | Google Calendar Sync | 5 | 1 | 80% | 3 | **1.3** | V2 |
| 26 | Waitlist Management | 3 | 2 | 50% | 4 | **0.8** | V2 |
| 27 | Multi-location (Clinic branches) | 1 | 0.5 | 80% | 6 | **0.1** | Won't Have |


---

## MVP Feature List (16 Weeks)

### Must Have Features (RICE > 10 or Critical Path)

#### Epic 1: Patient Booking (WhatsApp-first)
1. **WhatsApp Auto-Booking** (RICE: 10.0)
   - Bot responds to "I need appointment" → asks name, phone, doctor preference
   - Shows available slots → patient selects → instant confirmation
   - Works 24/7 (even when clinic closed at 11 PM)
   - **Acceptance Criteria:** <5 second response time, 95%+ message delivery

2. **WhatsApp Confirmation Messages** (RICE: 20.0)
   - Immediate booking confirmation with appointment details
   - Includes: Doctor name, date, time, clinic address (Google Maps link)
   - **Acceptance Criteria:** Sent within 10 seconds of booking

3. **SMS Reminders** (RICE: 20.0)
   - Sent 24 hours before appointment
   - Message: "Hi [Name], reminder: appointment with Dr. [Doctor] tomorrow at [Time]. Reply CANCEL to cancel."
   - **Acceptance Criteria:** 98%+ delivery rate, opt-out support

4. **SMS Fallback** (RICE: 10.0)
   - If WhatsApp delivery fails → automatic SMS fallback
   - **Acceptance Criteria:** Fallback within 30 seconds

#### Epic 2: Clinic Staff Mobile App
5. **Staff Mobile App (Android)** (RICE: 6.0)
   - Login screen (credentials-based)
   - Today's appointments list (chronological)
   - Add walk-in patient (quick form: name, phone, time)
   - Mark appointment as "Completed" or "No-show"
   - **Acceptance Criteria:** Works offline, syncs when online

6. **Walk-in Registration** (RICE: 10.0)
   - Staff adds walk-in directly from mobile app
   - Updates calendar in real-time (no double-booking)
   - **Why Critical:** 30-40% of appointments are walk-ins in India

#### Epic 3: Calendar Management
7. **Basic Calendar (30-min slots)** (RICE: 15.0)
   - Day view showing all appointments (walk-ins + booked)
   - Color-coded by status (Confirmed/Completed/No-show)
   - **Acceptance Criteria:** Real-time sync across staff/doctor devices

8. **Doctor Availability Editor** (RICE: 10.0)
   - Weekly schedule grid (Mon-Sun, 9 AM - 9 PM)
   - Support split shifts (10 AM-1 PM, 5 PM-9 PM)
   - One-click toggle for "Available" vs. "Off"
   - **Acceptance Criteria:** Changes reflect in booking system within 1 minute

9. **Split-shift Scheduling** (RICE: 13.3)
   - Default template: Morning (10 AM-1 PM), Evening (5 PM-9 PM)
   - Prevents bookings during lunch break (1 PM-5 PM)
   - **Why Critical:** Standard operating model for Indian clinics

10. **Holiday/Exception Management** (RICE: 10.0)
    - Staff marks specific dates as "Clinic Closed"
    - WhatsApp bot automatically suggests next available day
    - **Acceptance Criteria:** No bookings allowed on holidays

#### Epic 4: Patient Management
11. **Patient Phone Verification** (RICE: 10.0)
    - Send OTP via SMS on first booking
    - Prevents fake bookings (major no-show cause)
    - **Acceptance Criteria:** 99%+ OTP delivery, 2-minute expiry

12. **Patient History (Notes)** (RICE: 7.0)
    - Staff adds notes after appointment (e.g., "Root canal - 2nd visit")
    - Visible in next appointment (context for doctor)
    - **Acceptance Criteria:** Searchable by phone number

#### Epic 5: Doctor Dashboard (WhatsApp-based)
13. **Doctor WhatsApp Daily Summary** (RICE: 10.0)
    - Sent at 8 AM every morning
    - Lists today's appointments (time, patient name, contact)
    - **Why WhatsApp:** Doctors don't want another app

### Should Have Features (RICE 5-10, if time allows)

14. **UPI Payment Links (advance)** (RICE: 5.6)
    - Optional ₹100-200 advance payment link sent via WhatsApp
    - Reduces no-shows by 20-30% (proven by Practo)
    - **Decision:** Include if Sprint 7-8 has buffer time

15. **Multi-language (Hindi + English)** (RICE: 5.3)
    - WhatsApp bot supports code-switching (common in India)
    - UI text in Hindi + English (staff app)
    - **Decision:** Include core Hindi phrases in MVP

16. **No-show Tracking** (RICE: 7.0)
    - Automatic no-show flag if patient doesn't show up
    - Weekly report sent to doctor (via WhatsApp)
    - **Decision:** Include for measurement purposes

---

## V2 Features (Month 4-6)

### High-Value Additions (RICE 2-5)

#### Epic 6: Advanced Patient Experience
17. **AI Voice Calling (Hindi/English)** (RICE: 1.9)
    - Patient calls clinic number → AI answers
    - Books appointment via voice conversation
    - **Why Deferred:** High complexity, 50% confidence for MVP
    - **V2 Rationale:** WhatsApp proves workflow first, then add voice

18. **Appointment Rescheduling (Self-serve)** (RICE: 2.8)
    - Patient replies to reminder SMS → "Reschedule" option
    - Bot shows available slots → patient picks new time
    - **Why Deferred:** MVP focuses on reducing no-shows, not rescheduling

19. **Basic Analytics Dashboard** (RICE: 2.0)
    - Web dashboard for clinic owner
    - Metrics: Bookings/week, no-show rate, revenue (if UPI enabled)
    - Charts: Weekly trends, peak booking hours
    - **Why Deferred:** Nice-to-have, not blocking MVP launch

#### Epic 7: Operational Improvements
20. **Staff Role Management** (RICE: 2.5)
    - ADMIN role: Can edit availability, view all patients
    - STAFF role: Can only add walk-ins, mark completed
    - **Why Deferred:** Single staff member in MVP clinics

21. **Google Calendar Sync** (RICE: 1.3)
    - One-way sync: Appointments → Doctor's Google Calendar
    - Helps doctors who already use Google Calendar
    - **Why Deferred:** Complex OAuth flow, not critical for small clinics

22. **Waitlist Management** (RICE: 0.8)
    - If patient requests slot that's full → add to waitlist
    - Auto-notify via WhatsApp when slot opens (cancellation)
    - **Why Deferred:** Requires cancellation feature first

---

## V3 / Won't Have (Month 6+)

### Low Priority Features (RICE < 1)

23. **Regional Languages (Tamil, Telugu, Bengali)** (RICE: 0.4)
    - **Why Deferred:** Focus on Hindi+English heartland first (70% of market)
    - **Future:** Add region-by-region based on demand

24. **Patient Portal (Web login)** (RICE: 0.4)
    - Patients login to see appointment history, reschedule
    - **Why Won't Have:** WhatsApp already provides this via chat history
    - **Over-engineering risk:** Patients won't adopt another login

25. **Treatment Plan Reminders** (RICE: 0.5)
    - E.g., "Return in 6 months for checkup"
    - **Why Deferred:** Requires complex treatment tracking system
    - **V3 Candidate:** After patient portal exists

26. **Multi-location (Clinic branches)** (RICE: 0.1)
    - Clinic owner manages 2+ physical locations
    - **Why Won't Have:** Target market is single-location clinics
    - **Scope Creep Risk:** Adds complexity without MVP validation

---

## Effort Breakdown by Epic

### MVP (16 Weeks Total)

| Epic | Features | Total Effort (weeks) | Sprints |
|------|----------|----------------------|---------|
| **Epic 1:** Patient Booking | 4 features | 4.5 weeks | Sprint 3-4 |
| **Epic 2:** Staff Mobile App | 2 features | 6 weeks | Sprint 1-2 |
| **Epic 3:** Calendar Management | 4 features | 6.5 weeks | Sprint 5-6 |
| **Epic 4:** Patient Management | 2 features | 2 weeks | Sprint 7 |
| **Epic 5:** Doctor Dashboard | 1 feature | 1 week | Sprint 7 |
| **Foundation:** Database + Auth | Setup | 2 weeks | Sprint 1 |
| **Testing + Polish:** | End-to-end | 2 weeks | Sprint 8 |
| **TOTAL** | **17 features** | **16 weeks** | **8 sprints** |

**Buffer:** 2 weeks of polish/testing allows absorbing delays.

---

## Feature Comparison: MVP vs. Competitors

| Feature | Our MVP | Practo | DentalDost | WhatsApp Business (DIY) |
|---------|---------|--------|------------|-------------------------|
| WhatsApp Booking | ✅ (Auto-bot) | ❌ | ❌ | ⚠️ (Manual only) |
| SMS Reminders | ✅ | ✅ | ✅ | ❌ |
| Walk-in Registration | ✅ | ❌ | ✅ | ❌ |
| Split-shift Scheduling | ✅ | ❌ | ⚠️ (Rigid) | ❌ |
| Mobile App (Staff) | ✅ | ❌ | ✅ (Heavy) | ❌ |
| 10-min Setup | ✅ | ❌ (Days) | ❌ (Days) | ✅ |
| AI Voice Calling | ❌ (V2) | ❌ | ❌ | ❌ |
| Patient Portal | ❌ (V3) | ✅ | ✅ | ❌ |
| Analytics Dashboard | ❌ (V2) | ✅ | ✅ | ❌ |
| Price (₹/month) | ₹3,500 | Free (Patient-side) | ₹8,000-15,000 | Free (Manual labor) |

**Competitive Advantage:** WhatsApp-first automation + walk-in support + 10-min setup.

---

## Prioritization Decisions Explained

### Why WhatsApp > Voice AI for MVP?

**Data:**
- 98% of Indian clinic patients use WhatsApp daily
- Only 40% comfortable with AI voice interactions (user research)
- WhatsApp bot = 3 weeks effort, Voice AI = 4 weeks + Vapi.ai integration

**Decision:** WhatsApp delivers 80% of no-show reduction value with less risk. Voice AI is "wow factor" but not blocking MVP success.

**V2 Rationale:** Once WhatsApp workflow is validated, add voice as premium feature.

---

### Why Walk-in Registration is Must Have?

**Data from Problem Statement:**
- 30-40% of appointments are walk-ins in Indian clinics (vs. <10% in West)
- Neha (Front Desk persona) handles 5-8 walk-ins daily
- Without walk-in registration, system only solves 60% of appointment chaos

**Decision:** Must capture both appointment types in single calendar to prevent double-booking.

**Alternative Considered:** Defer to V2, focus only on pre-booked appointments.  
**Rejected because:** Incomplete solution → clinics won't adopt → MVP fails.

---

### Why UPI Payments are "Should Have" not "Must Have"?

**Data:**
- UPI adoption = 80% in urban India, but only 30% of clinics currently take advance payments
- Reduces no-shows by 20-30%, but SMS reminders already reduce by 40-50%
- Integration complexity: Razorpay API + compliance + testing = 2 weeks

**Decision:** Include if Sprint 7-8 runs ahead of schedule. Otherwise, launch without and add in V1.1 patch.

**Risk Mitigation:** No-show tracking in MVP proves ROI before adding payment complexity.

---

### Why Analytics Dashboard is V2?

**Data:**
- Clinic owners check analytics weekly, not daily (Dr. Priya persona)
- WhatsApp daily summary provides 80% of needed visibility
- Web dashboard = 2 weeks effort (React + charts + responsive design)

**Decision:** Focus MVP engineering time on booking workflow. Analytics are a "nice-to-have" after core system works.

**V2 Trigger:** After 50 clinics onboarded, aggregate data becomes valuable → build dashboard.

---

## Success Metrics by Priority Tier

### MVP Success = Must Have Features Working

**Target Metrics (After 1 Month Live):**
- **No-show Rate:** Drop from 28% → 15% (50% reduction)
- **Staff Time Saved:** 12+ hours/week (measured via clinic interviews)
- **Booking Completion Rate:** 70%+ (patients who start WhatsApp chat → complete booking)
- **System Uptime:** 99.5% during clinic hours (5 PM - 9 PM)
- **WhatsApp Response Time:** <5 seconds (95th percentile)

**Measurement:**
- Weekly check-ins with 10 beta clinics
- No-show tracking feature (built-in)
- Server logs (response time monitoring)

---

### V2 Success = Expansion Features

**Target Metrics (Month 4-6):**
- **AI Voice Call Success Rate:** 60%+ calls → successful booking
- **Rescheduling Usage:** 20% of patients use self-serve reschedule
- **Dashboard Engagement:** 50%+ clinic owners check weekly

**Measurement:**
- Vapi.ai call analytics
- Database queries (reschedule actions per week)
- Google Analytics (dashboard page views)

---

## Risk Analysis: MVP Scope

### Risks of Cutting Features

| Feature Cut | Risk | Mitigation |
|-------------|------|------------|
| AI Voice Calling → V2 | Competitors launch voice-first product | **Monitor:** Practo/DentalDost announcements. **Fast-follow:** Vapi.ai integration is 1 week if needed. |
| Analytics Dashboard → V2 | Clinic owners want data visibility | **Mitigation:** WhatsApp daily summaries + weekly reports (automated messages). |
| Multi-language → V2 | Non-Hindi regions feel excluded | **Mitigation:** Hindi+English covers 70% of TAM. Add regional languages based on demand signals. |

### Risks of Over-scoping MVP

| Feature Added | Risk | Impact |
|---------------|------|--------|
| Patient Portal (web login) | 6 weeks effort, low adoption | Delays launch by 1.5 months. Patients prefer WhatsApp chat history over portal login. |
| Treatment Plan System | Complex feature creep | Requires appointment history, dentist notes, reminder scheduling → 8+ weeks effort. |
| Multi-location Support | Premature optimization | Target market is single-location clinics. Adds database/UI complexity without validation. |

**Guiding Principle:** Launch MVP → Validate with 50 clinics → Add features based on real demand, not assumptions.

---



## Appendix: RICE Calculation Examples

### Example 1: WhatsApp Auto-Booking
- **Reach:** 10 (100% of clinics will use this)
- **Impact:** 3 (Massive - Core value proposition)
- **Confidence:** 100% (Proven by Practo's booking success)
- **Effort:** 3 weeks (WhatsApp Business API + bot logic + testing)
- **RICE = (10 × 3 × 1.0) ÷ 3 = 10.0** ✅ Must Have

### Example 2: AI Voice Calling
- **Reach:** 5 (50% of patients prefer voice over text - based on user research)
- **Impact:** 3 (Massive - "Wow factor" differentiator)
- **Confidence:** 50% (Unproven in dental context, Vapi.ai reliability unknown)
- **Effort:** 4 weeks (Vapi.ai integration + Hindi testing + call handling logic)
- **RICE = (5 × 3 × 0.5) ÷ 4 = 1.875** ⚠️ V2 Priority

### Example 3: SMS Reminders
- **Reach:** 10 (100% of patients get reminders)
- **Impact:** 2 (High - Proven to reduce no-shows by 40%)
- **Confidence:** 100% (Standard practice, Twilio reliability)
- **Effort:** 1 week (Twilio integration + cron job)
- **RICE = (10 × 2 × 1.0) ÷ 1 = 20.0** ✅ Must Have (Highest score!)

