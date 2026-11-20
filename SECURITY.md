# Security and privacy

Last updated 21 November 2026.

Security and privacy are part of "done" for every feature. References: [Django security](https://docs.djangoproject.com/en/5.2/topics/security/), the [Django deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/) and [OWASP ASVS 5.0](https://owasp.org/projects/asvs). We aim for ASVS Level 2 on staff access, personal data and application controls. That's a target, not a certification.

What's been checked, and what's still open, is in [SECURITY_AUDIT.md](SECURITY_AUDIT.md).

## What we protect

Staff accounts and MFA secrets; leads (names, phone numbers, messages) and consent records; unpublished content, prices and availability; storage and backups; API keys and billing limits; the company's reputation.

**Untrusted input:** visitor forms and chat, browser-sent history, URLs and query strings, staff uploads, model output, external URLs, third-party libraries. Staff input still gets validated.

**Separate boundaries:** public browsing, the staff area, lead storage, public media and the external AI service. The AI service will receive public facts and screened chat input only: no lead-form data, staff privileges, private documents, database credentials or write tools.

## Controls

| Control | Status | Where |
| --- | --- | --- |
| CSRF on every form | Done | Django middleware; tested |
| Template auto-escaping; staff content escaped in public pages | Done | Tested |
| Admin requires password + TOTP | Done | `config/admin.py` (`AdminSiteOTPRequired`) |
| Lockout after 5 failed logins for 30 minutes, keyed on username + IP | Done (see A09) | `AXES_*` in settings |
| Passwords: at least 12 characters, common, numeric and similarity checks, scrypt hashing | Done | settings |
| Sessions: 1 hour, HttpOnly, SameSite=Lax, Secure in production | Done | settings |
| Production refuses weak or missing secret, missing or wildcard hosts, SQLite, PostgreSQL without TLS | Done | `config/settings.py`; tested |
| HTTPS redirect and 1-year HSTS in production (no subdomains or preload yet) | Done | settings |
| CSP with self-only scripts, `frame-ancestors 'none'`, Permissions-Policy, nosniff, Referrer-Policy | Done | `config/middleware.py` |
| `no-store` on staff, account, contact and inquiry pages and on every non-GET response | Done | `config/middleware.py` |
| Inquiry fields hidden from Django error reports | Done | `sensitive_post_parameters` |
| Demo inquiry never stores or sends data | Done | `website/views.py`; tested |
| Public queries return published records only | Done | `ProjectQuerySet.published()` |
| Publish permission protects live content, including bulk delete | Done | `projects/admin.py`; tested |
| Photo uploads: JPEG, PNG or WebP only, up to 10 MB and 24 MP, verified, re-encoded, metadata stripped, generated file name | Done | `ProjectImage`; tested |
| Unapproved photos private | Done | `projects/views.py`; tested |
| Pannellum `escapeHTML: true` | Done | `static/js/site.js` |
| Secret scanning before each commit and over full history in CI | Done | `.githooks/`, CI |
| Hash-locked dependencies, pip-audit, Bandit; pinned actions; read-only CI token | Done | CI |
| Production logging and a 500 page | **Not done** (A07) | |
| Proxy-aware client IP for lockout | **Not done** (A09) | |
| Rate limits on future public endpoints (inquiry, chat) | Not built yet | |
| Draft/review workflow and staff audit log | Not built yet | |
| Backups, restore test, monitoring | Not built yet | |

The CSP still allows `'unsafe-inline'` for styles. Our templates use no inline styles, so check whether the Django admin needs it before tightening. Django 5.2 has no built-in CSP; if we later need nonces or violation reports, consider django-csp.

## Staff roles (draft)

| Capability | System admin | Manager | Content editor |
| --- | --- | --- | --- |
| Edit listing drafts and media | Yes | Yes | Yes |
| Approve and publish listings and public contacts | Yes | Yes | No |
| Read and manage inquiries | Only if separately authorised | Yes | No |
| Export inquiries | Off at first | Off at first | No |
| Manage staff accounts and permissions | Yes | No | No |
| See application secrets | Through restricted operations access only | No | No |

This is a proposal; the company hasn't confirmed roles (Q03). Django superusers bypass most permission checks, so keep superuser accounts for emergencies, and never promise that a role check hides leads from a superuser. Use named accounts, never shared passwords. Test every direct URL, admin action, list, search, preview and download under each role.

## Rules by area

### Sign-in and sessions

- Use Django's auth, hashing, validators and sessions. No custom password or MFA code.
- Every staff member uses MFA. Test enrollment, admin routes, recovery and any other way in.
- Protect recovery codes. Remove access when someone leaves, and record permission changes.
- Test logout, password change, recovery and expired sessions.
- Throttle at the hosting layer as well as in the app, and make sure no alternative login route skips throttling.

### Data, input and output

- Use the ORM and Django forms. Review any raw SQL or dynamic ordering separately.
- Validate lengths, formats, decimal ranges, publication state and allowed choices on the server. Normalise Bangla digits in phone numbers; a valid format doesn't prove the visitor owns the number.
- Deny staff actions by default. Filter every public query to published content, including chat context and media. Never trust IDs or role flags from the browser or the model.
- Keep auto-escaping on and quote attributes. Avoid `mark_safe`, raw HTML fields and `innerHTML` for chat or messages. Render model output as plain text. Build links from our own IDs, never from model instructions.
- Keep CSRF on every state-changing form, including chat and inquiry. GET must never change data. No wildcard CORS.

### Deployment and secrets

- HTTPS, explicit allowed hosts and trusted origins, DEBUG off, secrets outside source control.
- Trust forwarded HTTPS and IP headers only from our own proxy (`TRUST_PROXY_HTTPS=1` covers HTTPS only; see A09 for the IP).
- Turn on HSTS for subdomains, and preload, only after checking every company subdomain serves HTTPS.
- Least-privilege database and service accounts, a private database network, encrypted transport, disks and backups. Staging and production kept separate.
- Never expose `.env` files, tracebacks, admin dumps or API keys. Rotate anything leaked and record how.

### Media

- Allow only the image, panorama and video formats we need. Enforce file, request and dimension limits; check the real content; re-encode; strip metadata; generate file paths; reject SVG, HTML and anything script-bearing.
- Serve public media with correct content types and no execution. Private files need authentication and private storage. Never fetch remote media from a URL a user gives us (SSRF).

## AI safety

- The server supplies approved facts for the two listings and the FAQs. Prompts are not access control.
- No private-data tools, web access, code execution or admin functions for the model. Lead creation stays separate from chat and needs a human to submit the form.
- Price, area, availability and contact cards come from server data. Check any listing ID the model picks against the published records.
- The assistant admits when it doesn't know, and refers ownership, approvals, returns, negotiation and contract questions to staff. It can't book anything, promise availability, guarantee returns or decide eligibility.
- Keys stay on the server, in a restricted provider project. Limit message size, history and tokens, cap concurrent requests, and enforce global and per-session quotas plus a spending limit in the app. Don't rely on provider budget alerts alone. Timeouts, refusals, outages and exhausted quotas show a safe fallback in both languages.
- Before free-text chat, tell the visitor an external AI service processes it and get their agreement. Screen obvious phone, email and ID patterns, including Bangla digits, and point people to the inquiry form instead. Screening isn't perfect, so the company must accept that residual risk. Don't claim chats are anonymous or that no data leaves Bangladesh.
- Turn off response storage where supported; keep no transcripts. Provider abuse-monitoring retention can still apply (OpenAI's [data controls](https://developers.openai.com/api/docs/guides/your-data) describe this). Zero data retention needs separate approval, so confirm the real account settings before launch.
- Before launch, run a synthetic bilingual test set: ordinary questions, mixed language, unknown facts, sold or unpublished plots, conflicting facts, prompt injection, malicious HTML and links, personal data, duplicate leads, outages and quota limits.

## Privacy and Bangladesh law

Government sources list the **Personal Data Protection Act, 2026** (Act No. 63, gazetted 10 April 2026). Section 1(3) brings parts of it into force at different times. The company or its legal adviser must confirm which provisions apply now, any later rules, and what that means for this site. Sources: [gazette entry](https://www.dpp.gov.bd/bgpress/index.php/document/get_extraordinary/61156), [gazette text](https://www.dpp.gov.bd/upload_file/gazettes/61156_38449.pdf), [ICT Division laws](https://ictd.gov.bd/pages/laws). This is research, not a legal opinion.

The audience is in Bangladesh, but the host, AI provider or other services may process data abroad. Map every processor, storage location, contract and transfer. GDPR isn't our baseline just because the site can be opened from overseas.

We couldn't find a published company privacy policy (that doesn't prove there isn't one). Get the approved policy, or write an accurate bilingual one that describes what the site really does.

### Retention proposal

Starting points for discussion, not approved policy.

| Data | Purpose | Proposed handling |
| --- | --- | --- |
| Name, phone, chosen plot, short message | Reply to the inquiry | Restricted inbox; delete after 90 days unless there's a documented reason |
| Consent time and notice version | Proof of permission | Kept with the inquiry; separate permission if marketing is ever added |
| Chat text | Answer questions | Browser memory and limited server processing; no stored transcript |
| Anonymous session and abuse counters | CSRF, abuse and cost control | Short-lived; no advertising IDs |
| Security and server logs | Investigate abuse and failures | Minimise and redact; 30 days; restricted access |
| Staff audit events | Accountability | IDs, actions and times, never lead contents; retention to be agreed |
| Backups | Recovery | Encrypted and restricted; 30-day rotation; deleted data must not come back after a restore |

Access logs can contain IP addresses even without analytics; include that in the privacy notice. Keep lead and chat fields out of logs, error reports and CI artifacts. No customer data in URLs, localStorage, exports, notifications or admin previews. Permission must be specific to the inquiry, never preticked, and never imply marketing. Provide a privacy contact, a deletion and correction process, and scheduled cleanup.

## Tools

| Tool | Use | Notes |
| --- | --- | --- |
| Ruff, Django checks | Code quality and configuration | Every change; not a security guarantee |
| [Bandit](https://bandit.readthedocs.io/en/latest/) | Python security lint | Every change |
| [pip-audit](https://github.com/pypa/pip-audit) | Known dependency vulnerabilities | Every change and weekly in CI; sends package names and versions to the advisory service |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Secrets in commits and history | Pre-commit hook and CI, with redacted output |
| [Dependabot](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts) | Update proposals | Configured for GitHub Actions, weekly |
| [OWASP ZAP baseline](https://www.zaproxy.org/docs/docker/baseline-scan/) | Passive web scan | Our own staging only, with synthetic data |
| Semgrep (optional) | Extra Django/JS rules | Local mode, metrics off |
| axe-core, Lighthouse | Accessibility and performance evidence | Alongside manual testing |

Keep CI least-privilege with pinned actions, and never run untrusted pull-request code with production secrets. Block confirmed critical or high findings. Triage lower ones with evidence, an owner and a reason.

## Planning risks

| ID | Severity | Risk and action |
| --- | --- | --- |
| S01 | High | Undefined staff permissions could expose leads or allow unauthorised publishing. Agree the role matrix and test direct access |
| S02 | High | Free-text AI may receive personal details and be processed overseas. Approve the disclosure, filtering, provider terms and transfer assessment |
| S03 | High | Chat or media text could become stored or DOM XSS. Use safe rendering, Pannellum escaping, validation and CSP |
| S04 | High | Wrong AI prices, status or ownership claims could mislead buyers. Use data-driven cards, limited context, evaluations and handoff to staff |
| S05 | Medium | Anonymous AI and lead endpoints invite spam and cost abuse. Use quotas, hosting-level limits and safe fallbacks |
| S06 | High | Publishing land documents unreviewed could leak personal or legal information. Keep it out of the MVP |
| S07 | Medium | Hosting, restore and patching owners are unknown. Name accountable staff and test operations before release |

## Release checklist

- [ ] Roles, contacts, privacy owner, budgets, hosting, AI provider and retention confirmed by the company.
- [ ] Staff MFA, throttling, sessions, recovery, revocation and direct-URL authorisation tested.
- [ ] CSRF, validation, ORM use, safe output, published-only data and upload limits tested.
- [ ] CSP, HTTPS headers, allowed hosts, proxy trust, cookies and DEBUG off checked on the real host.
- [ ] Secret scan, dependency audit, static checks and security tests passing.
- [ ] Bilingual AI evaluations, spending limits, data filtering, provider failure and fallback reviewed.
- [ ] Privacy notice, consent, deletion, log restrictions, and no lead fields in AI requests checked.
- [ ] Staging ZAP scan, accessibility tests and real mobile performance checks done.
- [ ] Encrypted backup restored, deletion cleanup verified, rollback demonstrated.
- [ ] Remaining findings, company decisions, test evidence and maintenance owners recorded.
