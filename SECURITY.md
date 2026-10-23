# Security and Privacy Standards

Last updated: 23 October 2026, Asia/Dhaka. Status: baseline controls partly implemented and tested locally; production readiness is not established.

Security and privacy are completion requirements for each feature. Use [Django security guidance](https://docs.djangoproject.com/en/5.2/topics/security/), its [deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/), and applicable requirements from [OWASP ASVS 5.0](https://owasp.org/projects/asvs). Recommend ASVS Level 2 coverage for staff access, personal data, and application controls, with applicability recorded; this is a target, not a certification.

## Assets and trust boundaries

Protect staff accounts and MFA secrets, lead names/phone numbers/messages, consent records, unpublished content, prices and availability, storage, backups, API keys, billing limits, and the company's reputation.

Untrusted inputs include visitor forms and chat, browser-supplied history, URL/query values, uploaded staff media, model output, external URLs, third-party libraries, and imported content. Authenticated staff input still requires validation. Public browsing, the staff area, lead storage, public media, and the external AI service are separate permission/data boundaries.

The AI service receives public facts and screened chat input only. It receives no lead-form data, staff privileges, private documents, database credentials, or write tools. Public anonymity does not remove CSRF, validation, abuse, or privacy requirements.

## First implementation evidence

The local build applies Django CSRF/escaping, staff MFA, password-login throttling, publication permissions, published-only records/protected image routes, upload verification/re-encoding/metadata removal, generated filenames, secure production cookie/HTTPS settings and a public-page CSP. Staff/account routes use separate admin-compatible policy and no-store responses. Inquiries are preview-only with no contact-field storage/transmission; no external AI provider is connected. Production requires explicit secrets and PostgreSQL.

Twenty integration tests passed locally on SQLite, including direct draft/media isolation, MFA/revocation, permission boundaries, CSRF, escaping, consent and upload checks. Ruff/Bandit passed and pip-audit reported no known locked runtime vulnerabilities. These checks do not cover all release requirements. PostgreSQL execution, a deployed configuration, rate limits on future inquiry/AI endpoints, full role/review workflows, recovery, audit/retention, backup restoration, native-device accessibility and penetration review remain outstanding. See PROGRESS.md and app/README.md for commands and scope.

## Proposed staff permissions

| Capability | System administrator | Manager | Content editor |
| --- | --- | --- | --- |
| Edit listing drafts and media | Yes | Yes | Yes |
| Approve/publish listings and public contacts | Yes | Yes | No |
| Read/manage inquiries | Only if separately authorized | Yes | No |
| Export inquiry details | Disabled initially | Disabled initially | No |
| Manage staff accounts/permissions | Yes | No | No |
| View application secrets | Through restricted operational access | No | No |

This matrix is proposed; actual responsibilities remain unknown. Django superusers can bypass many application permissions, so reserve them for restricted operational recovery and do not promise that an ordinary role check can hide leads from a superuser. Prefer non-superuser accounts for daily work. Use named accounts, not shared passwords. Verify every direct URL, admin action, list, search, preview, and download under each role.

## Required implementation controls

### Authentication and sessions

Use Django's authentication, password hashing, password validators, and session handling. Recommend a maintained MFA package such as [django-two-factor-auth](https://django-two-factor-auth.readthedocs.io/en/stable/), subject to compatibility and maintenance checks before installation. Require MFA for all staff and verify enrollment, admin routes, recovery, and any alternate login route. Avoid custom password or MFA algorithms.

Prefer Django's supported scrypt hasher after deployment resource testing. Store hashes only. Protect MFA recovery codes, revoke access when staff leave, and record permission changes. Define session lifetime and idle behavior after staff workflow review. Use server-side sessions and secure, HttpOnly session cookies with appropriate SameSite policy. Test logout, password change, recovery, and expired sessions.

Django does not include authentication throttling by default. Require rate limits at the trusted ingress and application layer; choose a compatible package only if the host cannot supply needed controls. Prevent a login or MFA bypass through an unthrottled alternate endpoint.

### Authorization, SQL, input, and output

Use ORM parameterization and validated Django forms. Review every raw query or dynamic ordering clause separately. Validate field lengths, supported formats, decimal ranges, object ownership, publishing state, and allowed choices on the server. Normalize Bangla/ASCII digits where needed for phone validation; format validation does not prove the visitor owns a number.

Default-deny staff operations. Filter public queries to published, visible content, including chat context and media. Do not trust IDs or role flags from a browser or model.

Keep template autoescaping on and quote attributes. Avoid mark_safe, unsafe template filters, raw HTML content fields, and innerHTML for chat/messages. Render model output as plain text or tightly controlled components. Validate link schemes and destinations; generated URLs must come from application-owned identifiers, not model instructions.

Keep CSRF middleware active on staff and public state-changing forms, including chat and interest submission. Use appropriate request methods; GET must not modify records. SameSite cookies and CORS rules do not replace CSRF checks. Do not add wildcard CORS for a same-origin application.

### Deployment and secrets

Require HTTPS, explicit allowed hosts and trusted origins, production DEBUG off, and secret values outside source control. Trust forwarded HTTPS/IP headers only from configured proxies. Introduce HSTS carefully after verifying HTTPS and relevant subdomains. Add suitable CSP, clickjacking protection, content-type protections, referrer policy, and restrictive permissions policy.

Django 5.2 does not have the newer built-in CSP middleware. Recommend [django-csp](https://django-csp.readthedocs.io/en/latest/) or equivalent ingress headers, with report-only testing before enforcement. Avoid unsafe script directives where possible. Do not weaken the policy merely to accommodate an unnecessary embed.

Use least-privilege database and service accounts, a private database network, protected storage, and encrypted transport, disks, and backups. Keep staging/production separate. Never expose environment files, traceback pages, admin dumps, secret-bearing commands, or API keys in client JavaScript. Rotate compromised credentials and document recovery.

### Media

Allow only needed image, panorama, and video formats. Enforce request/file/dimension limits, validate actual content, re-encode images, strip unnecessary metadata, use generated paths, and reject SVG/HTML/script-bearing uploads. Check decompression/resource limits. Approved logo exports are handled separately from ordinary staff uploads.

Serve normalized public media from configured static/object storage with correct content types and no execution. Private files require authenticated access and private storage; public PDF/land documents are outside the initial scope. Do not let the server fetch arbitrary remote media URLs, avoiding SSRF and unexpected disclosure.

Pannellum's API configuration defaults HTML escaping off. Explicitly set escapeHTML true, validate captions/hotspots, disallow arbitrary hotspot HTML and unsafe links, and test with malicious content. See its [configuration reference](https://pannellum.org/documentation/reference/#escapehtml-boolean). This is a design control for a proposed dependency, not a discovered application flaw.

## AI security and safety

The server supplies current approved facts for only the two listings and FAQs. Do not use model prompts as access control. Give the provider no private-data tools, web access, code execution, or administrative functions. Separate lead creation from chat and require a human-initiated form submission.

Show price, area, availability, and contact cards from server data. Validate any model-selected plot IDs against public records. The assistant must admit missing information and refer ownership, approvals, investment returns, negotiation, and contractual questions to staff. It cannot book, promise availability, guarantee returns, or make housing eligibility decisions.

Keep keys server-side, use restricted provider projects, bound message sizes/history/tokens, cap concurrent requests, and enforce global/per-session quotas and application-side spend limits. Do not rely only on provider budget alerts. Timeouts, provider refusal, outages, and quota exhaustion must produce a safe bilingual fallback.

Before sending free text, disclose external AI processing and ask for affirmative agreement. Screen obvious phone/email/identity patterns, including Bangla numerals, and direct personal details to the separate form. Screening cannot guarantee removal of every personal detail; the company must approve the residual risk and processor arrangements. Do not claim all conversations are anonymous or that no data leaves Bangladesh.

Set supported response storage off, avoid durable conversation objects/background jobs, and do not store application transcripts by default. [OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data) distinguish application storage from standard abuse-monitoring retention, commonly up to 30 days with exceptions. Zero Data Retention requires eligibility/approval; it is not assumed. Confirm actual provider account behavior before launch.

Run a synthetic bilingual evaluation set containing ordinary questions, mixed-language input, unknown facts, sold/unpublished plots, conflicting facts, prompt injection, malicious HTML/links, personal identifiers, duplicate lead attempts, outage, and quota cases. Require no access-boundary violation in the tested set, staff review of factual answers, and documented limitations. Follow [official AI safety guidance](https://developers.openai.com/api/docs/guides/safety-best-practices).

## Privacy and Bangladesh requirements

Government sources list the Personal Data Protection Act, 2026, Act No. 63, gazetted on 10 April 2026. Section 1(3) has staggered commencement provisions. The company/legal adviser must verify currently applicable provisions, later notifications/rules, and obligations for its exact processing before launch. Do not rely solely on the earlier 2025 ordinance.

Sources: [official gazette entry](https://www.dpp.gov.bd/bgpress/index.php/document/get_extraordinary/61156), [gazette text](https://www.dpp.gov.bd/upload_file/gazettes/61156_38449.pdf), and [ICT Division current laws](https://ictd.gov.bd/pages/laws), which also lists cyber protection legislation and amendments. This planning review identifies the relevant current law; it does not establish complete legal compliance, mandatory localization, or a breach-notification deadline.

Domestic targeting does not prevent overseas processing by a host, AI service, analytics vendor, or communication provider. Map those processors, storage locations, access, contracts, and transfers. GDPR is not an assumed baseline merely because the website can be opened overseas; reassess if operations/targeting change.

A published company privacy policy could not be verified from the pages inspected. Attempts to fetch likely privacy-policy URLs did not establish absence. Obtain the approved policy or write an accurate bilingual policy describing this site's actual behavior.

### Data minimization and retention proposal

| Data | Purpose | Proposed handling, pending company approval |
| --- | --- | --- |
| Name, callback phone, selected plot, short message | Respond to requested sales inquiry | Restricted inbox; proposed deletion after 90 days unless a documented need/lawful exception applies |
| Consent timestamp and notice version | Evidence of inquiry permission | Keep with inquiry; separate marketing permission if marketing is later introduced |
| Chat text | Answer plot questions | Volatile browser history and bounded server processing; no durable application transcript |
| Anonymous session/abuse counters | CSRF and abuse/spend control | Short-lived technical state; no advertising ID; establish expiry and cleanup |
| Security/server logs | Diagnose abuse and failures | Minimize/redact identifiers; proposed 30-day retention; restrict access |
| Staff audit events | Accountability | IDs/actions/timestamps, no copied lead contents; retention to be approved |
| Backups | Recovery | Encrypted, access-restricted; proposed 30-day rotation with documented deletion/recovery handling |

Retention proposals are engineering defaults for discussion, not approved policy. Access logs can contain IP addresses even without analytics; minimize them and include actual practices in the privacy inventory. Redact lead/chat fields from logs, error monitoring, and CI artifacts. No customer information in URLs, browser localStorage, exports, notifications, or public admin previews.

Use clear purpose-specific permission before lead submission. Make no marketing subscription automatic. Provide a company-controlled privacy contact, deletion/correction process, and retention cleanup. Restoration from a backup must not silently reactivate previously deleted customer data; document deletion records and post-restore cleanup.

## Automated workflow and recommended tools

| Tool / integration | Use | Timing and privacy notes |
| --- | --- | --- |
| Ruff and Django checks | Code quality and configuration | Local/CI; not a security guarantee |
| [Bandit](https://bandit.readthedocs.io/en/latest/) | Python static security checks | Each relevant change; review severity and confidence |
| [pip-audit](https://github.com/pypa/pip-audit) | Known dependency vulnerabilities | Dependency changes, CI, recurring checks; advisory queries disclose package/version metadata |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Secrets in changes/history | Before commits and in CI; redact findings and restrict artifacts |
| [Dependabot](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts) | Dependency alerts and update workflow | After a company-owned private GitHub repository exists; confirm settings/feature access |
| [OWASP ZAP baseline](https://www.zaproxy.org/docs/docker/baseline-scan/) | Passive web checks during a limited crawl | Owned staging only, synthetic data; review traffic and report exposure |
| Semgrep, optional | Targeted Django/JS rules if more coverage is needed | Local mode, reviewed rules, metrics off; do not authenticate/upload findings without approval of data handling |
| axe-core and Lighthouse | Accessibility/performance evidence | Alongside manual tests; automated coverage is incomplete |
| Codex Security, optional | Contextual vulnerability investigation/review | Available but not installed/connected as of this review; assess permissions and source-code handling before use |

Use a company-owned private repository with least-privilege CI, protected production secrets, restricted artifacts, and pinned trusted actions. Untrusted pull-request code must not run with production credentials. Require tests and security checks before merging; perform deploy checks against production-like settings before release. Block confirmed critical/high issues; triage lower findings and false positives with evidence, owner, expiry, and rationale.

Recommended Codex skills: use OpenAI Docs for AI API/data-control changes; use skill-creator later to package a narrow project security-review workflow based on this file; use skill-installer only for a vetted skill after reviewing its source and permissions. No dedicated security auditing skill has been verified as installed here. Skills guide reviews; scanners, tests, and human judgment provide evidence. [Codex Security guidance](https://developers.openai.com/blog/scaling-cyber-defenders-with-daybreak) describes the optional integration. No plugin, package, or custom skill was installed in this planning phase.

## Planning risks requiring resolution

| ID | Potential severity | Risk and required action |
| --- | --- | --- |
| S01 | High | Undefined staff permissions could expose leads or allow unauthorized publishing; agree the matrix and test direct access |
| S02 | High | Free-text AI can receive unintended personal details and use overseas processing; approve disclosure, filtering, provider terms, and transfer assessment |
| S03 | High | Untrusted chat/media text could become stored or DOM XSS; use safe rendering, Pannellum escaping, validation, and CSP |
| S04 | High | Incorrect AI prices, status, or ownership claims can mislead buyers; use authoritative cards, constrained context, evaluations, and human handoff |
| S05 | Medium | Anonymous AI/lead endpoints can cause spam or cost/availability abuse; apply atomic quotas, ingress limits, and safe fallback |
| S06 | High | Unreviewed land-document publication could disclose personal/legal information; keep it outside MVP and require review before any expansion |
| S07 | Medium | Hosting, restoration, and patch ownership are unknown; select accountable staff and verify operations before release |

These are potential-impact planning risks. No code vulnerability is claimed. For each actual finding later, record affected file/version, evidence, severity, exploit conditions, privacy impact, recommended fix, owner, and retest result. Do not repeat secrets or real customer data in reports.

## Release checklist

- [ ] Confirm roles, contacts, privacy owner, budgets, hosting, provider processing, and approved retention.
- [ ] Verify staff MFA, throttling, sessions, recovery, revocation, and direct-route authorization.
- [ ] Verify CSRF, validation, ORM use, safe output, published-only data, and upload limits.
- [ ] Verify CSP and HTTPS headers, allowed hosts, proxy trust, cookie behavior, and DEBUG off.
- [ ] Confirm secrets scan, dependency audit, static checks, and security-sensitive tests pass.
- [ ] Review bilingual AI evaluations, spend limits, data filtering, provider failure, and fallback.
- [ ] Verify privacy notice, consent, deletion, access/log restrictions, and absence of lead fields from AI payloads.
- [ ] Complete staging ZAP baseline, accessibility tests, and realistic mobile performance checks.
- [ ] Restore an encrypted backup, verify deletion cleanup, and demonstrate rollback.
- [ ] Record residual findings, company decisions, test evidence, and maintenance responsibilities.
