# Website Requirements and MVP Scope

Last updated: 23 October 2026, Asia/Dhaka.

“Confirmed” means directly answered by the user. “Recommended” means proposed by this planning review. “Pending” means an answer or company decision is still needed. The user authorized implementation on 23 October after the V3 cleanup; the earlier design-only restriction is superseded by R23.

## Confirmed requirements

| ID | Requirement |
| --- | --- |
| R01 | Work for a Real Capita Group plot development business based in Gulshan-1, Dhaka, Bangladesh |
| R02 | The business develops its own properties and brokers other owners' properties |
| R03 | Launch with two land listings, publicly named Project 01 and Project 02 per the user's 23 October naming change; no project/subplot hierarchy is established |
| R04 | Serve local homebuyers aged 35–60; local investors may also visit; overseas targeting is outside scope |
| R05 | Provide both Bangla and English; most visitors will use phones |
| R06 | Let visitors browse available plots, location, actual photographs, and complete relevant details |
| R07 | Display prices publicly in BDT and land area in katha and square feet |
| R08 | Include photographs, a walkthrough video, and a 360° panorama; the administrator will supply them |
| R09 | Provide a staff administration area to maintain listings and media |
| R10 | Include an AI assistant with free-text Bangla and English conversations |
| R11 | When interested, visitors can obtain an approved manager/admin contact and send their details to authorized staff |
| R12 | With permission, collect only name, phone, interested plot, and an optional short message |
| R13 | No customer accounts, customer login, appointment scheduling, online reservation, or payments |
| R14 | Prioritize UI/UX, accessibility, security, privacy, simplicity, and maintainability |
| R15 | Deliver in approximately one to one-and-a-half months; a teammate will maintain the site |
| R16 | Establish the development workflow; a local Git repository now exists, with the company-owned private remote still pending |
| R17 | Original design-only instruction: create planning documentation first and preserve supplied files. Implementation hold superseded by R23; preservation remains required |
| R18 | Use the manager's V1 feedback to reduce homepage text and create a more modern, image-led visual direction; show multiple homepage candidates before developing the approved direction into full V3 |
| R19 | Add homepage Gallery and Virtual Site Visit sections as included in the selected Open Horizon design; Virtual Site Visit uses the existing video/panorama requirements and comes from feature 8 of the original document |
| R20 | A / Open Horizon is the selected homepage direction, final for now. Use Projects, Project 01 and Project 02 consistently in current/future public UI; all V3 screens follow this direction |
| R21 | Produce a complete V3 design folder comparable to V1/V2, covering all agreed public pages, gallery/media views, AI/inquiry and staff workflows with mobile/Bangla examples; a homepage-only deliverable is insufficient |

| R22 | Keep only fourteen important selected V3 images in the main folder and archive superseded alternatives; completed |
| R23 | Start building the project from V3 now; use sample photos, videos and 360° imagery until actual project media are supplied later |

The initial “no personal data” answer was clarified: the four minimal lead fields in R12 are permitted after asking the visitor's permission. Identity documents, financial records, addresses, customer uploads, and payment information remain outside scope.

## MVP visitor journey

1. Open the site and choose Bangla or English.
2. See the two available listings without needing search or registration.
3. Open a listing and inspect price, size, location, status, actual photos, video, panorama, and approved details.
4. Ask the AI assistant a question or use a visible direct contact option.
5. If desired, submit a separate contact form after a clear privacy explanation and affirmative permission.
6. Receive a submission confirmation and approved staff contact. Staff follow-up happens outside the website; it is not an appointment or booking.

## Proposed public pages

| Page | Essential content |
| --- | --- |
| Home | Short visual hero, two listing previews with essential facts, Gallery and Virtual Site Visit sections, concise contact path; minimize prose |
| Projects | Both listings, Project 01 and Project 02, with photo, location, area, BDT price, availability, and details link |
| Project detail | Accurate specifications, labeled media, location, status, authoritative price, and interest/contact action |
| About | Staff-approved company information and relationship to the group |
| Contact | Approved business contact and office details; no scheduling system |
| Privacy | Actual data flows, AI provider disclosure, retention, recipients, and privacy contact |
| Website Terms | Information accuracy, media labels, and distinction between inquiries and contractual transactions |

The AI assistant is a shared feature, not another navigation item. Videos and panoramas remain available inside the plot detail page and are also proposed in a homepage Virtual Site Visit preview. Gallery is a requested homepage section; a separate gallery page is not yet confirmed. Location information and any future approved brochure belong inside the plot detail page. Gallery navigation may link to the homepage section. Large media remains user initiated.

## Proposed staff functions

Create and edit the two listings; maintain Bangla and English content; set price and availability; upload approved media; preview and publish content; edit approved public contact details and FAQs. If lead capture is enabled, permitted staff can see new inquiries and mark them contacted or closed. This is a small inquiry inbox, not a full CRM.

Use individual staff accounts and least-privilege permissions. A proposed role matrix appears in SECURITY.md. The user's tentative admin/manager/sub-admin/super-admin labels do not yet establish access rights.

## Listing content requirements

Each listing needs a stable reference, bilingual title and description, locality, verified map coordinates or link, area and units, total BDT price, price basis, availability, date last reviewed, ownership/sales relationship, nearby facilities, verified road/facing information where applicable, and media descriptions.

Use decimal values for money and measurements. Company staff must supply the authoritative area and confirm any katha-to-square-foot conversion convention. Never invent a land conversion, approval, possession date, ownership claim, or investment return. If a price is per katha rather than total, label it explicitly and present a verified total.

Availability is staff-maintained information, not a real-time reservation guarantee. Define draft/published/archived separately from available/under discussion/sold. Proposed status wording needs company approval.

## AI assistant requirements

The assistant answers using current, published plot facts and approved company FAQs. It responds in the visitor's selected language and supports Bangla, English, and mixed-language questions. Authoritative price, area, and availability cards must come from application data.

The assistant may offer a secure contact form but must not submit a lead on the visitor's behalf. Names and phone numbers entered into that form are not sent to the model. The model has no access to staff accounts, customer leads, unpublished listings, private documents, or administrative actions.

The provider, budget, disclosure, and model are recommendations pending company review. AI processing can involve overseas services even though the audience is domestic. Chat must remain useful when the provider fails by showing approved FAQs and staff contact. The requested AI feature is not considered complete merely because a fallback exists.

## MVP acceptance criteria

| Area | Acceptance evidence |
| --- | --- |
| Browsing | Both published listings are easy to find; unpublished/archived content cannot leak through public URLs or chat |
| Content | All prices, areas, locations, claims, translations, and media labels are approved by company staff |
| Mobile usability | No unintended horizontal scrolling; important tasks remain simple at 320px width; test on actual Android and iPhone devices |
| Language | Both versions cover pages, controls, forms, validation, AI disclosure, and privacy information; switching preserves the listing |
| Media | Actual images distinguished from renders; video is user initiated; panorama is user initiated with a usable photo/text fallback |
| AI | Bilingual fact and adversarial evaluations pass; no invented price/booking promise or access to nonpublic information |
| Leads | Explicit visitor submission and permission; no contact details in AI requests, URLs, analytics, or application logs |
| Staff | Permission matrix, MFA, direct URL access, publishing, and lead visibility verified with separate role accounts |
| Security | Required scans, abuse controls, deployment checks, privacy review, and backup restore test pass |
| Accessibility | WCAG 2.2 AA target checked through automated checks and manual keyboard, zoom, and screen-reader review |
| Handover | Teammate can update a listing, handle a lead, restore a backup, and follow documented deployment steps |

## Excluded from this MVP

Customer accounts and dashboards; appointment scheduling; online booking, reservation, or payment; customer file uploads; native mobile apps; advanced search/filtering; clickable plot inventory maps; full CRM/pipeline/team automation; referral/discount programs; ROI or investment prediction; AI recommendations based on customer profiling; push notifications; live-agent chat software; and a blog.

SMS, advertising pixels, third-party analytics, embedded maps, public land-document downloads, and WhatsApp integrations are optional future decisions. A direct telephone contact is sufficient for launch unless the company chooses another channel. Filters can be reconsidered when the catalog grows enough that visitors need them.

## Decisions still needed

| ID | Missing decision | When needed |
| --- | --- | --- |
| Q01 | Exact registered entity and approved brand name | Before final legal text and publication |
| Q02 | Domain, existing host, Python support, monthly hosting and AI budgets | Before deployment/provider commitment |
| Q03 | Staff responsibilities, named role assignments, publishing approver, and lead recipients | Before protected workflows are implemented |
| Q04 | Approved business contact, office address, hours, and follow-up expectations | Before contact/handoff is complete |
| Q05 | Privacy owner, lawful processing basis, lead retention, deletion process, and processor arrangements | Before collecting production customer data |
| Q06 | Approved AI provider, processing location, terms, billing owner, and transfer assessment | Before sending production conversations |
| Q07 | Both listings' accurate facts, measurement convention, media files, usage rights, and translations | Before content implementation and launch QA |
| Q08 | Default language, maintainer's technical skills, browser/device baseline, and remaining V3 screen review. Homepage direction resolved: A / Open Horizon, final for now | During design refinement |
| Q09 | Company-approved recovery objectives and backup retention | Before production readiness |

Unknown decisions remain open; they must not be silently treated as approved defaults.
