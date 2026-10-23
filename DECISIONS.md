# Project Decisions and Changes

Last updated: 23 October 2026, Asia/Dhaka.

Record accepted decisions separately from proposed architecture. A new answer overrides earlier conflicting information and must update affected documents. Preserve the original materials.

## Accepted decisions

| ID | Date | Decision and reason |
| --- | --- | --- |
| D01 | 15 October 2026 | Django is the required backend, selected by the user |
| D02 | 15 October 2026 | Initial catalog is two individual land plots; no project/plot hierarchy is currently required |
| D03 | 15 October 2026 | Focus on domestic local homebuyers, mostly mobile, with Bangla and English |
| D04 | 15 October 2026 | Public BDT pricing and area shown in katha and square feet |
| D05 | 15 October 2026 | Use existing photos, walkthrough video, and 360° panorama supplied by the administrator; a movable 3D model is not requested |
| D06 | 15 October 2026 | Staff administration is required; actual access responsibilities remain unresolved |
| D07 | 15 October 2026 | Free-text bilingual AI assistant is required; the earlier guided-assistant recommendation was not selected |
| D08 | 15 October 2026 | Collect only name, phone, interested plot, and optional short message after asking permission; this clarifies the earlier “no personal data” answer |
| D09 | 15 October 2026 | No customer accounts/login, appointments, booking/reservation, or payments; simplify the visitor experience |
| D10 | 15 October 2026 | Premium and welcoming design; prioritize usability for ages 35–60, contrast, accessibility, security, and privacy |
| D11 | 15 October 2026 | Approximately one to one-and-a-half months; a teammate will maintain the site |
| D12 | 15 October 2026 | Plan and create/maintain the eight requested Markdown files before implementation; do not change supplied files |
| D13 | 15 October 2026 | The first active project step is showing the required page designs; the user reiterated that coding must not begin |
| D14 | 15 October 2026 | The user selected the brighter plot-focused imagery direction for a separate V2 design and required preservation of V1; this authorizes new design artifacts, not website implementation |
| D15 | 15 October 2026 | The user rejected the initial V2's repeated near-identical plot imagery; distinct property identities and context-appropriate images are required, with different gallery viewpoints and no filler photos in functional states |
| D16 | 23 October 2026 | The manager found V1 broadly acceptable but too wordy, resembling a newspaper. Use V1 as the starting point for a more modern, image-led, concise design; this is feedback, not final approval of V1 |
| D17 | 23 October 2026 | Add a Gallery section and a second suitable section from the supplied feature document. Virtual Site Visit is selected for the homepage proposals from feature 8, using the already-required walkthrough video and 360° panorama; no new transactional feature is introduced |
| D18 | 23 October 2026 | Present multiple homepage directions first. Create the complete V3 design only after the user selects a direction; preserve V1/V2 and continue to defer application implementation |
| D19 | 23 October 2026 | The user selected A / Open Horizon as final for now. Save the selected desktop homepage as the V3 visual baseline; other V3 screens remain to be designed |
| D20 | 23 October 2026 | Rename the two public listings Project 01 and Project 02 instead of Plot 01 and Plot 02. Apply Projects wording consistently in current/future UI. This changes display naming and does not itself add a project/subplot hierarchy or new inventory |
| D21 | 23 October 2026 | The user clarified that V3 must be a complete folder like V1/V2 with all agreed page designs based on the selected homepage, followed by a clear next step; complete the full design pack, not just the homepage |
| D22 | 23 October 2026 | The user requested only important images and plans to start building next. Keep one selected PNG per page/workflow in the V3 root, use canonical filenames, and move superseded drafts/homepage alternatives into an archive. No image contents are changed; implementation is the next task |

| D23 | 23 October 2026 | The user explicitly instructed “Okay lets start” and authorized temporary sample photos, videos and 360° views. This supersedes the earlier design-only implementation hold; preserve supplied originals and use V3 for the local build |

| D24 | 23 October 2026 | The user requested an audit against the original plan/security requirements, updated documentation and multiple focused commits/pushes to a new private repository. This authorizes source remediation and the private remote, not public deployment or company-operating decisions |

## Recommended technical and design decisions

| ID | Proposal | Rationale / status |
| --- | --- | --- |
| P01 | Django 5.2 LTS, Python 3.13, PostgreSQL 17 | Django 5.2.18/Python 3.13.16 installed locally; PostgreSQL CI passed and production required; local SQLite exception recorded below |
| P02 | Django templates, custom CSS, small JavaScript modules | Implemented without Bootstrap to match V3 with fewer framework defaults; engineering choice, not an additional user requirement |
| P03 | Focused Django admin instead of a separately built staff dashboard | Fits current inventory; verify usability and roles with staff |
| P04 | Self-host Pannellum and load media on demand | Uses actual supplied panorama; projection/size and accessibility still need inspection |
| P05 | Separate secure interest form from AI conversation processing | Keep lead fields out of model payloads; explicit visitor submission required |
| P06 | OpenAI Responses API adapter; evaluate GPT-5.4 mini | Candidate only; Bangla quality, latency, account availability, budget, and privacy must be approved/tested |
| P07 | No durable chat transcripts, vector database, autonomous tools, or customer profiling | Two public records need little context; minimize complexity and disclosure |
| P08 | Manager/editor/system-administrator permission matrix with staff MFA | Least privilege; role names and assignments need company confirmation |
| P09 | Darker blue/green UI palette and self-hosted bilingual fonts | Logo colors need different text/button treatment for contrast; design review pending |
| P10 | Static location information and a user-selected map link initially | Avoid an automatic third-party map embed; accurate coordinates and staff choice still needed |
| P11 | No filters/search at launch | Superseded gallery restriction: V3 includes dedicated Gallery and Virtual Site Visit pages, now implemented as sample previews |
| P12 | Company-owned private GitHub repository with automated checks | Private arifshekhk8/rc-property-website created with checks/protected main. The connected account has no company organization; ownership transfer and approved maintainers remain pending |
| P13 | Managed Python hosting, PostgreSQL, protected media, separate staging | Existing hosting details are unavailable; no provider or region selected |
| P14 | Lead retention 90 days, logs/backups 30 days as discussion defaults | Require documented company purpose, legal review, and operational approval |
| P15 | Optional Codex Security with a local-first scanner baseline | Plugin available but not confirmed installed/connected; assess code/privacy access before use |
| P16 | Version 1 visual concept in design/concepts/v1/ | Nine selected raster boards; white/navy/blue/green direction, core mobile/Bangla examples, separate inquiry consent, and proposed staff workflows; awaiting user feedback |
| P17 | Version 2 visual concept in design/concepts/v2/ | Eleven boards improve imagery, hierarchy, staff navigation, Bangla mobile coverage and recovery states; V2 remains a proposal, with actual facts/media and final visual approval pending |
| P18 | Complete V3 Open Horizon pack in design/concepts/v3/ | Fourteen selected boards extend the approved homepage across agreed public/staff pages, gallery/media, AI/inquiry, mobile/Bangla and recovery views; new boards available for comparison with the local implementation; actual content and production workflows pending |

## Implementation choices on 23 October

These are local engineering choices within D23, not company operating approvals. Use custom CSS and self-hosted fonts/viewer; keep the catalog flat with `Project`, `ProjectImage` and `FAQ` models. Local SQLite permits an immediate preview because PostgreSQL/Docker are unavailable on this machine. Production settings require PostgreSQL, and PostgreSQL 17 CI now runs and has passed. Python is pinned to patched 3.13.16 locally and in CI. See SECURITY_AUDIT.md for execution evidence. Use hashed dependency locks, staged/history secret scans and the new private remote. Main requires pull requests and passing checks, with no force-push or deletion. Independent approval is not yet enforced because no approved second maintainer exists; require that before production release.

The first milestone deliberately implements no inquiry persistence or external AI requests while recipients, notices, retention and provider arrangements remain unresolved. This does not change the agreed eventual free-text AI/inquiry requirements. Staff with publishing permission can edit current records; draft revisions/review are the next content milestone. No shared staff credential is created.

## Open decisions

Use Q01–Q09 in REQUIREMENTS.md as the authoritative list. Important unresolved items include exact legal name, actual host/domain, AI/provider budget and data arrangements, roles/lead recipients, contact information, privacy responsibility/retention, approved listing facts/units, visual/default-language approval, and recovery objectives.

Company public pages use RC Property Development Ltd. A public page naming two housing projects does not override the user's two-individual-plot answer. No public contact discovered during research is automatically the chatbot handoff contact.

## Change record

| Date | Change | Consequence |
| --- | --- | --- |
| 15 October 2026 | Reduced the broad supplied feature list to a small browsing/communication MVP | Removed accounts, appointments, transactional features, advanced inventory, CRM, and marketing tools |
| 15 October 2026 | Clarified two plots as individual listings | Keep the data model flat; do not assume a housing project inventory |
| 15 October 2026 | User selected AI free-text chat over the guided proposal | Add provider/data review, factual evaluations, abuse/spend controls, and prompt-injection safeguards |
| 15 October 2026 | Clarified minimal contact collection is permitted | Define a private inquiry flow, consent, authorized recipients, deletion, and logging controls |
| 15 October 2026 | Clarified existing media includes panorama/video | Use an on-demand panorama viewer; no custom 3D model creation |
| 15 October 2026 | Current research found Bangladesh's 2026 privacy Act | Review current legislation and commencement rather than assuming older 2025 guidance is sufficient |
| 15 October 2026 | User requested UI/UX designs as the first step, before code | Created a visual review pack and prompt archive; implementation remains deferred |
| 15 October 2026 | User rejected road-focused imagery and selected vibrant plot-focused illustrations for a new V2 | Created a separate design pack, labeled AI imagery, preserved V1, and retained the same small MVP scope; no verified/recent-property-photo claim |
| 15 October 2026 | User rejected repeated imagery across the initial V2 boards | Created eight corrected sibling boards and three distinct source illustrations under V2/imagery-revision; updated current review links, retained prior images, and preserved V1; no coding |
| 23 October 2026 | Manager feedback favors V1 with much less text; user requests multiple modern homepage options before V3 | Prepare three image-led homepage candidates under design/concepts/v3/homepage-options, with Gallery and Virtual Site Visit sections. Full V3 awaits user selection; no application code |
| 23 October 2026 | User selected A / Open Horizon and requested Project 01 / Project 02 naming | Saved a finalized V3 homepage with consistent Projects navigation, headings, actions, cards, gallery captions and contact text. Corrected the green aerial caption to Project 01. Preserved earlier candidates and versions; remaining V3 screens follow this baseline |
| 23 October 2026 | User clarified the full V3 deliverable after the homepage-only response | Created the complete fourteen-board V3 review pack and interaction handoff, preserving earlier versions/homepage. Added separate detail designs for both projects and expanded gallery/media coverage. No application implementation |
| 23 October 2026 | User requested removal of duplicate page images from the main design folder | Kept fourteen canonical selected images in V3; archived seven drafts and three homepage alternatives; updated links and manifests. Building the Django project is next |

| 23 October 2026 | User authorized implementation with sample media | Built the first local bilingual Django/catalog/staff-editing milestone. Recorded checks and remaining production work in PROGRESS.md; no remote deployment |

| 23 October 2026 | User requested a security/plan audit and private source history | Remediated publication/deletion/media/configuration gaps, added tests/scans, ran PostgreSQL CI, created the private repo/protected main and documented unresolved launch gates in SECURITY_AUDIT.md |

## How to add a decision

Record the date, author/approver, problem, selected behavior, alternatives when relevant, security/privacy effect, affected requirements, and schedule effect. Mark recommendations as proposed until accepted. When scope changes, update the roadmap and progress before implementing the change. Never include confidential data in a decision example.
