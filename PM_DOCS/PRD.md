# Product Requirements Document (PRD)
## AI-Powered Appointment Booking System for Indian Dental Clinics


**Date:** May 17, 2026  
**Version:** 1.0
**Target Launch:** Q3 2026 (Beta: July, Public: September)

---

## Executive Summary

### Vision
Simplest appointment booking system for small Indian dental clinics that reduces no-shows by 50% and saves 10+ hours/week through WhatsApp-first automation.

### Solution
Mobile-first, WhatsApp-integrated booking system with:
- WhatsApp bot for 24/7 patient booking (Hindi/English)
- Automated reminders (24hr + 1hr before appointments)
- UPI advance payment (₹200-500) to reduce no-shows
- Mobile app for staff (schedule + walk-in management)
- Optional: AI voice calling

### Success Criteria (3 Months)

| Metric | Baseline | Target |
|--------|----------|--------|
| **No-Show Rate** | 25-30% | <12% |
| **Staff Scheduling Time** | 15 hrs/week | <5 hrs/week |
| **Booking Conversion** | 60% | 85% |
| **Patient Satisfaction** | 3.8/5 | 4.3/5 |
| **Revenue Impact** | Baseline | +₹30k/month |

---

## Goals & Objectives

### Business Goals
- **Primary:** 100 paying clinics in 6 months (₹3.5L MRR)
- 40% trial-to-paid conversion
- <10% monthly churn
- 30% referral-driven growth
- NPS >50

### User Goals

**Clinic Staff:**
- Instant WhatsApp responses (even when busy)
- Zero double-bookings
- No manual reminder calls
- Work-life balance restored

**Clinic Owners:**
- No-show rate: 28% → <12%
- 20-25 patients/day consistently
- ROI: ₹30k+ monthly savings
- Professional image

**Patients:**
- Book in <2 minutes via WhatsApp
- Instant confirmation
- Automated reminders
- UPI advance payment

---

## Out of Scope (V1)

-Multi-clinic management  
-Electronic medical records (EMR)  
-Lab integrations  
-Inventory management  
-Google Calendar sync  
-Patient portal/login  
-Insurance claim processing  
-Regional languages beyond Hindi  
-Desktop/web version for staff  
-Video consultations

**Rationale:** Focus on 5 core features that solve the critical problem. Additional features based on usage data.

---

## Product Architecture

```
PATIENT SIDE                    CLINIC SIDE
┌─────────────┐                ┌──────────────┐
│  WhatsApp   │                │   Staff      │
│  Bot (24/7) │──┐             │   Mobile/    |
|             |                |  Application │
└─────────────┘  │             └──────────────┘
                 │                      │
┌─────────────┐  │                      │
│ Voice Call  │──┤                      │
│ AI          │  │                      │
└─────────────┘  │                      │
                 ▼                      ▼
          ┌──────────────────────────────┐
          │     Backend Server           │
          │  (Node.js + PostgreSQL)      │
          └──────────────────────────────┘
                 │              │
          ┌──────┴──────┐      │
          ▼             ▼      ▼
    WhatsApp API   Voice AI   Payment
    (Twilio)       (Vapi.ai)  (Razorpay)
```

---

## Core Features & Requirements

### 1. Patient Booking (WhatsApp Bot)

#### 1.1 Booking Initiation
**User Story:** Patient messages clinic → bot responds in <5 seconds with options

**Acceptance Criteria:**
- Detects booking intent from: "appointment", "slot", "booking", Hindi equivalents
- Responds with: Clinic name + quick reply buttons [Today] [Tomorrow] [This Week] [Next Week]
- Works 24/7, even when clinic closed
- Multi-language: English + Hindi code-switching

**Technical:**
- WhatsApp Business API (Twilio/MessageBird)
- NLP: Keyword matching + GPT-4 fallback
- Response time <5 sec (95th percentile)

---

#### 1.2 Slot Selection
**User Story:** Patient sees available slots → selects time → instant confirmation

**Acceptance Criteria:**
- Displays slots as clickable buttons (e.g., [6:00 PM] [6:30 PM] [7:00 PM])
- Shows 12-hour format, doctor name (if multiple)
- Real-time availability (no double-booking)
- Max 6 slots shown at once
- Grayed-out unavailable slots

**Technical:**
- API: `GET /availability?date=YYYY-MM-DD&clinicId=X`
- Slot algorithm: 30-min intervals, buffer time, existing bookings
- Concurrent booking protection: Optimistic locking
- Response time <500ms

**Business Rules:**
- Don't show past slots
- Account for: Clinic hours, doctor availability, buffer time (10 min)
- If all slots full → suggest next available date

---

#### 1.3 Patient Details & Confirmation
**User Story:** Patient provides name/phone → sees booking summary

**Acceptance Criteria:**
- First-time: Asks name + phone (auto-filled from WhatsApp)
- Returning: Auto-fills details, confirms
- Optional: Reason [Checkup] [Cleaning] [Pain] [Other]
- Shows summary: Date, Time, Doctor, Location (Google Maps link)

**Technical:**
- Patient profile: Phone as unique ID
- Session management: Remember details within conversation
- Google Maps API for location link

---

#### 1.4 UPI Advance Payment
**User Story:** Patient pays ₹200 advance via UPI to secure slot

**Acceptance Criteria:**
- Payment link opens PhonePe/Google Pay directly (UPI intent)
- Backup: QR code image
- Amount: ₹200 (clinic-configurable ₹100-500)
- Timeout: 5 minutes
- Success → confirmation + receipt PDF
- Failure → retry option or "Pay at Clinic"

**Technical:**
- Razorpay Payment Gateway
- Webhook: Payment status (success/failure)
- Refund API ready

**Refund Policy:**
- 24+ hrs before: 100% refund
- 12-24 hrs: 50% refund
- <12 hrs: No refund

---

#### 1.5 Reminders & Follow-ups
**User Story:** Patient receives automated reminders to prevent no-shows

**Acceptance Criteria:**

**Immediate confirmation:**
- WhatsApp message + Google Calendar .ics + SMS fallback

**24-hour reminder:**
```
Reminder: Tomorrow 6:00 PM appointment
Dr. Priya at Smile Dental Clinic
[Confirm] [Reschedule] [Directions]
```
- Sent 6pm day before
- WhatsApp + SMS (both)

**1-hour reminder:**
```
Your appointment is in 1 hour (6:00 PM).
See you soon! 😊
[Get Directions]
```

**Post-appointment (2 hrs after):**
```
Thanks for visiting!
Rate your experience: [5★] [4★] [3★] [2★] [1★]
```

**Technical:**
- Cron job (every 10 min, check reminders due)
- WhatsApp Business API templates (pre-approved)
- SMS gateway (MSG91/Twilio fallback)
- Calendar generation (.ics format)

---

### 2. Staff Mobile App

#### 2.1 Daily Schedule View
**User Story:** Staff views today's appointments on home screen

**Acceptance Criteria:**
- Default: Today's appointments (chronological list)
- Each card shows:
  - Time, Patient name, Phone (click-to-call)
  - Status: [Confirmed] [Pending] [Walk-in] [Completed] [No-show]
  - Payment: ₹200 paid, ₹800 pending
- Color-coded: Green (confirmed), Yellow (pending), Blue (walk-in), Gray (completed), Red (no-show)
- Pull-to-refresh for updates
- Real-time push notifications for new bookings

**Technical:**
- React Native (Android first)
- API: `GET /appointments?date=today&clinicId=X`
- WebSocket for real-time updates
- Offline cache + sync

**Performance:**
- Load time <2 seconds
- Works offline (cached data)
- Touch targets ≥44px

---

#### 2.2 Walk-In Management
**User Story:** Staff adds walk-in patients in <30 seconds

**Acceptance Criteria:**
- Big [+ Add Walk-In] button on home screen
- Form: Name (required), Phone (required), Time (auto-filled, editable), Reason (optional)
- Submit → added to today's schedule
- No payment required (collected in person)
- Auto-links to existing patient if phone number matches

**Technical:**
- API: `POST /appointments/walkin`
- Phone validation + duplicate check
- Conflict detection (warns if overlaps)

**Business Rules:**
- Walk-ins marked with "Walk-in" source tag
- Can "squeeze in" even if slots full (15-min buffer)

---

#### 2.3 Appointment Status Management
**User Story:** Staff marks completed/no-show to keep schedule accurate

**Acceptance Criteria:**
- Swipe left → [✓ Completed] [✗ No-Show] [Reschedule]
- **Completed:** Card grayed out, triggers post-appointment WhatsApp (2 hrs later)
- **No-show:** Marked red, doctor gets end-of-day summary
- **Reschedule:** Opens booking flow, patient gets WhatsApp notification
- Undo within 5 minutes (accidental marks)

**Technical:**
- API: `PATCH /appointments/:id/status`
- Push notification to doctor (no-show summary)

---

#### 2.4 Payment Collection
**User Story:** Staff tracks and collects balance payments

**Acceptance Criteria:**
- Card shows: ₹200 paid (advance) ✓, ₹800 pending, [Collect Balance]
- Options: [Cash] [UPI] [Partial]
- **Cash:** Marks "Paid - Cash"
- **UPI:** Sends payment link to patient WhatsApp
- **Partial:** Enter amount, track remaining balance
- End-of-day summary: "Total collected: ₹18,500"

**Technical:**
- API: `POST /payments`
- Razorpay UPI link generation

---

### 3. AI Voice Calling (Optional)

#### 3.1 Voice Booking
**User Story:** Patient calls clinic → AI books appointment in Hindi/English

**Acceptance Criteria:**
- AI answers within 2 rings
- Greeting: "Namaste, aap Smile Dental Clinic ko call kar rahe hain. Main aapki appointment book kar sakti hoon. Aapka naam kya hai?"
- Supports: Hindi, English, Hinglish (code-switching)
- Collects: Name, phone, preferred date/time
- Real-time availability check
- Confirms booking + sends WhatsApp confirmation
- Call duration: <2 minutes
- If AI fails (>2 attempts) → transfer to staff

**Technical:**
- Vapi.ai API integration
- GPT-4 with Hindi fine-tuning
- Function calling: `check_availability()`, `book_appointment()`
- Call recording storage (quality assurance)

**Conversation Flow:**
```
AI: "Namaste, Smile Dental Clinic. Aapka naam?"
Patient: "Amit Verma"
AI: "Amit ji, appointment kab chahiye?"
Patient: "Is week mein, evening"
AI: "Ek minute... Wednesday 6pm available. Chalega?"
Patient: "Haan"
AI: "Perfect! Wednesday 6pm booked. WhatsApp confirmation aayega. Thank you!"
```

**Edge Cases:**
- Regional language only → "I understand Hindi and English only. Connecting to staff..."
- Medical question → "I only help with appointments. Please visit clinic for medical questions."
- Call drops → WhatsApp: "Call disconnected. Continue booking: [Link]"

---

### 4. Doctor Dashboard (WhatsApp)

#### 4.1 Daily Summary
**User Story:** Doctor receives morning summary and evening report via WhatsApp

**Morning (8:00 AM):**
```
Good Morning Dr. Priya! ☀️

Today's Schedule (Thu 16th May):
📋 12 appointments booked
✅ 10 confirmed
⏳ 2 pending confirmation

Peak hours: 6-7pm (4 appointments)

[View Full Schedule]
```

**Evening (9:30 PM):**
```
Today's Summary 📊

Patients seen: 18
- Booked: 15
- Walk-ins: 3

No-shows: 2 (Ram Sharma 6pm, Priya Patil 7:30pm)

Revenue: ₹22,400
- Collected: ₹18,600
- Pending: ₹3,800

[Detailed Report]
```

**Technical:**
- Cron job (scheduled WhatsApp messages)
- API: `GET /analytics/daily-summary`
- WhatsApp Business API templates

---

#### 4.2 Weekly/Monthly Reports
**User Story:** Doctor tracks business performance and system ROI

**Weekly (Every Monday 9am):**
```
Weekly Report (May 6-12) 📈

Appointments: 78 (↑12% vs last week)
No-show rate: 9% (↓ from 28% before!)
Revenue: ₹98,500

Busiest day: Thursday (20 patients)
Top treatment: Cleanings (32)

[View Details]
```

**Monthly (1st of month):**
```
Monthly Report (April 2026) 🎉

Appointments: 320
No-show rate: 11% (saved ₹34,000!)
Revenue: ₹3.8 lakhs

Time saved: 48 hours
Patient rating: 4.6★ (from 3.9★)

[Full Report PDF]
```

**Technical:**
- Analytics dashboard (web, opens in WhatsApp browser)
- Charts: Line graph (appointments), pie chart (treatments)
- PDF export

---

### 5. Clinic Onboarding

#### 5.1 Setup Flow
**User Story:** New clinic completes setup in <10 minutes

**WhatsApp-Based Setup:**
```
Welcome to DentBook! 👋

Let's set up in 3 minutes:

1️⃣ Clinic name?
2️⃣ Location (city)?
3️⃣ Operating hours? (e.g., 5pm-9pm)
4️⃣ Doctor name(s)?
5️⃣ Phone for bookings?

[Start Setup]
```

**After Setup:**
- WhatsApp bot activated (test booking sent)
- Staff app invite (download link)
- 5-min tutorial video (Hindi/English)
- Optional: 15-min onboarding call

**Success Metric:**
- 80% complete setup in <10 minutes
- 90% test-book successfully

---

#### 5.2 Configuration Settings

**Configurable via Staff App:**

**Operating Hours:**
- Days (Mon-Sat, custom)
- Timings per day
- Lunch breaks/closures

**Appointments:**
- Duration (20/30/45 min)
- Buffer time (5/10 min, none)
- Advance payment (₹100/200/500, none)
- Cancellation policy (24hr/12hr/no refund)

**Staff:**
- Add/remove members
- Assign permissions

**Doctor Availability:**
- Individual schedules (multi-doctor)
- Block dates (holidays, leave)

**Messaging:**
- Customize WhatsApp greeting
- Enable/disable AI voice
- Reminder timing (24hr/2hr/both)

---

## Non-Functional Requirements

### Performance

| Metric | Target | Measurement |
|--------|--------|-------------|
| WhatsApp bot response | <5 sec (P95) | Message → reply |
| Availability API | <500ms | Query + calculation |
| App launch (cold start) | <2 sec | To usable screen |
| App screen load | <1 sec | Cached instant, API background |
| Payment link generation | <3 sec | After booking confirmed |

### Reliability
- **Uptime:** 99.5% during clinic hours (5-9pm IST)
- **Message delivery:** 98%+ (SMS fallback)
- **Database backup:** Hourly, 30-day retention
- **Payment success:** 95%+ (Razorpay standard)

### Scalability
- 500 clinics × 20 patients/day = 10,000 bookings/day
- 50,000 WhatsApp messages/day
- PostgreSQL with read replicas (10M appointments/year)
- Auto-scaling for peak load (6-8pm IST)

### Security
- **Encryption:** AES-256 at rest, TLS 1.3 in transit
- **PII:** Phone numbers hashed, names not in logs
- **Payments:** PCI-DSS compliant (Razorpay)
- **Auth:** JWT tokens (24hr expiry)
- **Rate limiting:** 10 requests/min per IP

### Compatibility
- **Android:** 8.0+ (API 26+, covers 95% devices)
- **iOS:** Phase 2
- **WhatsApp:** Latest (2-year back-compat)
- **Browsers:** Chrome, Firefox, Safari (last 2 versions)

### Data & Privacy
- **Residency:** India (AWS Mumbai)
- **GDPR-inspired:** Right to delete
- **Retention:** >2 years archived, >5 years deleted
- **Consent:** Explicit opt-in for marketing
- **Compliance:** DISHA-aware

---

## Testing Requirements

### Unit Tests
- Backend APIs: 80%+ coverage
- Payment flows: 100% coverage
- Booking logic: All edge cases

### Integration Tests
- WhatsApp end-to-end booking
- Payment gateway (mock Razorpay)
- Voice AI (mock Vapi)

### UAT (Beta Phase, 10 Clinics)
- 2-week trial
- Daily feedback calls
- Track: No-show reduction, satisfaction, bugs

**Launch Gates:**
- <5% app crash rate
- <1% payment failure rate
- 70%+ booking completion rate
- 4.0+ star rating from beta users

---

## Launch Plan

### Phase 1: Beta (Month 1-2)
**Goal:** Validate PMF with 10 clinics

**Success Criteria:**
- 8/10 use daily
- 20%+ no-show reduction (5+ clinics)
- 6/10 willing to pay ₹3,500/month
- <10 critical bugs

---

### Phase 2: Soft Launch (Month 3-4)
**Goal:** 50 paying clinics

**GTM:**
- Referral program ("Refer dentist, both get ₹1k credit")
- YouTube testimonials
- Dentist WhatsApp groups
- Google Ads ("Reduce no-shows 50%")

**Pricing:**
- Free trial: 1 month
- Paid: ₹3,500/month (cancel anytime)
- Annual: ₹35,000/year (17% discount)

**Success Criteria:**
- 40% trial → paid
- <15% churn
- NPS >40
- 20% referral-driven

---

### Phase 3: Public Launch (Month 5-6)
**Goal:** 100 paying clinics (₹3.5L MRR)

**Marketing:**
- PR (TechCrunch, YourStory)
- IDA conference booth
- Dental influencers
- Case studies

**Product:**
- iOS app (if demand)
- Regional languages (Tamil, Telugu)
- Advanced analytics

**Success Criteria:**
- 100 paying clinics
- ₹3.5L MRR
- <10% churn
- NPS >50

---

## Technical Stack

### Backend
- **Language:** Node.js (TypeScript)
- **Framework:** Express.js
- **Database:** PostgreSQL 14+ (AWS RDS)
- **Caching:** Redis
- **Queue:** BullMQ (async tasks)

### Frontend
- **Mobile:** React Native
- **State:** Redux Toolkit
- **UI:** React Native Paper
- **Dashboard:** Next.js + Tailwind

### Infrastructure
- **Hosting:** AWS Mumbai (ECS Fargate, RDS Multi-AZ, S3, CloudFront)
- **Monitoring:** CloudWatch + Sentry
- **CI/CD:** GitHub Actions, blue-green deployment

---

## Pricing

| Plan | Price | Target | Features |
|------|-------|--------|----------|
| **Free Trial** | ₹0 | New clinics | 1 month, 50 bookings max |
| **Starter** | ₹3,500/month | 1-2 dentists | Unlimited bookings, WhatsApp, SMS, mobile app |
| **Growth** | ₹5,500/month | 3+ dentists | Starter + AI voice + priority support |
| **Annual** | ₹35,000/year | Price-conscious | Starter annual (save 17%) |

**Add-ons:**
- AI Voice: +₹1,500/month
- Custom branding: +₹1,000/month
- Dedicated phone: +₹500/month

---

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| WhatsApp API policy change | High | SMS fallback, web booking |
| Low clinic adoption | Critical | 10-min onboarding, clear Week 1 ROI |
| No-show reduction <20% | High | A/B test reminder timings, phone backup |
| Staff resistance | High | Optional mode, "assistant" feature first |
| Competition launches | Medium | Move fast, WhatsApp-first moat, annual lock-in |

---

## Development Roadmap

**Sprint 1-2 (Weeks 1-4):** Database, backend API, WhatsApp integration, staff app (login + schedule)

**Sprint 3-4 (Weeks 5-8):** Full booking flow, Razorpay, SMS reminders, staff app (walk-in + status)

**Sprint 5-6 (Weeks 9-12):** AI voice, doctor dashboard, analytics, beta testing

**Sprint 7-8 (Weeks 13-16):** Onboarding optimization, performance testing, security audit, app store submission

**Post-Launch:** iOS app, regional languages, advanced features

---

## Definition of Done

**Per Feature:**
- Code reviewed (2 engineers)
- Unit tests (80%+ coverage)
- Integration tests pass
- Tested on ₹10-15k Android phones
- Hindi + English verified
- Documented
- Staged + PM verified
- Demo video recorded

**MVP Launch:**
- 10 beta clinics (2 weeks)
- No P0/P1 bugs
- <1% payment failure
- 70%+ booking completion
- 4.0+ star rating
- Legal review complete
- Support playbook ready


---

**Last Updated:** May 17, 2026  
**Version:** 1.0 — Initial PRD approved
