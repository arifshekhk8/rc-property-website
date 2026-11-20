# Requirements

Last updated 21 November 2026.

**Confirmed** means Arif answered it directly, or passed it on from the manager or company. **Recommended** means it's our proposal. **Open** means it still needs an answer.

## Confirmed

| ID | Requirement |
| --- | --- |
| R01 | A website for a Real Capita Group plot development business in Gulshan-1, Dhaka |
| R02 | The business develops its own land and brokers land for other owners |
| R03 | Launch with two listings, named Project 01 and Project 02 (D20); no hierarchy |
| R04 | Audience: local homebuyers aged 35–60, plus local investors. Overseas buyers are out of scope |
| R05 | Bangla and English; most visitors use phones |
| R06 | Visitors can browse available plots, location, real photos and full details |
| R07 | Public prices in BDT; area in katha and square feet |
| R08 | Photos, a walkthrough video and a 360° panorama, supplied by the admin |
| R09 | A staff admin area for listings and media |
| R10 | An AI assistant with free-text chat in Bangla and English |
| R11 | Interested visitors get an approved staff contact and can send their details to authorised staff |
| R12 | With permission, collect only name, phone, chosen plot and an optional short message |
| R13 | No customer accounts, login, appointments, reservations or payments |
| R14 | Priorities: UI/UX, accessibility, security, privacy, simplicity, maintainability |
| R15 | About 1–1.5 months of work; a teammate maintains the site afterwards |
| R16 | A private GitHub repo with a protected `main`. It's under Arif's account for now; company ownership is pending |
| R17 | Keep the supplied files unchanged |
| R18 | Follow the manager's V1 feedback: less text, more modern and image-led; show homepage options first |
| R19 | The homepage has Gallery and Virtual Site Visit sections |
| R20 | Open Horizon is the design direction; use "Projects", "Project 01" and "Project 02" everywhere |
| R21 | V3 is a complete design pack covering public pages, media, AI/inquiry and staff flows |
| R22 | Keep only the 14 selected V3 boards in the main folder (done) |
| R23 | Build from V3 now, with sample media until real media arrives (done) |
| R24 | Audit the build against the plan and security rules, using a private repo with focused commits (done) |

Arif's first answer was "no personal data". It was later clarified to the four fields in R12, collected only after asking. ID documents, financial records, home addresses, customer uploads and payments stay out of scope.

## Visitor journey (MVP)

1. Open the site and choose Bangla or English.
2. See both listings without searching or signing up.
3. Open a listing: price, size, location, status, photos, video, panorama and approved details.
4. Ask the AI assistant, or use a visible direct contact.
5. Optionally send the separate inquiry form, after a clear privacy note and explicit permission.
6. See a confirmation and the approved staff contact. Follow-up happens outside the website; it's not a booking.

## Pages

| Page | Must contain | Built? |
| --- | --- | --- |
| Home | Short image hero, both listings with key facts, Gallery, Virtual Site Visit, contact path | Yes, with samples |
| Projects | Both listings: photo, location, area, BDT price, availability, details link | Yes, with samples |
| Project detail | Facts, labelled media, location, status, price, inquiry button | Yes, with samples; location pending |
| Gallery | Approved photos with captions in both languages and a photo viewer | Yes, with samples |
| Virtual Site Visit | Video and panorama that start only when asked, a project picker, photo fallback | Yes, with samples |
| About | Approved company information and how it relates to the group | Yes; placeholder text |
| Contact | Approved phone and office address; no scheduling | Yes; contacts pending |
| Privacy | Real data flows, AI disclosure, retention, recipients, privacy contact | Draft |
| Terms | Accuracy of information, media labels, inquiry versus contract | Draft |

The AI assistant is a floating button on every page, not a menu item. Location lives on the project page. Land documents and brochures are out of scope for now. Large media loads only when the visitor asks for it.

## Staff functions

Edit both listings in both languages; set price and availability; upload approved media; preview and publish; edit public contacts and FAQs. Once inquiries are stored, permitted staff can see them and mark them contacted or closed. This is a small inbox, not a CRM.

Each staff member gets their own account with only the permissions they need. The draft role matrix is in [SECURITY.md](SECURITY.md#staff-roles-draft). Arif's role labels (admin, manager, sub-admin, super-admin) don't define access rights yet.

Built so far: listing and FAQ editing, photo upload with rights and approval flags, publish permission, MFA. Not built: draft/review revisions, contact editing, the inquiry inbox.

## Listing content

Each listing needs a stable reference, title and description in both languages, locality, a verified map link or coordinates, area and units, total BDT price and what the price covers, availability, last-reviewed date, ownership or sales relationship, nearby facilities, road and facing details where relevant, and media descriptions.

- Store money and measurements as decimals.
- The company supplies the official area and confirms its katha-to-square-foot convention. Never invent a conversion, approval, possession date, ownership claim or investment return.
- If a price is per katha, label it that way and show a verified total.
- Staff set availability by hand; it is not a live reservation. Keep publication (draft, published, archived) separate from availability (available, unavailable; any other states need company wording).

## AI assistant

- Answers only from published listing facts and approved FAQs, in the visitor's language (Bangla, English or a mix).
- Price, area and availability cards come from application data, never from the model.
- May offer the inquiry form but never submits a lead itself. Names and phone numbers from the form never go to the model.
- No access to staff accounts, leads, unpublished listings, private documents or admin actions.
- Provider, budget and model are proposals pending company review. Processing may happen outside Bangladesh.
- If the provider fails, show the approved FAQs and the staff contact. A fallback alone doesn't make the AI feature done.

## Launch criteria

| Area | Evidence needed |
| --- | --- |
| Browsing | Both listings are easy to find; unpublished or archived content never leaks through URLs or chat |
| Content | Company staff approved every price, area, location, claim, translation and media label |
| Mobile | No sideways scrolling; key tasks are simple at 320 px wide; tested on a real Android phone and iPhone |
| Language | Both languages cover pages, controls, forms, errors, AI disclosure and privacy text; switching language keeps the listing |
| Media | Real photos are clearly told apart from renders; video and panorama start only on request and have a fallback |
| AI | Fact and adversarial tests pass in both languages; no invented prices or promises, no non-public data |
| Leads | Explicit submission and permission; no contact details in AI requests, URLs, analytics or logs |
| Staff | Roles, MFA, direct-URL access, publishing and lead visibility tested with separate accounts |
| Security | Scans, abuse limits, deployment checks, a privacy review and a backup restore test all pass |
| Accessibility | WCAG 2.2 AA target: automated checks plus manual keyboard, zoom and screen-reader testing |
| Handover | The teammate can update a listing, handle a lead, restore a backup and follow the deployment steps |

## Out of scope

Customer accounts and dashboards; appointments; booking, reservation or payment; customer uploads; native apps; advanced search or filters; clickable plot maps; CRM or team automation; referral and discount schemes; investment-return predictions; AI profiling of customers; push notifications; live-agent chat; a blog.

Possible later additions: SMS, advertising pixels, third-party analytics, embedded maps, public land documents, WhatsApp. A phone number is enough for launch unless the company wants more. Filters can come back if the catalog grows.

## Open questions

| ID | We still need | Needed before |
| --- | --- | --- |
| Q01 | Exact registered name and approved brand name | Final legal text and publishing |
| Q02 | Domain, current host, Python support, hosting and AI budgets | Deployment and choosing an AI provider |
| Q03 | Staff responsibilities, named roles, who approves publishing, who receives leads | Building the protected workflows |
| Q04 | Approved business phone, office address, hours, follow-up promise | Finishing Contact and the handoff |
| Q05 | Privacy owner, legal basis, lead retention, deletion process, processor contracts | Collecting real customer data |
| Q06 | AI provider, processing location, terms, billing owner, data-transfer assessment | Sending real conversations |
| Q07 | Accurate facts, measurement convention, media files, usage rights and translations for both listings | Content and launch testing |
| Q08 | Default language, the maintainer's skills, supported browsers and devices, sign-off on the V3 pages beyond the homepage | Design refinement |
| Q09 | Recovery objectives and backup retention | Production readiness |

Unanswered questions stay open. Don't treat them as approved defaults.

### What to ask the company for

| Topic | Ask for |
| --- | --- |
| Both projects | Public titles, exact area in both units and the conversion used, total BDT price and what it covers, availability, location link, verified facts |
| Media | Licensed photos with captions, the walkthrough video, panorama files, capture dates, transcripts if needed |
| Brand and contact | Approved company wording, logo export, contact person and role, business phone, office address and hours |
| Staff workflow | Who edits, who reviews and publishes, who reads inquiries, who manages accounts |
| Hosting and budgets | Domain and hosting details and their owner, Python support, hosting and AI budgets |
| Privacy and AI | Why we collect data, who receives it, privacy contact, retention and deletion, provider terms, who approves |

The company should send this through its own channels. Never paste credentials into chat or these docs.
