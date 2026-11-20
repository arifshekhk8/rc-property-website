# Decisions

Last updated 21 November 2026.

Accepted decisions, oldest first. "Arif" means Arif made the decision or passed it on from the manager or company. A later decision overrides an earlier one; update the affected docs when that happens.

## Accepted

| ID | Date | Decision |
| --- | --- | --- |
| D01 | 15 Oct | Django is the backend (Arif's choice) |
| D02 | 15 Oct | Launch with two individual land plots; no project/plot hierarchy |
| D03 | 15 Oct | Audience: local homebuyers, mostly on phones, in Bangla and English |
| D04 | 15 Oct | Show prices publicly in BDT; land area in katha and square feet |
| D05 | 15 Oct | Use the admin's existing photos, walkthrough video and 360° panorama; no 3D model |
| D06 | 15 Oct | Staff administration is required; who does what is still open (Q03) |
| D07 | 15 Oct | Free-text bilingual AI assistant. Arif chose this over a guided-menu assistant |
| D08 | 15 Oct | With permission, collect only name, phone, chosen plot and an optional short message. This clarifies Arif's earlier "no personal data" answer |
| D09 | 15 Oct | No customer accounts, appointments, bookings or payments |
| D10 | 15 Oct | Premium, welcoming design for ages 35–60; accessibility, security and privacy come first |
| D11 | 15 Oct | Timeline of about 1–1.5 months; a teammate maintains the site afterwards |
| D12 | 15 Oct | Write the planning docs before building; never change the supplied files |
| D13 | 15 Oct | Show page designs first; no code yet |
| D14 | 15 Oct | Make a separate V2 with brighter, plot-focused imagery and keep V1 |
| D15 | 15 Oct | Arif rejected V2's repeated plot images: each property needs its own look, and no filler photos |
| D16 | 23 Oct | Manager: V1 is broadly fine but too wordy, "like a newspaper". Use it as the base for a more modern, image-led design |
| D17 | 23 Oct | Add Gallery and Virtual Site Visit sections (feature 8 of the original document). No new transactional features |
| D18 | 23 Oct | Show several homepage options before designing the full V3 |
| D19 | 23 Oct | Arif chose **A / Open Horizon**, final for now |
| D20 | 23 Oct | Rename the listings **Project 01 / Project 02** (প্রকল্প 01 / 02). Display names only; no hierarchy |
| D21 | 23 Oct | V3 must be a complete pack like V1 and V2, not just a homepage |
| D22 | 23 Oct | Keep only the 14 selected V3 boards in the main folder and archive the rest |
| D23 | 23 Oct | Arif: "Okay lets start." Build from V3 with sample photos, video and 360° imagery |
| D24 | 23 Oct | Audit the build against the plan and security rules, fix the gaps, and push to a new private repo in focused commits |
| D25 | 7 Nov | Continue development in a new private repo, `rcpdl-website`. This repo keeps the foundation and changes only when Arif asks |
| D26 | 21 Nov | Arif asked for a code review, then the template cleanup, the 404 fix, a docs rewrite and a tidier folder layout in this repo. The docs are internal working notes |

## Engineering choices (made during the build, 23 October)

These are our technical choices, not company approvals.

- Custom CSS instead of Bootstrap, to match V3 without fighting framework defaults.
- A flat catalog: `Project`, `ProjectImage` and `FAQ`.
- SQLite for local development only, because PostgreSQL and Docker weren't available on this Mac. Production refuses to start without PostgreSQL over TLS, and CI tests on PostgreSQL 17.
- Python pinned to 3.13.16 locally and in CI.
- No inquiry storage and no AI requests until the company decides recipients, privacy notice, retention and provider (Q03–Q06). Both features are still required.
- `main` needs a pull request and passing checks. There's no second reviewer yet, so independent review is a launch gate.

## Proposals

Our recommendations, with their current status. None of these is a company approval.

| ID | Proposal | Status |
| --- | --- | --- |
| P01 | Django 5.2 LTS, Python 3.13, PostgreSQL 17 | In use: Django 5.2.18, Python 3.13.16, PostgreSQL 17 in CI |
| P02 | Django templates, custom CSS, small JavaScript | In use |
| P03 | A customised Django admin instead of a separate dashboard | In use; check it with real staff |
| P04 | Self-hosted Pannellum, loaded only when asked | In use with a sample panorama; check the real file's format and size |
| P05 | Keep the inquiry form separate from the AI chat | Planned. Inquiry fields must never reach the model |
| P06 | OpenAI Responses API adapter; evaluate GPT-5.4 mini | Candidate only. Test Bangla quality, speed, cost and privacy first |
| P07 | No stored chat transcripts, vector database, autonomous tools or profiling | Planned |
| P08 | Roles: system admin, manager, content editor, all with MFA | Draft matrix in SECURITY.md; the company must confirm |
| P09 | Darker blue/green palette, self-hosted Noto fonts | In use; design review pending |
| P10 | Location as text plus a staff-chosen map link; no embedded map | Planned; needs real coordinates |
| P11 | No search or filters at launch | Still applies. Gallery and Virtual Site Visit pages exist as samples |
| P12 | Company-owned private GitHub repo with checks | The repo is private under Arif's account; transfer to the company is pending |
| P13 | Managed Python hosting, PostgreSQL, private media storage, separate staging | No provider chosen |
| P14 | Keep leads 90 days and logs/backups 30 days (starting point for discussion) | Needs company and legal approval |
| P15 | Optional external AI security-review plugin | Dropped 21 Nov: local scanners and tests cover this stage |
| P16 | V1 design pack | Kept locally for reference |
| P17 | V2 design pack | Kept locally for reference |
| P18 | V3 Open Horizon pack | Implemented in this repo |

## Open questions

Q01–Q09 in [REQUIREMENTS.md](REQUIREMENTS.md#open-questions) are the master list.

The group's property page names two housing projects, RC Maya Kanon and RC Rivery Village. Arif confirmed two individual plots, so we don't assume those names. No contact found online gets published without company approval.

## Adding a decision

Add a row with the date, who decided, and what changed. If it changes scope, update REQUIREMENTS.md and PLAN.md first. Keep recommendations under Proposals until someone confirms them. Never put confidential data in a decision.
