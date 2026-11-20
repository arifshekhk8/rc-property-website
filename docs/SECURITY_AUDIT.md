# Security audit

Last updated 21 November 2026. These are self-reviews of the development code. They are not penetration tests or certifications, and nothing has been deployed.

## 23 October 2026: foundation audit

We checked the first build against the plan and [SECURITY.md](SECURITY.md) and fixed these:

| ID | Severity and problem | Fix |
| --- | --- | --- |
| A01 | Medium: an editor with delete permission could delete live content without publish permission | Single and bulk delete of live projects and FAQs now need publish permission. Tested both refusals, and that deleting a draft still works |
| A02 | Medium: a photo on a published project could go public without explicit approval | Needs both rights confirmed and publication approval. Public pages, cover choice and the file URL all agree. Only MFA-verified staff can preview unapproved photos, with `no-store` |
| A03 | High if deployed without config: settings defaulted to development mode | `wsgi.py` now defaults to production and refuses a missing or weak secret, missing or wildcard hosts, SQLite, and PostgreSQL without TLS. `manage.py` defaults to development. Tested in subprocesses |
| A04 | Medium: staff and account pages had no CSP; inquiry responses could be cached | CSP on every route. `no-store` on contact, inquiry and every POST response. Inquiry fields hidden from error reports |
| A05 | Medium: secret scanning and PostgreSQL CI had never run | Gitleaks on every commit and over full history in CI. CI runs hash-locked installs, Ruff, Bandit, pip-audit, PostgreSQL tests and the production-settings check |
| A06 | Low: positive price and area were enforced only in forms | Database check constraints added; tested |

Evidence: 34 tests passed locally and on [PostgreSQL 17 in CI](https://github.com/arifshekhk8/rc-property-website/actions/runs/39985417363) ([PR #3](https://github.com/arifshekhk8/rc-property-website/pull/3)). The earlier [31-test CI run](https://github.com/arifshekhk8/rc-property-website/actions/runs/39983848657) also passed. Ruff, Bandit, pip-audit and full-history Gitleaks were clean.

## 21 November 2026: code review

Arif asked for a senior-level review of everything in the repo: Python, templates, JavaScript, CSS, tests, CI and scripts. We re-ran every CI check locally, and all passed (results in [PROGRESS.md](PROGRESS.md#latest-checks-21-november-2026-local)). No high-severity problems were found.

Changes made in this pass were not security-related: templates re-indented with no output change, and the 404 page given its own text.

### Open findings

| ID | Severity | Problem | Where | Suggested fix |
| --- | --- | --- | --- | --- |
| A07 | Medium, before deploying | No `LOGGING` setup and no `500.html`. With DEBUG off and no `ADMINS`, Django records unhandled errors nowhere | `app/config/settings.py` | Log `django` and `django.request` to the console; add a simple bilingual `500.html` |
| A08 | Low, before deploying | `SECURE_SSL_REDIRECT` sends a 301 to `/health/` when a load balancer checks over plain HTTP | `app/config/settings.py:164` | `SECURE_REDIRECT_EXEMPT = [r"^health/$"]` |
| A09 | Medium, before deploying | Lockout is keyed on username + `REMOTE_ADDR`. Behind a reverse proxy every visitor shares the proxy's IP, so five wrong passwords for a staff username lock the real person out for 30 minutes | `app/config/middleware.py:1-3`, `app/config/settings.py:135-136` | Read the client IP from the trusted proxy's forwarded header only when the app is behind our proxy |
| A10 | Low | Phone validation rejects `8801XXXXXXXXX` and `00880…`, both common ways to type a Bangladeshi number | `app/website/forms.py:41` | Also accept a leading `880` or `00880` |
| A11 | Low | `CSRF_TRUSTED_ORIGINS` entries aren't trimmed, so `a.com, b.com` silently breaks the second origin | `app/config/settings.py:38` | `strip()` each entry, as `ALLOWED_HOSTS` does |
| A12 | Low | Replacing or deleting a `ProjectImage` leaves the old file on disk | `app/projects/models.py` | Delete the old file on replace and delete |
| A13 | Nit (accessibility) | The video caption track is labelled "en"/"bn" | `app/templates/website/visit.html` | Use "English" and "বাংলা" |
| A14 | Nit | `GENERATION_PROMPTS.md` is in `app/static/images/`, so `collectstatic` would publish it | `app/static/images/` | Move it outside `static/` |

## Plan coverage

| Area | Done | Still needed before launch |
| --- | --- | --- |
| Public site | All pages in both languages with the V3 design; bilingual 404 | Manager and native-Bangla review, real-device accessibility and performance, remaining recovery states |
| Catalog and media | Decimal facts, publication separate from availability, photo approval, normalised uploads | Draft revisions and review, approved contacts and location, real video and panorama upload, file cleanup (A12) |
| Staff access | Named accounts, MFA-gated admin, real sign-in, lockout and logout tests, publish permission | Confirmed roles, recovery and access-review drills, proxy-aware lockout (A09), hosting-level rate limits |
| Customer data | No inquiry storage, no chat transcripts; demo form saves nothing | Restricted inbox, consent record, recipient permissions, retention and deletion, abuse limits, logging and backup inventory |
| AI | Placeholder only; no provider, requests or tools | Provider, transfer and budget decisions; public-fact adapter; quotas; disclosure; bilingual factual and adversarial tests |
| Repository | Private repo, focused commits, secret scans, protected `main`, PostgreSQL CI | Transfer to the company; add maintainers; require an independent reviewer |
| Deployment | Production settings checked with a synthetic config | Staging, proxy and IP policy, TLS, database and storage, logging (A07), health check (A08), backups and restore, monitoring, rollback |

## Limits

- `security.W005` and `security.W021` (HSTS on subdomains, and preload) stay visible on purpose until we know the company's real domains. Don't enable them on unchecked domains.
- `main` needs a pull request and passing `django` and `secrets` checks, even for admins, but needs zero approvals because there's no second maintainer yet. That isn't independent review. Add one before anything goes to production.
- These reviews don't cover a penetration test, ASVS certification, a full privacy-law review, or proof of accessibility and performance.
