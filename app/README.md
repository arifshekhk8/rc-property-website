# RC Property — Local Django Build

Foundation and security audit checkpoint, 23 October 2026. Uses the selected V3 Open Horizon design and two sample records: Project 01 and Project 02.

## Run locally

The existing workspace is ready: run `./scripts/dev.sh` from the root. The virtual environment now uses isolated Python 3.13.16; system Python was not changed.

For a fresh checkout, install Python **3.13.16** first (pinned in `.python-version`), then run from the workspace root:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
./scripts/dev.sh
```

Open [English](http://127.0.0.1:8000/en/) or [Bangla](http://127.0.0.1:8000/bn/). SQLite is used only for local development; it is under the ignored `.runtime/` directory. PostgreSQL is configured through `DATABASE_URL`; production refuses SQLite and requires an explicit secret key. Environment variables are read from the process, not automatically from `.env.example`. Local manage.py commands default to development. The WSGI entry defaults to production and rejects missing/weak secrets, absent/wildcard hosts and PostgreSQL without TLS; deployment commands must explicitly set `DJANGO_DEBUG=0`.

The seed command is idempotent: it creates missing sample projects and leaves existing staff edits untouched. Sample image/video/font/viewer files are included, so running the app does not require external asset services or image generation.

## Staff access

Create your own local staff administrator interactively:

```bash
.venv/bin/python app/manage.py createsuperuser
```

Open [staff sign-in](http://127.0.0.1:8000/account/login/), sign in, and enroll an authenticator. Then open [the staff workspace](http://127.0.0.1:8000/staff/). Password-only sessions cannot access the admin. Keep authenticator/recovery secrets private. No default/shared administrator password has been created.

Daily staff should use individually assigned permissions after company roles are approved. The custom `projects.publish_project` permission controls publication. Until the planned draft-revision workflow is implemented, editors without publishing permission cannot alter or delete already-published project or FAQ records, including through bulk actions. Managers with permissions edit current records directly. The complete V3 review/publish workflow is not yet implemented.

## Implemented

- English/Bangla Home, Projects, both project details, Gallery/lightbox, media views, About, Contact, inquiry preview and draft policy pages.
- Database-backed project facts and availability; positive price/area DB constraints, published-only public queries and media authorization.
- Uploaded photos appear publicly only when both rights and publication approval are confirmed; unapproved captions/files remain private.
- Staff project/FAQ editing, image uploads, MFA enrollment/verification and password-login throttling.
- Validated/re-encoded photo uploads, generated filenames and removal of source image metadata.
- A self-hosted Pannellum viewer loaded only after selection, explicit video playback and captioned sample clips.
- Demo inquiry validation with an initially unchecked permission field. **No inquiry contact fields are stored or sent in this milestone.**
- A clearly identified guide placeholder. **No external AI provider is connected yet.**
- Hashed dependency locks, staged/history secret scans, synthetic production checks and an executed PostgreSQL CI workflow on the private GitHub repo.

## Temporary content

All property data/media are samples. Actual photos, video and panoramas will be supplied later. The video is an eight-second animated still, not a recorded walkthrough. The generic generated panorama demonstrates the viewer and does not depict either real listing. Business contacts and final legal text remain pending; there are no invented business phone numbers or active map destinations.

Ordinary photos can be added through staff project editing; bilingual captions and alternative text are required. Confirm usage rights and explicitly approve publication to display a photo. Only permitted publishers can set approval, and only MFA-verified permitted staff can preview unapproved files. A fallback illustration remains labeled as a sample. Dedicated upload/replacement for real video and panorama, complete review/draft revisions, public-contact settings, the private inquiry inbox and the AI adapter are upcoming milestones. Do not remove sample labels before approved facts/media are in place.

The interface uses custom CSS rather than the proposed Bootstrap layer to match V3 without unnecessary framework defaults. English/Bangla copy needs native review; raster mockups and this build do not establish accessibility conformance.

## Repository and commits

Private source: [arifshekhk8/rc-property-website](https://github.com/arifshekhk8/rc-property-website). Company ownership and approved maintainers are pending. Main requires a pull request plus passing `django` and `secrets` checks even for administrators; force-pushes/deletion are disabled. No independent approver is assigned yet, so peer-review requirements must be completed before production release.

Install the checksum-pinned secret scanner and enable the local hook on a fresh checkout:

```bash
./scripts/install-gitleaks.sh
git config core.hooksPath .githooks
```

Commit focused changes. The hook fails closed if the scanner is missing and scans staged content with redacted output. GitHub also scans full history. Do not bypass these checks to commit a real credential; rotate a credential if exposed. Do not commit local databases, customer data, upload directories, MFA secrets or environment files.

Only selected V3 boards/handoff notes are tracked. Old design archives and supplied DOCX/Illustrator references remain local and preserved; links to those local archives are not available in a fresh source-only clone.

## Checks

```bash
.venv/bin/python app/manage.py check
.venv/bin/python app/manage.py makemigrations --check --dry-run
.venv/bin/python app/manage.py collectstatic --noinput --verbosity 0
.venv/bin/python app/manage.py test tests
.venv/bin/ruff check app scripts
.venv/bin/bandit -r app scripts -x app/tests,app/projects/migrations -q
.venv/bin/python scripts/check_production.py
.runtime/tools/gitleaks git --redact --no-banner --log-opts=--all
.venv/bin/pip-audit -r requirements.lock --disable-pip --no-deps --progress-spinner off
```

Tests cover bilingual routes, unpublished-record/media isolation, escaping, consent/phone validation, non-persistence of demo inquiry fields, CSRF, MFA gate/revocation, authorized editing and image normalization. Local tests use SQLite. PostgreSQL 17 CI now executes remotely. The audit records exact runs/counts; current PR checks are the source of truth for that commit. There are 34 current integration tests, including real password/TOTP sign-in, invalid OTP rejection, password lockout, logout, direct/bulk deletion permissions, unapproved-media access and production configuration boundaries. Production readiness, browser/device coverage and full role workflows still require later integration checks. Synthetic production checks leave `security.W005`/`security.W021` visible until company subdomains/TLS and HSTS preload decisions are known; no deployed-system check is implied.

## Assets and references

- Official logo source: supplied `RCPDL.png`; web export preserves the original asset.
- Sample project photographs: generated illustrations from the preserved V2 source assets, optimized as new WebP copies.
- Hero and panorama: built-in image generation; [exact prompts](static/images/GENERATION_PROMPTS.md).
- Video: FFmpeg animation of each sample project still, with explicit sample labels and captions.
- Pannellum 2.5.7 and Noto fonts are self-hosted; package provenance/integrity is recorded in [the vendor manifest](static/vendor/MANIFEST.json). Licenses accompany the files.
- [Django 5.2 installation compatibility](https://docs.djangoproject.com/en/5.2/faq/install/) and [staff MFA installation guidance](https://django-two-factor-auth.readthedocs.io/en/stable/installation.html).

No live hosting, production database, company domain/DNS or paid AI provider is configured. The private GitHub remote is configured; the company-owned organization remains pending. Follow the root PLAN.md and SECURITY.md before those steps.

See [the foundation audit](../SECURITY_AUDIT.md) for fixed findings, plan coverage, verification evidence and remaining launch gates.
