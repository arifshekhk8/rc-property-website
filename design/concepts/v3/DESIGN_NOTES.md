# V3 design and interaction notes

Last updated 21 November 2026. This is the interaction spec behind the [V3 boards](README.md). It goes with [REQUIREMENTS.md](../../../REQUIREMENTS.md) and [SECURITY.md](../../../SECURITY.md). Items marked **(built)** exist in the app; everything else is still to do.

## Visual system and naming

- Keep the selected homepage look: white surfaces, navy headings, blue buttons, green availability labels, large land images and short copy. Colours come from the tokens in [DESIGN.md](../../../DESIGN.md#interface-palette), not from the generated pixels. **(built)**
- Use the official logo export, not the AI-drawn versions in the boards. **(built)**
- Names: Project 01 and Project 02 in English; প্রকল্প 01 and প্রকল্প 02 in Bangla. Use them in navigation, headings, cards, the inquiry form and staff screens. Display names only; no parent-project/child-plot system. **(built)**
- Marketing pages lead with images and short headings, but always show price, both area units, location, availability and the next action. Forms, policies and staff screens use the same type and colours without decorative photos. **(built)**
- Noto Sans and Noto Sans Bengali, visible focus, clear labels, and buttons and form fields at least 44 px tall. **(built)** Check text links and the 19 px consent checkbox (its label is clickable) on touch screens. Final sizes are in DESIGN.md.

## Page structure

Home → Projects → Project 01 or 02 → inquiry or AI. Gallery and Virtual Site Visit are reachable from Home and from each project page. About, Contact, Privacy and Terms are always one click away. **(built)**

Gallery and Virtual Site Visit are separate pages (`/gallery/`, `/visit/`), keeping their return links to the project. **(built)** Video and 360° form one shared media view, not extra menu items.

Out of scope: customer accounts, appointments, reservations, payments, customer uploads, ROI tools, blog and careers pages. Staff sign-in is for company staff only.

## Facts and imagery

| Project | Sample imagery | Sample facts |
| --- | --- | --- |
| Project 01 | Green grass with white corner posts | 3 katha / 2,160 sq ft; ৳45,00,000 total |
| Project 02 | Sandy ground with a low boundary wall | 5 katha / 3,600 sq ft; ৳75,00,000 total |

These are samples, not real prices or a conversion rule. Every land image is AI-generated. Replace all sample locations, availability and media with approved facts and licensed photos. Never invent road width, approvals, title, possession date, distances or contacts.

Keep the landscape hero separate from either project's identity. Reuse a project's image only when it refers to that project. Forms, receipts, legal pages and error states don't need decorative land photos.

The location block shows a "pending" note, not a map. **(built)** Add an external map link only after staff approve the destination.

## Responsive and bilingual behaviour

- Columns stack in reading order, essential facts stay visible, forms go full-width on phones, and supporting pages become a single column. **(built)**
- Switching language keeps the current page, project and query string. **(built, tested)**
- Every control, error, status message, disclosure and policy needs a human-approved translation. Numbers use ASCII digits for now, pending a native reader's review. Check Bangla glyphs and longer labels at 320 px and with zoom.
- One main button in the home hero. **(built)** The mobile menu uses `<details>`; check focus order on real devices. Floating buttons must never cover content, focus or the device's safe areas. No chat window opens by itself. **(built)**

## Gallery and media behaviour

- The photo viewer shows the selected photo with its caption, previous and next buttons, a close button and arrow keys. Escape closes it and focus returns to the photo that opened it (native `<dialog>` behaviour; confirm in Safari). No slideshow. **(built)**
- Video and panorama load only after the visitor chooses them. **(built)** Video uses native controls and captions; add a transcript if the real video has speech. **(built, captions)**
- The 360° view rotates a fixed image; it is not a 3D model. No auto-rotation; zoom, move and fullscreen controls; photo and text fallback; link back to the project. **(built)** Don't trap page scrolling on phones; check this on a real device.

## AI and inquiry boundary

- Before chat starts, show that it's an AI service run by an outside provider, with a way back and a non-AI contact option. Use approved public facts and app-rendered cards. Keep answers short. The model never sees staff data, unpublished content or inquiries.
- The inquiry form is separate and works without the chat. Fields: optional name, required phone, selected project, optional short message. The permission box starts unchecked, covers only replying to this inquiry, and never implies marketing. **(built as demo)**
- Form fields never become AI input. Visitors might still type personal details into chat, so disclosure, screening, limits and a provider review remain necessary (see SECURITY.md).
- Show the confirmation only after the inquiry is really stored. It confirms an inquiry, not a booking, sale or callback time. Label the visitor's number as "Your submitted number", separate from the business contact. Never show placeholder contacts as tappable phone links. **(built: the demo receipt says nothing was stored)**
- After a validation error, keep the visitor's entries and their permission choice. **(built)**

## Staff workflows

- A compact staff area: Projects, Inquiries, FAQs and Public contacts, delivered as a customised Django admin, not a separate dashboard. **(partly built: Projects and FAQs)**
- Keep publication state, draft revision state and availability separate. Editing a draft must not change the published version. Review covers facts, both languages and media rights. FAQs and contacts follow the same draft → review → publish steps. **(not built; today a publish permission guards live records)**
- Staff sign-in uses MFA, throttling, personal accounts and server-side permission checks. **(built)** Revealing a lead's phone number needs a real permission check, not just a hidden button. No export, bulk messaging or CRM pipeline.

## States

| Situation | Expected behaviour | Status |
| --- | --- | --- |
| Invalid field or missing permission | Text error and an error summary that receives focus; keep the visitor's entries and checkbox choice | Built |
| Sending | "Sending…" label, button disabled; the server must also block duplicates | Built (label and disable) |
| Network or server failure | No receipt; keep entries; offer retry | Not built (no real submission yet) |
| Success | Confirmation, chosen project, visitor's number shown separately from the business contact | Built as demo |
| AI outage or quota reached | Plain message, contact and inquiry options, browsing continues | Not built |
| Media fails | Retry plus photo and text fallback; a way back | Partly: the panorama shows an error message; no retry button yet |
| No published projects | "Project information is being updated" with a contact path | Built |
| Page not found | "Page not found" with links home and to projects | Built |
| No inquiries yet | "No inquiries yet" in the staff inbox | Not built |
| Staff access denied | Explain, offer a way back or sign-out, show nothing private | Built (Django admin) |
| Unsaved staff edit | Warn before leaving: Stay or Discard | Not built |
| Staff save or publish succeeds | Say exactly what happened: "Draft saved" or "Revision published" | Not built (no drafts yet) |
| Invalid or expired MFA code | Explain, allow a throttled retry, offer recovery; never reveal whether an account exists | Built (two-factor package) |
| Password or MFA recovery | Neutral confirmation, single-use expiring process, named owner | Recovery codes built; owner not named |
| Retention or deletion | Restricted action with confirmation and audit, following approved policy | Not built |

Board 14 shows the main feedback and failure patterns; this table covers the rest. Test the behaviour itself, not just the wording.
