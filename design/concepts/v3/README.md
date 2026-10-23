# V3 — Open Horizon: Complete Design Review Pack

Updated: 23 October 2026, Asia/Dhaka. Status: all agreed page types and principal workflows designed for review; no application code.

V3 extends the user-selected **A / Open Horizon** homepage across the website, using **Project 01** and **Project 02** consistently. The approved homepage is preserved unchanged. This folder now contains a full pack comparable to V1/V2, rather than only a homepage choice.

The main folder contains **one selected image per page/workflow: 14 PNGs total**. Earlier drafts and homepage alternatives are in [archive/](archive/README.md). The selected files use simple numbered names, without final/refined duplicates.

## Review all designs

| Board | Coverage |
| --- | --- |
| [01 Home](01-home.png) | Selected cinematic homepage, Gallery and Virtual Site Visit sections |
| [02 Projects](02-projects.png) | Desktop catalog and English mobile; both projects with essential facts |
| [03 Project 01 detail](03-project-01-details.png) | Desktop/mobile, green identity, gallery, facts, media, inquiry and location |
| [04 Project 02 detail](04-project-02-details.png) | Desktop/mobile, sandy identity, correct aerial view, facts, media and inquiry |
| [05 Gallery and photo viewer](05-gallery.png) | Expanded Gallery, mobile and lightbox with close/previous/next controls |
| [06 Virtual Site Visit](06-virtual-site-visit.png) | Desktop panorama, mobile video and mobile 360° view |
| [07 AI assistant and inquiry](07-assistant-inquiry.png) | AI disclosure, bilingual conversation example, separate consent form and receipt |
| [08 About and Contact](08-about-contact.png) | Both public pages, pending contacts, purpose-specific inquiry consent and mobile previews |
| [09 Privacy and Terms](09-privacy-terms.png) | Both draft-policy layouts with mobile examples and company-review labeling |
| [10 Staff project content](10-staff-content.png) | Two-record management, bilingual editor, media and publication review |
| [11 Staff access and inquiries](11-staff-access-inquiries.png) | Staff sign-in, MFA, inbox and inquiry detail |
| [12 Staff FAQs and public contacts](12-staff-faqs-contacts.png) | Bilingual content/contact settings and review/publish workflow |
| [13 Mobile and Bangla](13-mobile-bangla.png) | English/Bangla Home, Bangla Project 01 detail and inquiry form |
| [14 Feedback and recovery](14-feedback-recovery.png) | Form validation/sending/failure, AI outage, media failure and staff restriction |

Start with 02–06 to review the new project/media pages. Then check 07–09 for the communication/supporting pages and 10–14 for staff, language and recovery coverage.

## What this pack covers

All seven agreed public page types are represented: Home, Projects, Project detail (both records separately), About, Contact, Privacy and Terms. Expanded Gallery and video/panorama views cover the two added homepage sections. Staff content, sign-in/MFA, inquiry handling, FAQs and business-contact settings are included. Desktop and representative English/Bangla mobile examples establish the shared direction, as in V1/V2.

These are raster design boards, not a separate image of every page in every language at every viewport. [DESIGN_NOTES.md](DESIGN_NOTES.md) specifies responsive rules, language behavior, gallery/media interactions, inquiry boundaries, staff publication states and further recovery cases. A full design pack is not a working website or automatic approval of every new screen.

## Selected direction and sample boundaries

Use the selected image-led composition, short headings, white surfaces, navy text, blue actions and green availability labels. Public naming is Project 01 / Project 02; no parent-project/child-plot hierarchy or added transactional features are introduced.

Project 01 uses green grass with corner posts; Project 02 uses sandy ground and a low boundary wall. All property images are AI-generated illustrations, not actual verified photos. Prices, measurements, locations and availability are sample data; no land-unit conversion or legal/ownership claim is established. Actual company contacts, facts, approved translations and licensed media must replace placeholders before launch.

Privacy and Terms are draft layouts, not reviewed legal notices. Staff roles and operating/privacy decisions remain pending. Use approved original logo exports during implementation, not the generated logo approximations. Exact colors, font sizes and focus behavior come from the design specification and must be verified interactively.

## Preservation and generation

V1, V2 and the approved homepage image contents remain unchanged. Seven superseded V3 boards and three homepage alternatives are retained only in the archive. The table above links to the fourteen canonical selected images. Refinements correct project photo identity, purpose-specific inquiry permission, sending/success separation, draft-policy wording, staff headers and sample copy.

- [Homepage edit prompt](PROMPTS.md)
- [Full-pack generation prompts](FULL_PACK_PROMPTS.md)
- [Refinement prompts](REFINEMENT_PROMPTS.md)
- [Final visual-review correction prompts](FINAL_REVIEW_PROMPTS.md)
- [Pre-work preservation manifest](PRESERVATION.json)
- [Selected-board manifest](SELECTED_BOARDS.json)
- [Verification record](VERIFICATION.json)
- [Original homepage options](archive/homepage-options/README.md)
- [File relocation record](archive/RELOCATIONS.json)

Generated with the built-in image-generation tool; no CLI/API-key workflow. All selected outputs are saved in this project folder.

## Verification

All fourteen selected boards were visually inspected for page coverage, hierarchy, Project 01/02 identity, sample facts, consent separation and excluded-feature boundaries. Targeted refinements were re-inspected. PNG signatures/dimensions are valid; twelve new boards are 1536 × 1024, the AI/inquiry board is 1774 × 887 and the preserved homepage is 1024 × 1536. All 56 pre-work preserved files match their hashes. All local links across 24 Markdown documents resolve. These checks verify design artifacts and preservation; no application, interaction, accessibility, performance or security tests are claimed.

Cleanup on 23 October moved earlier images into the archive and renamed selected images without changing their contents. The historical preservation manifest retains its original paths; use RELOCATIONS.json to locate moved files. Archived documentation links were updated for the new locations. VERIFICATION.json records the current cleanup checks.

## Next step

1. Review the complete V3 with the manager, concentrating on the project pages, inquiry path and mobile/Bangla readability. Record any concrete revisions.
2. Collect approved facts/media for both projects, business contacts, legal brand, staff responsibilities, hosting/budgets and privacy/provider decisions. REQUIREMENTS.md Q01–Q09 is the decision checklist.
3. With the user's instruction to begin implementation, create the private repository and Django foundation, then build one bilingual published project editable by authorized staff. Extend to the second project, media, inquiries and AI in PLAN.md order.

[NEXT_STEPS.md](NEXT_STEPS.md) provides the company-content checklist and the concrete first implementation milestone.

No application, dependencies, repository, infrastructure or deployment was created by this design work.
