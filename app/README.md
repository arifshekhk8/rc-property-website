# App: developer guide

Last updated 21 November 2026. This is the Django project for the RC Property site. For the overview and status, see the [root README](../README.md).

## Run locally

You need Python 3.13.16 (see `.python-version`). From the repo root:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
./scripts/dev.sh
```

`dev.sh` runs migrations and `seed_demo`, then serves on http://127.0.0.1:8000 (set `RCP_PORT` to use another port). Open `/en/` or `/bn/`.

- `manage.py` defaults to development (`DJANGO_DEBUG=1`). It uses SQLite at `.runtime/development.sqlite3` and a generated secret key in `.runtime/dev-secret`.
- `wsgi.py` defaults to production. It won't start without a strong `DJANGO_SECRET_KEY`, explicit `DJANGO_ALLOWED_HOSTS`, and a PostgreSQL `DATABASE_URL` using TLS. Production management commands need `DJANGO_DEBUG=0` set explicitly.
- Settings are read from environment variables in the shell. `.env.example` documents them but isn't loaded automatically.
- `seed_demo` only creates sample records that are missing; it never overwrites staff edits.

## Staff access

```bash
.venv/bin/python app/manage.py createsuperuser
```

Sign in at http://127.0.0.1:8000/account/login/, set up an authenticator app, then open http://127.0.0.1:8000/staff/. A password alone never opens the admin. There is no default or shared account.

Permissions:

- `projects.publish_project` lets a user publish projects and FAQs, approve photos, and change or delete live records.
- Without it, staff can edit drafts but can't change or delete published records, even with delete permission or through bulk actions.
- Unapproved photos are visible only to MFA-verified staff with `view_projectimage`.

Once the company confirms roles, use non-superuser accounts with assigned permissions for daily work.

## Checks

These are the same checks CI runs (`.github/workflows/checks.yml`):

```bash
.venv/bin/ruff check app scripts
.venv/bin/ruff format --check app scripts
.venv/bin/python app/manage.py check
.venv/bin/python app/manage.py makemigrations --check --dry-run
.venv/bin/python app/manage.py collectstatic --noinput --verbosity 0
.venv/bin/python app/manage.py test tests
.venv/bin/python scripts/check_production.py
.venv/bin/bandit -r app scripts -x app/tests,app/projects/migrations -q
.venv/bin/pip-audit -r requirements.lock --disable-pip --no-deps --progress-spinner off
.runtime/tools/gitleaks git --redact --no-banner --log-opts=--all
```

There are 35 tests. They cover:

- every public page in both languages, plus the 404 page
- hiding unpublished and archived records
- escaping of staff content
- the inquiry form: consent, phone validation, nothing stored
- CSRF and security headers
- the MFA gate and device revocation; real password + TOTP sign-in, lockout and logout
- publish and delete permissions
- photo validation and privacy
- production settings

Local runs use SQLite; CI uses PostgreSQL 17.

`check_production.py` shows `security.W005` and `security.W021` (HSTS on subdomains, and preload) on purpose until the real domain is known. Any other warning makes it fail.

## Secret scanning on a fresh clone

```bash
./scripts/install-gitleaks.sh
git config core.hooksPath .githooks
```

The pre-commit hook refuses to commit if Gitleaks is missing. Never bypass it for a real credential; if one leaks, rotate it. Don't commit databases, uploads, MFA secrets, `.env` files or customer data.

## Sample content and assets

Every listing fact and image is a sample, and labelled as one. Keep the sample labels until the company approves the real facts and media.

| Asset | Source |
| --- | --- |
| Logo (`logo.webp`, `favicon.png`) | Exported from the supplied `docs/supplied/RCPDL.png` |
| Project photos (`project-01.webp`, `project-02.webp`) | AI-generated illustrations from the V2 design work |
| Hero and panorama | AI-generated; prompts in [SAMPLE_MEDIA_PROMPTS.md](../docs/SAMPLE_MEDIA_PROMPTS.md) |
| Sample videos | 8-second FFmpeg animations of each project's still image, with English and Bangla captions |
| Noto fonts, Pannellum 2.5.7 | Self-hosted with licences; sources and checksums in [MANIFEST.json](static/vendor/MANIFEST.json) |

Staff can add photos to a project, with captions and alt text in both languages. A photo appears publicly only when its rights are confirmed and a publisher approves it. Real video and panorama upload, contact editing, the inquiry inbox and the AI adapter aren't built yet.

Contacts, legal text and the map link are placeholders. No phone number, address or map destination has been made up.
