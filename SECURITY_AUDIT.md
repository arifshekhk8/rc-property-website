# Foundation Security and Plan Audit

23 October 2026 · Asia/Dhaka · Development milestone, not production approval.

The first implementation follows the agreed Django, bilingual catalog and V3 direction. It did not complete the whole launch plan. In particular, the private remote and an executed PostgreSQL integration run were initially unfinished; this audit established both before proceeding to real inquiries or AI. Custom CSS replaced the proposed Bootstrap layer, and SQLite remains a local-only convenience. These engineering choices are recorded in DECISIONS.md.

## Findings fixed

| ID | Severity and condition | Correction and evidence |
| --- | --- | --- |
| A01 | Medium: an editor granted delete permission could remove live content despite lacking publication authority | Project/FAQ direct deletion and bulk deletion now require publication authority for live records. Tests verify both denial paths and permitted deletion of a draft |
| A02 | Medium: a photo attached to a published project could become public without explicit media approval | Both usage rights and publication approval are required. Public HTML, cover selection and the direct file route agree. Only MFA-verified permitted staff can preview unapproved media; preview responses are private/no-store |
| A03 | High if deployed with missing environment settings: the settings module defaulted to development mode | WSGI now defaults to production and refuses missing/weak secrets, absent/wildcard hosts, SQLite and PostgreSQL without TLS. Local management commands explicitly select development. Subprocess tests verify rejection and valid configuration loading |
| A04 | Medium defense gap: staff/account pages lacked CSP, and inquiry responses lacked explicit cache prevention | Self-hosted-script CSP now covers staff/account/public routes. Contact/inquiry and all POST responses use private/no-store. Inquiry fields are marked sensitive for Django error reporting |
| A05 | Medium process gap: secret scanning and PostgreSQL CI had not executed | Gitleaks scans every staged commit and full history in CI. Hash-locked dependencies, Ruff, Bandit, pip-audit, PostgreSQL tests and synthetic production checks now run in GitHub Actions |
| A06 | Low data-integrity gap: positive price/area rules were enforced by forms but not database constraints | Database check constraints reject zero/negative price and either area measurement even through ORM updates; regression test included |

These severities describe the conditions in the development source, not evidence of an incident or an exposed production system. No production site was deployed during this work.

## Plan coverage

| Area | Current state | Remaining launch work |
| --- | --- | --- |
| Public experience | English/Bangla Home, Projects, both details, Gallery, video/panorama, About/Contact and draft policies; V3 visual direction | Manager review, native Bangla review, real-device accessibility/performance and complete recovery states |
| Catalog and media | Decimal facts, publication/availability separation, approved media boundary, normalized image uploads | Draft revisions/review, approved contacts/location, dedicated real video/panorama replacement and media lifecycle cleanup |
| Staff access | Named accounts supported, MFA-gated admin, real password/TOTP/logout and lockout integration tests, publication permissions | Company-approved role assignments, recovery/expiry/access-review drills and infrastructure rate limits |
| Customer information | No durable inquiry model or chat transcripts; sample form does not save/send contact fields | Restricted inbox, consent evidence, recipient permissions, retention/deletion, duplicate/abuse controls, logging/backup inventory |
| AI | Explicit preview only; no provider, external request, private-data tool or autonomous action | Provider/transfer/budget decisions, isolated public-fact adapter, quotas, disclosure and bilingual factual/adversarial evaluations |
| Repository | Private repo, focused commits, pre-commit/history secret scans, protected main, PostgreSQL CI | Transfer to company ownership when available; add approved maintainers and require an independent reviewer |
| Deployment | Production defaults checked using synthetic configuration | Owned staging, trusted ingress/proxy/IP policy, TLS/database/storage setup, backups/restore, monitoring, rollback and release review |

## Verification and boundaries

Local tests: **34 passed** on Python **3.13.16**, using SQLite. The local environment was upgraded from 3.13.5 without changing system Python. Runtime dependencies remain locked with hashes. Ruff, Bandit and runtime pip-audit passed; Gitleaks reported no secrets in the committed history. The initial remote PostgreSQL 17 run passed 31 tests on Python 3.13.16; the expanded **34-test** PostgreSQL 17 suite also passed on [this run](https://github.com/arifshekhk8/rc-property-website/actions/runs/39985417363), including the full authentication flow on [audit PR #3](https://github.com/arifshekhk8/rc-property-website/pull/3).

Evidence: [initial PostgreSQL/security CI run](https://github.com/arifshekhk8/rc-property-website/actions/runs/39983848657), [current workflow](.github/workflows/checks.yml), [integration tests](app/tests/test_foundation.py), [authentication/configuration/privacy tests](app/tests/test_security.py) and [synthetic production check](scripts/check_production.py). CI uses synthetic database credentials and no production secrets. Asset licenses/provenance accompany the self-hosted files. Original materials, V1/V2 archives and the fourteen V3 image hashes remain unchanged.

`security.W005` and `security.W021` remain visible: HSTS coverage of every subdomain and preload must wait for the actual company domain/TLS inventory. The synthetic check reports these two known domain decisions and fails on other warnings/errors; it does not silence them or establish a deployed system's security. Do not enable subdomain HSTS/preload on unverified company domains.

Main requires pull requests and successful `django` and `secrets` checks, including for administrators; force-pushes and deletion are disabled. No second company maintainer is assigned, so the repository currently requires zero approving reviewers. This is **not independent review**. Add the approved teammate and require at least one independent approval before production work is released. No collaborator was invited or granted access during this audit.

This was an implementation self-review and targeted regression testing. It is not a penetration test, ASVS certification, complete privacy-law review or proof of accessibility/performance. The unresolved items above remain acceptance gates, and no production-readiness claim is made.

## Next milestone

Finish staff draft/review/publish and contact/media controls, then build the private inquiry flow using synthetic data. Obtain company roles, recipients, notices and retention before collecting real leads. Add AI only after the private-data boundary and provider decisions are settled. Replace all sample facts/media and complete staging, independent review and recovery/release checks before public launch.

The deployment approach was checked against the [official Django checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/). Repository settings were verified through GitHub's API; see [GitHub's branch-protection guidance](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
