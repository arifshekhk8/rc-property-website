# V3: Open Horizon design boards

Last updated 21 November 2026.

Arif chose **A / Open Horizon** on 23 October 2026. These 14 boards extend that homepage to every agreed page and staff workflow. The design was built into the app the same day. Use the boards as a reference; where they differ from the running app, the app wins.

## Boards

| Board | Shows | In the app? |
| --- | --- | --- |
| [01 Home](01-home.png) | Hero, both projects, Gallery and Virtual Site Visit sections | Yes |
| [02 Projects](02-projects.png) | Catalog on desktop and mobile | Yes |
| [03 Project 01](03-project-01-details.png) | Detail page, green identity: photos, facts, media, inquiry, location | Yes; location pending |
| [04 Project 02](04-project-02-details.png) | Detail page, sandy identity | Yes; location pending |
| [05 Gallery](05-gallery.png) | Gallery and photo viewer with close, previous and next | Yes |
| [06 Virtual Site Visit](06-virtual-site-visit.png) | Panorama on desktop; video and 360° on mobile | Yes, with samples |
| [07 AI assistant and inquiry](07-assistant-inquiry.png) | AI disclosure, sample chat, separate consent form, receipt | Form and receipt as a demo; chat not built |
| [08 About and Contact](08-about-contact.png) | Both pages, pending contacts, inquiry consent | Yes; contacts pending |
| [09 Privacy and Terms](09-privacy-terms.png) | Draft policy layouts | Yes; draft text |
| [10 Staff content](10-staff-content.png) | Project list, bilingual editor, media, publication review | Partly: Django admin editing; no draft/review |
| [11 Staff access and inquiries](11-staff-access-inquiries.png) | Sign-in, MFA, inquiry inbox and detail | Sign-in and MFA yes; inbox not built |
| [12 Staff FAQs and contacts](12-staff-faqs-contacts.png) | FAQ and public-contact settings with review | FAQ editing yes; contacts and review not built |
| [13 Mobile and Bangla](13-mobile-bangla.png) | English and Bangla home, Bangla Project 01, inquiry form | Yes |
| [14 Feedback and recovery](14-feedback-recovery.png) | Form errors, sending, failure, AI outage, media failure, staff restriction | Form errors and sending yes; the rest depends on unbuilt features |

## What the boards are, and aren't

- Static images, not a picture of every page at every size in both languages. Responsive and interaction rules are in [DESIGN_NOTES.md](DESIGN_NOTES.md).
- Every property image is AI-generated. Prices, sizes, locations and availability are samples. Project 01 shows green grass with corner posts; Project 02 shows sandy ground with a low wall.
- Logos in the boards are AI approximations. The app uses the official logo export.
- Privacy and Terms boards are draft layouts, not legal text.

## Files

Prompt files are kept word-for-word as a record of how each board was made:

- [PROMPTS.md](PROMPTS.md): the homepage edit
- [FULL_PACK_PROMPTS.md](FULL_PACK_PROMPTS.md): boards 02–14
- [REFINEMENT_PROMPTS.md](REFINEMENT_PROMPTS.md) and [FINAL_REVIEW_PROMPTS.md](FINAL_REVIEW_PROMPTS.md): corrections
- `SELECTED_BOARDS.json`: which file was selected for each board

Local only (git-ignored): `archive/` (7 superseded boards, 3 homepage options, `RELOCATIONS.json`), `PRESERVATION.json` and `VERIFICATION.json` (file-hash records), and the V1 and V2 packs. The prompt files use file names from before the 23 October cleanup; `archive/RELOCATIONS.json` maps old names to new ones.

## Checked on 23 October

All 14 boards were inspected for page coverage, Project 01/02 identity, sample facts, consent separation and scope. Twelve boards are 1536 × 1024 px, the AI/inquiry board is 1774 × 887 px, and the homepage is 1024 × 1536 px. Earlier design files matched their preserved hashes.
