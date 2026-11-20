# Plan

Last updated 21 November 2026.

## Original timeline and where we are

Arif asked for about 1–1.5 months from 15 October. The baseline was six weeks, ending 26 November 2026.

| Phase | Planned | Actual, in this repo |
| --- | --- | --- |
| 0. Scope and design | 15–21 Oct | Done by 23 Oct (three design rounds) |
| 1. Foundation | 22–28 Oct | Done 23 Oct: Django, MFA, permissions, CI, private repo |
| 2. Catalog and content | 29 Oct – 4 Nov | Partly done: bilingual pages, two sample listings, gallery, publish permission. Missing: draft/review workflow, editable contacts, real location |
| 3. Media and communication | 5–11 Nov | Partly done: sample video and 360° view. Missing: real media management, inquiry inbox, AI |
| 4. Verification | 12–18 Nov | Not started here |
| 5. Deployment and handover | 19–26 Nov | Not started; no host or domain yet |

The 26 November target won't be met from this repo. Work moved to `rcpdl-website` on 7 November (D25). Launch dates depend on the company's answers to Q01–Q09 and need re-planning there.

## Build order

This order still applies wherever the work continues.

1. **Thin path first:** one published listing in both languages, editable by a permitted staff account, with checks and separate environments from the first change. *Done.*
2. **Both listings and navigation,** then photos and facts before heavy media. *Done with samples.*
3. **Video and panorama,** tested for accessibility and security on their own. *Done with samples.*
4. **Inquiry form and restricted inbox, before AI,** so the private-data boundary is proven by itself.
5. **AI through a provider adapter,** using approved public facts only. Test with synthetic conversations. Inquiry data must never enter its requests, and quotas, outages and bad output must fail safely.
6. **Staging with synthetic leads:** production settings, headers, storage access, translated privacy text, backups and alerts. Plan any domain move with a rollback.

## Definition of done (every feature)

- It matches REQUIREMENTS.md.
- The code is readable and reviewed, and the relevant tests and checks pass.
- Role and public-data boundaries hold.
- It collects only the data it needs, and that data is documented.
- It works in both languages, on mobile and with a keyboard.
- It stays within the performance budget.
- Any new dependency is justified.
- Risks are fixed, or recorded with an owner.
- The docs record the result.

Tests should target real risks: permission bypass, private-data leaks, consent, upload limits, unsafe model output and abuse limits. A screenshot or a clean scanner run alone doesn't make a feature done.

## Handover (at launch)

Train the teammate to update both languages, change prices and status, replace media safely, handle inquiries, manage staff access and ask for help. Once the systems exist, document deployment, migrations, secret rotation, backup restore, data deletion, provider quotas and rollback. The company must name who owns patches, incidents, backups, privacy requests and billing.

## Changing scope

Record the reason in DECISIONS.md, check the effect on security, privacy, accessibility and time, and update the affected docs before building. Add search, a CMS, queues or a project hierarchy only when real volume or workflow needs them.
