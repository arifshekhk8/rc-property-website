# RC Property Website

Internal working notes. Last updated 21 November 2026.

## What this is

Arif's internship project: a bilingual (English/Bangla) Django website for RC Property Development Ltd., a sister concern of Real Capita Group. Visitors browse two land listings, Project 01 and Project 02, and send an inquiry. Staff edit content in an admin area that needs a password and an authenticator code.

The company's exact registered name is not confirmed yet. Arif's first description was "Real Capita Plot Dev Lim."; the company website says "RC Property Development Ltd." This is Q01 in [REQUIREMENTS.md](docs/REQUIREMENTS.md#open-questions).

## Where things stand

- **This repo holds the foundation build from 23 October 2026.** All public pages work in both languages, with two sample listings, a gallery, a sample video and 360° view, a demo inquiry form that stores nothing, and staff editing with MFA. Every fact and image is a labelled sample.
- **New feature work happens in a separate private repo, `arifshekhk8/rcpdl-website`.** It started from this repo's history on 7 November 2026 and released the "Grounded Premium" redesign as v0.2.0 on 8 November. Change this repo only when Arif asks.
- **21 November 2026:** code review and cleanup here. Templates re-indented (no visual change), a proper bilingual 404 page, and these docs rewritten. See [PROGRESS.md](docs/PROGRESS.md).
- Nothing is deployed. There is no production server, domain, AI provider or real customer data.

## Run it

```bash
python3.13 -m venv .venv          # needs Python 3.13.16 (see .python-version)
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
./scripts/dev.sh                  # migrate, add sample data, serve on 127.0.0.1:8000
```

Open http://127.0.0.1:8000/en/ or http://127.0.0.1:8000/bn/. Staff setup and the full list of checks are in [app/README.md](app/README.md).

## Documents

| File | Read it for |
| --- | --- |
| [PROGRESS.md](docs/PROGRESS.md) | Current state, latest check results, open items, next steps |
| [DECISIONS.md](docs/DECISIONS.md) | What was decided, by whom and when |
| [REQUIREMENTS.md](docs/REQUIREMENTS.md) | Agreed scope, exclusions, launch criteria, questions for the company |
| [PLAN.md](docs/PLAN.md) | The original six-week plan, where we really are, definition of done |
| [DESIGN.md](docs/DESIGN.md) | Visual direction, colours, type, accessibility targets |
| [TECH_STACK.md](docs/TECH_STACK.md) | What it's built with, code layout, data model, what's still planned |
| [SECURITY.md](docs/SECURITY.md) | Security and privacy rules every feature must meet |
| [SECURITY_AUDIT.md](docs/SECURITY_AUDIT.md) | Findings fixed, findings still open, evidence |
| [app/README.md](app/README.md) | Developer guide: setup, staff access, checks, sample assets |
| [design/concepts/v3/](design/concepts/v3/README.md) | The 14 selected Open Horizon design boards and interaction notes |

## How we work

- **Starting a session:** read `docs/PROGRESS.md`, then `docs/DECISIONS.md`. Read `docs/SECURITY.md` before changing code.
- **Record as we go** (all in `docs/`): company answers go in REQUIREMENTS.md, decisions in DECISIONS.md, finished work and check results in PROGRESS.md. Update the other docs when a change affects them.
- **A recommendation is not a decision** until Arif or the company confirms it.
- **Commits:** only when Arif asks. Small, focused commits with an imperative subject line and no AI attribution lines. `main` is protected: changes go in through a pull request, and the `django` and `secrets` checks must pass.
- **No secrets or personal data** in the repo or these docs: no credentials, customer leads, chat transcripts, database exports or private land documents.
- **Keep the supplied originals unchanged:** `RCPDL.png`, `RCPDL Logo.ai` and the feature DOCX. Their hashes are in PROGRESS.md.

## Workspace layout

```text
Intern_/
  app/                      Django project: config, projects, website, templates, static, tests
  docs/                     planning, decisions, design direction, security, progress
  scripts/                  dev runner, production-settings check, Gitleaks installer, asset export
  design/concepts/v3/       14 selected design boards and notes (tracked)
  design/concepts/v1, v2    earlier design packs (local only, git-ignored)
  .github/                  CI workflow and Dependabot config
  requirements*.in / .lock  dependencies; the locks are hashed (uv pip compile)
  RCPDL.png                 supplied logo (tracked)
  RCPDL Logo.ai, *.docx     supplied originals (local only, git-ignored)
```

## Company sources

Checked 15 October 2026: [group profile](https://rcgcbd.com/about-us/), [RC Property Development page](https://rcgcbd.com/rc-property-development-ltd/), [RC Holdings](https://rcholdingsltd.com/). Treat these as research only; staff must approve any content or contact we publish.
