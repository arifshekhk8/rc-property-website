# Development Roadmap

Last updated: 23 October 2026, Asia/Dhaka. Status: first local Django/catalog/staff-editing milestone complete; remaining foundation and production milestones in progress.

The user selected **A / Open Horizon as final for now** and clarified that V3 must be a complete folder like V1/V2. The [complete V3 design pack](design/concepts/v3/README.md) contains fourteen selected boards for every agreed public page type, gallery/media views, AI/inquiry, staff administration, mobile/Bangla and recovery patterns. The homepage and earlier versions remain preserved. The user has now authorized implementation with temporary sample media. A local bilingual Django build follows this direction; manager feedback and company content/operating decisions can continue alongside implementation.

The user requested approximately one to one-and-a-half months from 15 October. The working plan uses six weeks, targeting 26 November 2026 within an approximate 15–30 November launch window. Dates are planning targets and depend on company responses, usable media, user authorization to implement, and passing release checks.

Schedule checkpoint, 23 October: Phase 1 has begun, including a working catalog/staff-editing slice and sample public/media pages. A local Git repository, locked dependencies and checks exist. A private remote under the user account and executed PostgreSQL CI now exist. Company ownership, approved roles/recovery, independent review and remaining production features are unfinished. The dates below remain the original baseline and require reassessment as company inputs arrive.

## Milestones

| Phase | Target dates | Work and review outcome |
| --- | --- | --- |
| 0. Scope and design | 15–21 October | Resolve key decisions, inspect supplied media, approve facts/branding, review mobile wireframes and visual direction |
| 1. Foundation | 22–28 October | Establish private repository and environments; Django/PostgreSQL; pinned dependencies; CI; authentication/MFA and staff permission foundation |
| 2. Catalog and content | 29 October–4 November | Bilingual pages, two listings, public prices/units, gallery, location, focused administration, publishing controls |
| 3. Media and communication | 5–11 November | Video and panorama; secure interest form/inbox; AI provider adapter, published facts, disclosure, quotas, and fallback |
| 4. Verification and refinement | 12–18 November | User testing, translations, AI evaluations, authorization/privacy tests, scans, mobile accessibility/performance improvements |
| 5. Deployment and handover | 19–26 November | Staging approval, production configuration, restore/rollback demonstration, controlled release, teammate training and operating documentation |

Security reviews happen in every phase. Phase 4 is final integration verification, not the first security work.

## Phase 0 sequence

1. Review the eight documents with the user and company decision-makers.
2. Confirm the legal brand name, domain/host inventory, staff responsibilities, public contacts, and operating budgets.
3. Resolve privacy ownership, retention, AI processing/transfer assessment, and company policy.
4. Obtain the two listings' accurate prices, measurement convention, status, location, rights, photographs, videos, and panorama format.
5. Review mobile wireframes for Home, listing/detail, chat/interest, and staff content workflow; compare the DESIGN.md references.
6. Present a visual direction with readable Bangla/English typography, component states, and approved brand usage before implementation.

No existing domain, host, repository, or supplied asset is changed in this phase. Recommendations can be refined without implementation.

## Implementation order after authorization

Start with a thin functional path: one published listing rendered in both languages and editable by a permitted staff account. Confirm publishing restrictions before expanding pages. Set up checks and environment separation from the first code change.

Then complete both listings and page navigation. Add optimized photos and factual/location content before large media. Configure and test video/panorama accessibility and security separately. Build minimal, consent-based inquiry submission and the restricted inbox before connecting AI; this proves the private data boundary independently.

Integrate the AI through the provider adapter with only approved public facts. Test it using synthetic conversations before company-approved production credentials/data. Verify that lead-form information never enters its payload and that quotas, outages, and untrusted output fail safely.

Deploy first to owned staging using synthetic leads. Verify production-like settings, headers, storage access, translated privacy text, backups, and operational alerts. Prepare a specific domain/DNS migration and rollback plan only when hosting information is available.

## Audit checkpoint

The original foundation sequence is now backed by a private repository, executed PostgreSQL checks and focused security remediation; details are in [SECURITY_AUDIT.md](SECURITY_AUDIT.md). This is a development checkpoint. Do not mark the launch roadmap complete on the basis of scanner/test success. Main has automated gates; independent human review remains an explicit requirement before production release.

## Next implementation milestone

1. Add staff draft revisions, preview/review/publish transitions and focused role tests. Add editable public contacts and dedicated media replacement controls.
2. Build the consent-based private inquiry inbox with recipient permissions, duplicate/abuse controls, approved notice/retention configuration and deletion. Continue using synthetic test data while company decisions are pending.
3. Maintain the passing PostgreSQL checks and private remote, settle company ownership/reviewers, then add the AI adapter and factual evaluations after provider arrangements are settled.
4. Replace samples with approved facts/media, review Bangla copy and mobile accessibility, and complete staging/release checks before production deployment.

## Definition of done for every feature

The behavior matches REQUIREMENTS.md; code is understandable and reviewed; appropriate tests/checks pass; role and public-data boundaries hold; data collected is necessary and documented; both languages and mobile/keyboard behavior work; performance stays within measured budgets; new dependencies are justified; discovered risks are resolved or documented with an owner; and documentation records the result.

Tests must exercise real risks, especially permission bypass, private-data exposure, consent, upload boundaries, unsafe model output, and abuse limits. Avoid duplicating trivial implementation details in tests. Do not mark a feature complete based only on a screenshot or a clean scanner output.

## Handover and recurring work

Train the teammate to update both language versions, change prices/status, replace media safely, review inquiries, manage access, and request support. Document deployment, migrations, secret rotation, backup restore, deletion, provider quotas, and rollback when these systems exist.

Recommend recurring dependency/secret/security checks, prompt/model evaluation after changes, and periodic restoration/access reviews. The company must name the person responsible for patches, incidents, backups, privacy requests, and billing.

## Scope changes

For a requested change, record the trigger and intended outcome in DECISIONS.md, assess security/privacy/accessibility/time impact, and update affected documents. Reuse the current modules when appropriate. Reconsider added search, CMS, queues, or project hierarchy only when actual volume or workflow justifies them. Keep excluded features out of the launch schedule unless the user intentionally changes its priorities.
