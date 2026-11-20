# Progress

Last updated 21 November 2026.

## Current state

The foundation build is complete and checked. It is a working local preview, not something ready to launch. Feature work continues in `rcpdl-website` (D25 in [DECISIONS.md](DECISIONS.md)).

| Area | State |
| --- | --- |
| Public pages (EN/BN) | Built: Home, Projects, both project pages, Gallery with photo viewer, Virtual Site Visit (sample video and 360° view), About, Contact, demo inquiry and receipt, draft Privacy and Terms, 404 |
| Content | Two sample listings and one FAQ from `seed_demo`; every fact and image is labelled as a sample |
| Staff area | Django admin at `/staff/`, password + authenticator code, publish permission, photo upload with approval |
| Inquiries | Demo only: the form validates input but never stores or sends it |
| AI assistant | A dialog that says AI is coming later; no provider connected |
| Deployment | None: no host, domain or production database |

## Done

**Planning and design, 15–23 October**

- Read the supplied feature DOCX (20 feature groups, 15 proposed pages) and both logo files. Gathered 22 answers and 7 follow-ups from Arif and cut the scope down to a small browse-and-inquire MVP.
- Researched the company's public pages, three local property websites, Django and PostgreSQL support windows, and Bangladesh's Personal Data Protection Act 2026.
- Three design rounds: V1 (9 boards), V2 (11 boards plus 8 imagery corrections) and V3 Open Horizon (14 boards). The manager found V1 too wordy; Arif chose Open Horizon. All images are AI-generated.

**Foundation build, 23 October**

- Django 5.2 project with two apps: `projects` (Project, ProjectImage, FAQ) and `website` (pages, inquiry form, bilingual copy).
- Staff MFA (django-two-factor-auth), login lockout (django-axes), publish permission, photo validation and re-encoding.
- Self-hosted fonts and Pannellum viewer, custom CSS, one small `site.js`.
- Hashed dependency locks, a Gitleaks pre-commit hook, GitHub Actions CI with PostgreSQL 17.

**Security audit, 23 October**

- Fixed six findings (A01–A06 in [SECURITY_AUDIT.md](SECURITY_AUDIT.md)), grew the tests from 20 to 34 with real sign-in and configuration tests, created the private GitHub repo with a protected `main`, and merged everything as PR #3.

**Code review and cleanup, 21 November** (Arif asked for a senior-level review)

- Re-indented all 17 page, component and staff templates, so each element is on its own line. Checked the output did not change: the rendered HTML of 34 pages is identical apart from whitespace between tags, and 46 screenshots (desktop and mobile) are pixel-identical.
- Gave the 404 page its own text in both languages ("Page not found"), with buttons to the home page and to projects. It used to say "Project information is being updated." Added a test for it.
- Rewrote every doc as short internal working notes. Removed stale status lines and references to tooling the project never used, and deleted `design/concepts/v3/NEXT_STEPS.md` (its checklist is now in REQUIREMENTS.md).
- Logged the review's open findings as A07–A14 in SECURITY_AUDIT.md.
- Organised the folder: planning docs moved into `docs/`, the supplied originals into `docs/supplied/`, and the sample-media prompts out of the public static folder (fixes A14).

## Latest checks (21 November 2026, local)

| Check | Result |
| --- | --- |
| `ruff check`, `ruff format --check` | Pass |
| `manage.py check`, `makemigrations --check` | Pass, no missing migrations |
| `manage.py test tests` | **35 passed** (SQLite) |
| `scripts/check_production.py` | Pass. W005 and W021 (HSTS subdomains and preload) are shown on purpose |
| Bandit | No findings |
| pip-audit (runtime lock) | No known vulnerabilities |
| Supplied file hashes | All three match the 15 October values |

CI also passed on PostgreSQL 17 for these changes: [PR #5](https://github.com/arifshekhk8/rc-property-website/pull/5), [run](https://github.com/arifshekhk8/rc-property-website/actions/runs/44806183830). Earlier evidence: the [34-test PostgreSQL run](https://github.com/arifshekhk8/rc-property-website/actions/runs/39985417363) on [PR #3](https://github.com/arifshekhk8/rc-property-website/pull/3).

## Open items

From the 21 November review. Details, file references and suggested fixes are in [SECURITY_AUDIT.md](SECURITY_AUDIT.md#open-findings).

1. No logging setup and no `500.html`, so server errors in production would go unrecorded (A07).
2. The HTTPS redirect sends a 301 to `/health/` if a load balancer checks over plain HTTP (A08).
3. Login lockout uses `REMOTE_ADDR`. Behind a proxy, anyone could lock a staff member out for 30 minutes (A09).
4. Phone validation rejects `8801…` and `00880…` numbers (A10).
5. `CSRF_TRUSTED_ORIGINS` doesn't strip spaces (A11).
6. Replaced or deleted photos stay on disk (A12).
7. The caption track is labelled "en"/"bn" instead of a language name (A13).

## Next steps

If work resumes in this repo (otherwise these carry over to `rcpdl-website`):

1. Review and merge [PR #5](https://github.com/arifshekhk8/rc-property-website/pull/5).
2. Fix A07–A09 before any deployment; A10–A13 when convenient.
3. Staff draft/review/publish workflow, editable public contacts, real video and panorama upload.
4. Private inquiry inbox with a consent record, recipient permissions, abuse limits and retention. Use synthetic data until the company answers Q03–Q05.
5. The AI adapter, only after the inquiry boundary exists and the company settles Q06.
6. Replace samples with approved facts and media, get a native Bangla review, then staging, backups, independent review and launch.

## Supplied file hashes

Recorded on 15 October 2026 before any work; rechecked on 21 November 2026 after moving the files to `docs/supplied/`.

| File | SHA-256 |
| --- | --- |
| RCPDL.png | cd207c273fcdcae422cda733b26d8fb898ea11a3e469044a5693bb9e74157755 |
| RCPDL Logo.ai | 241a4c3e524a0e064c30217f18289e60b9d9ecc9488402b5b2a43d432a098b36 |
| Advanced_Real_Estate_Plot_Website_Features.docx | a3fcb98a2ebdb3214323341f1f2b27d58535830a27d7f161c34dce6c143f8d10 |

## Session log

| Date | What happened |
| --- | --- |
| 15 Oct 2026 | Scope analysis, research and the first docs; V1 and V2 designs; V2 imagery corrections |
| 23 Oct 2026 | Manager feedback; three V3 homepage options and Open Horizon chosen; full V3 pack; build approved and foundation built; audit; private repo and CI |
| 7–8 Nov 2026 | Work continued in `rcpdl-website`; v0.2.0 released there |
| 21 Nov 2026 | Code review; templates re-indented; 404 page fixed; docs rewritten |
