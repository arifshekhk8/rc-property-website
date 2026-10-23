# RC Property Website

Last updated: 23 October 2026, Asia/Dhaka. Documentation version: 0.9.

This project will help local buyers explore two land listings, publicly named Project 01 and Project 02, see accurate prices and media, and communicate with the company through a Bangla and English AI assistant. The public experience must be welcoming, premium, accessible, fast on mobile, and simple for people aged 35–60. Staff will manage listings and customer interest through a protected administration area. The display naming does not introduce a project/subplot hierarchy.

The group is Real Capita Group. Its public website calls the relevant sister concern RC Property Development Ltd. The exact registered name for this project remains to be confirmed with the company; the user's wording was “Real Capita Plot Dev Lim.” This documentation does not establish legal identity.

## Current status

The first local Django build is implemented from the selected **A / Open Horizon** V3 design. It includes English/Bangla public pages, Project 01/02 details, Gallery/lightbox, sample video and a 360° viewer, plus database-backed staff project/FAQ editing with MFA. All project facts and media are labeled samples. The inquiry form is a non-persistent demo, and the AI launcher explains that live AI is pending.

The foundation was audited against the original plan; see [the audit](SECURITY_AUDIT.md). Thirty-four local tests pass; PostgreSQL CI and secret/dependency checks now execute remotely. Full launch approval remains pending.

Open the running preview at [English](http://127.0.0.1:8000/en/) or [Bangla](http://127.0.0.1:8000/bn/). See [local setup and staff access](app/README.md) to restart it or create your own local administrator. Run `./scripts/dev.sh` from this folder after installing the locked dependencies.

The [fourteen selected V3 boards](design/concepts/v3/README.md), earlier V1/V2 packs and supplied originals remain preserved. Phase 1 has begun; live inquiries, complete review/publishing workflows, real media management, AI integration and deployment are still upcoming. The requested November launch window remains a target, dependent on company inputs and release checks.

## Read these documents

| Document | Purpose |
| --- | --- |
| [REQUIREMENTS.md](REQUIREMENTS.md) | Confirmed requirements, MVP boundaries, acceptance criteria, and unanswered questions |
| [DESIGN.md](DESIGN.md) | Visual direction, reference websites, colors, typography, and accessibility |
| [TECH_STACK.md](TECH_STACK.md) | Proposed technologies, modules, data flow, and hosting criteria |
| [SECURITY.md](SECURITY.md) | Threat model, privacy requirements, security controls, tools, and release checklist |
| [SECURITY_AUDIT.md](SECURITY_AUDIT.md) | Plan coverage, fixed findings, executed checks and remaining launch gates |
| [PLAN.md](PLAN.md) | Development sequence, milestones, dependencies, and completion criteria |
| [PROGRESS.md](PROGRESS.md) | Completed work, verification evidence, current phase, and next actions |
| [DECISIONS.md](DECISIONS.md) | Accepted scope, recommendations, changes, and pending decisions |

## Current workspace

    Intern_/
      RCPDL.png
      RCPDL Logo.ai
      Advanced_Real_Estate_Plot_Website_Features.docx
      README.md
      REQUIREMENTS.md
      DESIGN.md
      TECH_STACK.md
      SECURITY.md
      PLAN.md
      PROGRESS.md
      DECISIONS.md
      app/                 working Django application and local setup guide
      scripts/             development runner and optional asset preparation
      requirements*.lock   hashed runtime/development dependencies
      .github/workflows/   checks with a PostgreSQL CI service
      design/concepts/v1/   visual mockups, review index, and generation prompts
      design/concepts/v2/   new visual proposal, review/handoff notes, and prompts
      design/concepts/v3/   14 selected Open Horizon images, review notes and handoff
      design/concepts/v3/archive/   earlier drafts and homepage alternatives

The supplied files remain intact. A local Git repository, virtual environment, application and development database now exist. The private [GitHub repository](https://github.com/arifshekhk8/rc-property-website) is configured under the user account, with protected main and automated checks. Company ownership/maintainers are pending. No cloud infrastructure, project AI API account or deployment has been configured. Runtime secrets, local databases, uploads, original DOCX/Illustrator references and old design archives are excluded from source control. The fourteen selected V3 boards and their handoff notes are included. V1/V2/archive links refer to the preserved local workspace.

## Recommended starting architecture

Implemented: Django 5.2.18, Python 3.13.16, Django templates, custom CSS and small JavaScript modules, with self-hosted fonts/Pannellum. SQLite supports the local preview; PostgreSQL 17 is configured for CI and required outside development. The server-side AI adapter and separate private inquiry service remain planned.

## Resume and change workflow

At the start of each future session, read PROGRESS.md, DECISIONS.md, and the requirements for the intended task. Read SECURITY.md before implementation or review. The user's latest instruction authorizes implementation using V3 and temporary sample media, superseding the earlier design-only pause. Continue the planned local build within that scope and maintain these eight documents. Preserve supplied assets; company-owned hosting, domains, credentials and production content still require their concrete configuration and decisions.

Record new answers in REQUIREMENTS.md, important changes in DECISIONS.md, and completed work plus verification in PROGRESS.md. Update DESIGN.md, TECH_STACK.md, SECURITY.md, or PLAN.md when the change affects them. Do not convert a recommendation into a confirmed decision without recording the user's or company's answer.

Never put credentials, customer leads, chat transcripts, database exports, or private land documents in this documentation or a repository. A future maintainer should be able to understand what is complete, what was checked, and what remains without needing the original chat.

## Public company sources

Research checked on 15 October 2026: [group company profile](https://rcgcbd.com/about-us/), [RC Property Development page](https://rcgcbd.com/rc-property-development-ltd/), and [RC Holdings website](https://rcholdingsltd.com/). Public information is a research input; staff must approve launch content and contacts.
