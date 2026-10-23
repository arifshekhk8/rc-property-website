# Project Progress

Last updated: 23 October 2026, Asia/Dhaka.

## Current phase

Phase 1 is underway. The user authorized building from V3 using sample photos, videos and 360° imagery. The first local Django milestone now runs at [English](http://127.0.0.1:8000/en/) / [Bangla](http://127.0.0.1:8000/bn/): public pages, two database-backed sample projects, Gallery/lightbox, sample video/panorama and staff project/FAQ editing with MFA. See [app/README.md](app/README.md) for setup, staff enrollment and limitations.

Live inquiry persistence, the private inbox, free-text AI, full draft/review publishing, editable business contacts, dedicated real video/panorama management and production infrastructure are unfinished. No company-owned GitHub remote or deployment exists. The V3 design boards and supplied originals are unchanged.

## Audit and repository checkpoint — 23 October

User requested a plan/security audit, document updates and a private repository with focused commits. [SECURITY_AUDIT.md](SECURITY_AUDIT.md) maps requirements, fixed findings, evidence and remaining launch gates.

- Created [arifshekhk8/rc-property-website](https://github.com/arifshekhk8/rc-property-website) as private. Main requires pull requests and successful django/secrets checks even for admins; force-pushes and deletion are blocked. Company ownership/maintainers and independent approving review remain pending; no collaborator was added.
- Added staged/full-history Gitleaks scans, checksum-pinned scanner installation, read-only CI permissions, pinned trusted actions, weekly checks and action-update proposals. Runtime secrets, local DB/uploads and original private-reference files are excluded from Git.
- Fixed live-record direct/bulk deletion authorization, added explicit photo rights/publication approval and protected previews, added DB constraints, hardened production defaults/TLS/hosts/secrets, and extended CSP/no-store/sensitive-field protections. Regression tests accompany the changes.
- Upgraded the local isolated runtime from Python 3.13.5 to 3.13.16, matching the verified CI interpreter; system Python was preserved. Expanded CSS/JS sources for easier review.
- **34 local tests passed on Python 3.13.16** (final runtime check: 6.932 s). Ruff, Bandit, pip-audit and full-history Gitleaks passed. The initial [PostgreSQL CI run](https://github.com/arifshekhk8/rc-property-website/actions/runs/39983848657) passed 31 tests; the expanded **34-test PostgreSQL run** also [passed](https://github.com/arifshekhk8/rc-property-website/actions/runs/39985417363), including the full authentication tests on [audit PR #3](https://github.com/arifshekhk8/rc-property-website/pull/3).
- Synthetic production checks reject unexpected warnings/errors. W005/W021 remain visible domain/TLS decisions for subdomain HSTS/preload; there is no production deployment or independent-review certification.

## First implementation milestone — 23 October (historical checkpoint)

The evidence below records the initial build before the audit above; the audit supersedes its pending-remote/PostgreSQL status.

- Created the local Git repository, Python 3.13 virtual environment, hashed dependency locks, development runner and Django 5.2.18 application/migrations. Local SQLite is an explicitly documented development exception; production requires PostgreSQL and an explicit secret. PostgreSQL 17 CI is prepared but has not executed remotely.
- Implemented V3 English/Bangla Home, Projects, separate detail records, Gallery/lightbox, media page, About, Contact, demo inquiry/receipt and draft policies using custom CSS, self-hosted fonts and the supplied logo export.
- Added Project, ProjectImage and FAQ models/admin, published-only public queries, an explicit publication permission and protected media delivery. Non-publishers cannot change already-published records until draft revisions are available. Verified permitted staff edits appear on both language pages.
- Added staff MFA/authenticator enrollment, login throttling, CSRF, escaping and a strict public-page script policy. Staff/account responses are private/no-store. No shared staff account/password has been created; local enrollment instructions are in app/README.md.
- Added photo validation/re-encoding/metadata removal and sample-safe seeding that preserves existing edits. Optimized new copies of V2 illustrations; generated a new hero and generic panorama; created captioned eight-second animated sample clips. Exact image prompts and vendor provenance/licenses are included.
- Demo inquiry validates phone/project/unchecked consent but never stores, sends or echoes contact fields. The guide dialog clearly states that live AI is pending. No company contact, map destination or legal text was invented as approved content.

### Verification on 23 October

| Check | Result and limits |
| --- | --- |
| `manage.py check` / `makemigrations --check --dry-run` | Passed; no system issues or migration drift |
| `manage.py collectstatic --noinput --verbosity 0` | Passed; manifest and self-hosted assets generated |
| `manage.py test tests --verbosity 1` | 20 tests passed on local SQLite (final run 0.341 s) |
| Ruff / Bandit | Passed, no findings in their configured source scope |
| `pip-audit -r requirements.lock --disable-pip --no-deps --progress-spinner off` | No known runtime dependency vulnerabilities reported; point-in-time result, not a full security audit |
| Chrome UI review | Desktop English homepage, Bangla detail, 390 × 844 emulated English/Bangla layouts, guide dialog, gallery with keyboard next/Escape, video playback/captions, panorama rendering and staff login reviewed |
| Browser defect corrected | Removed the static poster before initializing Pannellum; confirmed that the actual panorama canvas and viewer controls render afterward |
| Preservation hashes | 48 supplied/V1/V2 files and all 14 selected V3 boards match their existing SHA-256 baselines |

The tests exercise unpublished/archived URL and media isolation, bilingual routes/facts, language context, escaping, consent/phone validation, no demo inquiry writes, CSRF, MFA gates/revocation, authorized editing and image normalization/rejection. Browser review is a limited smoke check; no native-phone, full accessibility, performance, production or PostgreSQL certification is claimed. Browser extension wallet errors appeared in the existing Chrome profile; no site policy was weakened for them.

## Completed work

- Inspected the three supplied files: PNG logo, PDF-compatible Illustrator logo, and feature DOCX.
- Read the complete feature document and its structure: 20 feature groups and 15 proposed pages.
- Inspected both logo versions; identified the wide layout and transparency; sampled colors and calculated contrast.
- Gathered the initial 22 answers and seven focused follow-ups.
- Confirmed two individual plots, Bangla/English mobile use, public BDT prices, katha/square feet, staff administration, provided media, and a free-text AI assistant.
- Confirmed minimal consent-based lead details and exclusions for customer login, appointments, bookings, payments, and customer uploads.
- Researched the group and sister concern using company-controlled public pages; checked suitable local property website references.
- Verified relevant Django/Python/PostgreSQL compatibility/support, Bootstrap accessibility caveats, panorama configuration, AI data controls, security tools, and current Bangladesh law sources.
- Created README.md, REQUIREMENTS.md, DESIGN.md, TECH_STACK.md, SECURITY.md, PLAN.md, PROGRESS.md, and DECISIONS.md.
- Suggested optional Codex Security; it is not confirmed installed or connected. No integration is required to review this documentation.
- Created and visually inspected nine selected UI/UX boards using the built-in image-generation tool, with desktop/mobile public examples, Bangla listing/chat, AI disclosure and separate consent form, and essential staff workflows.
- Refined mobile numeric presentation, the selected panorama media state, and the AI flow's close control/professional presentation. Kept earlier drafts without overwriting them.
- Saved all selected images, three superseded drafts, the review index, and twelve generation/refinement prompts under design/concepts/v1/.
- Created design/concepts/v2/ and retained the chosen plot-imagery reference there.
- Generated and visually inspected eleven new V2 boards: all principal public/staff workflows, dedicated Bangla mobile examples, and feedback/recovery states.
- Improved hero text/image separation, landscape plot presentation, price/area hierarchy, staff navigation, and policy navigation state.
- Added visible validation/focus, submission loading, AI-outage fallback and staff access-restricted examples; remaining states are listed in the handoff notes.
- Saved the V2 review index, design/handoff notes, eleven full generation prompts, and the pre-change V1 integrity manifest. Recorded minor generated-text/style normalizations without modifying either design version.
- Updated the maintained project overview, design direction, roadmap, decisions and progress to point to V2. Scope and implementation authorization remain unchanged.
- Corrected the rejected image repetition in eight sibling boards under design/concepts/v2/imagery-revision/: distinct landscape hero, green Plot01 and sandy Plot02, alternate gallery/media views, planning-workspace About image, and removal of decorative photos from disclosure/receipt/feedback screens.
- Saved three independent source illustrations, the correction review notes and twelve source/edit/refinement prompts. Refined the Bangla board again after detecting a hero-mapping and sample-value error. Updated the review index to select corrected files without overwriting earlier PNGs.
- Read the original feature DOCX again for the V3 brief. Added the requested Gallery section and selected Virtual Site Visit from feature 8 for the homepage candidates; this promotes existing media requirements without introducing bookings or additional transactional scope.
- Created and visually inspected three desktop homepage candidates with the built-in image-generation tool. All use large illustrative land images, short headings, compact facts for exactly two plots, Gallery, Virtual Site Visit and concise contact actions. Saved the PNGs, exact prompts, review index and preservation baseline under design/concepts/v3/homepage-options/.
- Recorded the manager's feedback and the user's selection-before-full-V3 workflow in the maintained planning documents; A was subsequently selected as recorded below.
- Finalized the selected A / Open Horizon homepage for now using a targeted built-in image-generation edit. Renamed the two public listings Project 01 and Project 02 and updated navigation, section heading, actions, gallery captions and contact text consistently. Corrected the green aerial gallery caption to Project 01. Saved design/concepts/v3/01-home-final.png, the selection index and exact edit prompt without overwriting earlier candidates.
- Recorded that the public naming change does not establish a project/subplot hierarchy. The homepage decision is resolved; the later full-pack work below completes the remaining page designs for review.
- Completed the requested V3 folder, comparable to V1/V2, with thirteen new page/workflow boards plus the unchanged approved homepage: Projects; separate Project 01/02 details; Gallery/lightbox; video/panorama; AI/disclosure/inquiry/receipt; About/Contact; Privacy/Terms; staff content; staff sign-in/MFA/inbox/detail; staff FAQs/contacts; English/Bangla mobile; feedback/recovery.
- Visually inspected the generated boards and refined seven where needed for property-image identity, purpose-specific consent, draft-policy purpose/media wording, staff header consistency, synthetic inquiry copy and sending/success separation. Preserved the earlier drafts and exact generation/refinement prompts.
- Added the V3 review index and DESIGN_NOTES.md covering visual tokens, responsive/language rules, media interactions, AI/inquiry boundaries, staff draft/publishing states and recovery behavior. Updated the maintained project documents and next actions. This completes page-design coverage for review, not application implementation or approval of every new board.
- Cleaned the V3 folder at the user's request: retained fourteen selected images with canonical numbered names, moved seven superseded boards and three homepage alternatives into archive/, and updated review links/selection metadata. All PNG contents remain unchanged. The user intends to start building the project next; no application code was created during this cleanup.

## Evidence and verification limits

Company sources call the sister concern RC Property Development Ltd. The exact project legal name remains unresolved. Public pages list a Gulshan-1 corporate office; company approval is required before publishing contacts/address.

The group property page mentions RC Maya Kanon and RC Rivery Village, but the user confirmed two individual plots. Those project names have not been assumed to identify the launch listings. A company privacy policy could not be verified from inspected pages; that does not prove none exists.

Design references were reviewed for public content and information hierarchy. Their full rendered mobile appearance, accessibility, security, and performance were not audited. Existing walkthrough/panorama/photo assets were reported by the user but have not yet been delivered or inspected in this folder.

The official 2026 privacy Act was located, and its commencement page inspected. Complete provision-to-feature mapping and any later rules/notifications remain a company legal-review task. No legal-compliance certification is claimed.

The following design-stage evidence records earlier work. Application evidence for the new implementation is recorded above; earlier statements that no application tests ran refer to those design-only tasks.

Documentation verification on 15 October: all eight files exist and have titles, dates, and terminal newlines; local Markdown links resolve; no repeated section headings were found; the three supplied files match their original SHA-256 values. Scope consistency was reviewed across the documents, including the user's AI choice, two individual plots, permitted lead fields, and excluded transactional features. The Mermaid architecture diagram is a documentation source; its rendered appearance has not been separately checked.

Visual review checked page coverage, the two-listing scope, sample labeling, mobile reading order, consent separation, masked lead data, and the exclusion of customer accounts/transactional features. The images are static raster proposals: exact font metrics, programmatic contrast/focus, complete translation variants, keyboard behavior, security controls, and interactions have not been tested. Use the review pack's normalization and remaining-state notes during the next design revision.

Design-pack file verification passed: nine selected PNGs have valid signatures/dimensions, all local links in the planning/review/prompt documents resolve, and original source hashes remain unchanged. No application tests were run or claimed.

V2 verification on 15 October: all eleven board PNGs have valid signatures and dimensions (1536 × 1024 or wider board variants); all local links across thirteen Markdown files resolve. SHA-256 comparison confirms that all fourteen V1 files, including its documentation and earlier drafts, match the baseline captured before this task. The three original supplied files also match their recorded hashes. See design/concepts/v2/V1-INTEGRITY.sha256 for the preserved baseline. All boards are raster proposals; application tests/security scans and interactive accessibility/performance checks do not apply yet.

V2 imagery is AI-generated and clearly labeled. It is not verified recent photography of Purbachal or the launch plots. V2 has not received final visual approval. Its handoff notes record remaining responsive/translation/state specifications and small consistency corrections, including final logo exports and the publication-versus-availability distinction. The corrected receipt now labels the submitted visitor number separately from the pending business contact.

Imagery-correction verification: eight corrected board PNGs and three distinct source PNGs have valid signatures/dimensions; all local links across fifteen Markdown files resolve. All fourteen V1 files and three supplied originals still match their integrity baselines. Visual review checked image assignments, property distinction, alternate viewpoints, captions and the corrected Bangla sample price/area. These remain generated raster concepts; no interactive, security or accessibility tests were run or claimed.

Homepage-option verification on 23 October: all three PNGs have valid signatures and dimensions of 1024 × 1536. All 48 V1/V2/original files match the pre-change preservation baseline, and local links across 17 Markdown documents resolve. Visual review confirmed the principal layout/content requirements; the review index records minor generated-logo and illustrative gallery-mapping/viewpoint normalizations for the selected V3. These are desktop raster candidates, with no responsive, interactive accessibility, application or security tests claimed.

## Supplied file integrity baseline

Full-V3 verification on 23 October: fourteen selected boards exist and have valid PNG signatures/dimensions (twelve 1536 × 1024 boards, one 1774 × 887 AI/inquiry board and the preserved 1024 × 1536 homepage). All boards and seven refinements were visually inspected; the selected index points to refined versions where applicable. All 56 files in the pre-work preservation manifest match their hashes, including V1, V2, original sources, homepage candidates and the approved V3 homepage. All local links across 24 Markdown documents resolve. SELECTED_BOARDS.json and VERIFICATION.json record the file evidence. No application tests or interactive accessibility/security/performance verification were run or claimed.

Selected-homepage verification on 23 October: the final PNG is valid at 1024 × 1536. Visual inspection confirmed Project 01 / Project 02 naming, Projects navigation, project actions/captions/contact text, both unchanged sample price/area pairs and the corrected aerial caption. All 48 V1/V2/original files match their baseline and local links across 19 Markdown documents resolve. No application tests were run for this raster/design-documentation change.

Original SHA-256 values recorded before creating documentation:

| File | SHA-256 |
| --- | --- |
| RCPDL.png | cd207c273fcdcae422cda733b26d8fb898ea11a3e469044a5693bb9e74157755 |
| RCPDL Logo.ai | 241a4c3e524a0e064c30217f18289e60b9d9ecc9488402b5b2a43d432a098b36 |
| Advanced_Real_Estate_Plot_Website_Features.docx | a3fcb98a2ebdb3214323341f1f2b27d58535830a27d7f161c34dce6c143f8d10 |

## Next actions

Latest user direction: implementation is authorized using V3 and temporary sample media. The first working build is available for review; actual project media will be provided later.

1. Next coding milestone: complete staff draft/review/publish controls and media/contact editing, then the restricted consent-based inquiry inbox with role/abuse/retention tests.
2. Confirm company recipients, notice/retention, approved contacts and staff responsibilities before collecting real leads. Continue implementation/testing with synthetic records meanwhile.
3. Maintain PostgreSQL CI and settle company ownership/independent reviewers, then implement the free-text bilingual AI adapter and factual/privacy evaluations once provider arrangements are settled.
4. Gather approved facts/media for both projects, review Bangla copy/mobile behavior with the manager, and complete staging, backup/recovery and production checks before release. Reassess the original dates as these inputs arrive.

## Session log

| Date | Result | Resume point |
| --- | --- | --- |
| 15 October 2026 | Source analysis, company/reference/security research, confirmed MVP, proposed architecture, and initial documentation | Review documents and resolve company decisions; implementation not started |
| 15 October 2026 | First UI/UX concept: nine selected boards, three retained earlier drafts, review index, and prompt archive | Review visual direction and refine states; no coding |
| 15 October 2026 | Separate V2: eleven boards, plot-focused AI illustrations, public/staff improvements, Bangla mobile and recovery states; V1 and all originals verified unchanged | Review V2 and remaining handoff details; no coding |
| 15 October 2026 | User rejected repetitive V2 imagery; corrected eight boards, generated three distinct source illustrations, removed filler photos, and updated selected review links | Review the imagery-corrected V2; preserve V1 and defer coding |
| 23 October 2026 | Manager feedback favors V1 with much less text; created three modern homepage candidates with Gallery and Virtual Site Visit, using the original feature document | User selects a homepage direction; create full V3 afterward; no application code |
| 23 October 2026 | User selected A / Open Horizon as final for now; saved the finalized homepage with Project 01 / Project 02 naming and corrected aerial caption | Homepage choice resolved; extend remaining V3 design from this baseline; no application implementation |
| 23 October 2026 | User clarified the full V3 deliverable; completed fourteen selected boards, seven refinements and responsive/interaction handoff while preserving earlier versions/homepage | Review complete V3 with manager, obtain company content/operating inputs, then begin Django foundation when instructed |
| 23 October 2026 | Cleaned V3 to fourteen canonical selected images; archived earlier alternatives/drafts and updated references | Next task: start the Django project foundation using V3 |
| 23 October 2026 | User authorized building with sample media; completed the first local Django/catalog/staff-editing milestone, 20 tests and local checks | Review the running bilingual build; next complete staff publishing/media/contact controls and the private inquiry flow, then AI and staging |
| 23 October 2026 | Audited foundation, fixed security gaps, added real authentication tests, created/pushed private repo with protected main and executed PostgreSQL CI | Continue staff publishing/media/contact and restricted inquiry milestones; company approvals and production checks remain launch gates |
