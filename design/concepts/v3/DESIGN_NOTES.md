# V3 Design and Interaction Handoff

Updated: 23 October 2026, Asia/Dhaka. Direction: approved A / Open Horizon. These notes accompany the [review index](README.md), [requirements](../../../REQUIREMENTS.md) and [security plan](../../../SECURITY.md).

## Visual system and public naming

Retain the selected homepage unchanged. Extend its white surfaces, navy headings, blue actions, green availability labels, large land photographs and concise copy. Source colors remain #123B5D, #172C3D, #45596A, #165F96, #146B3A and #F6F8F4 as specified in DESIGN.md; generated pixels are not token values. Use approved original logo exports during implementation, not generated recreations or an unapproved white logo variant.

Use Project 01 and Project 02 in English; প্রকল্প 01 and প্রকল্প 02 in Bangla. Apply this vocabulary to navigation, headings, assistant cards, inquiry labels and staff content. This is display naming for two listings, not authorization for a parent-project/child-plot inventory system.

Marketing pages favor images and short headings. Keep price, both area units, location, availability and a clear next action visible. Forms, policies and staff screens use the same typography/color language with the space needed for their tasks; do not force decorative photographs into them.

Recommend self-hosted Noto Sans / Noto Sans Bengali, starting at 18px / 19px body size and generous line height. Use 44px controls, visible focus and meaningful labels. Normalize these values in an interactive implementation; scaled raster boards are not measurements or accessibility evidence.

## Page and view structure

Home → Projects → Project 01 or Project 02 → inquiry or AI. Gallery and Virtual Site Visit can be entered from Home or the current project's media area. About, Contact, Privacy and Terms remain directly reachable.

The Gallery board specifies the expanded view and lightbox for the requested Gallery section. It does not require a separate CMS or a new permanent page route: a section expansion/overlay can implement it. If a separate route is preferred later, keep the same content and return paths. Video/360° is a shared media view, not an additional marketing navigation item. This avoids silently adding unrelated pages from the original broad feature list.

There are no customer accounts, appointments, reservations, payments, customer uploads, ROI tools, blog or career pages in this agreed launch scope. The staff sign-in is exclusively for company staff.

## Facts and imagery

| Identity | Illustrative media | Sample facts |
| --- | --- | --- |
| Project 01 | Green grass with white corner posts; distinct ground, wider and aerial concept views | 3 katha / 2,160 sq ft; total ৳45,00,000 |
| Project 02 | Sandy ground with low boundary wall; distinct ground and boundary views | 5 katha / 3,600 sq ft; total ৳75,00,000 |

These examples establish neither an actual listing price nor a conversion rule. Every land image is generated illustration, not verified property evidence. Replace all sample locations, availability and media with company-approved facts and licensed actual assets. Do not fabricate road width, approvals, title, possession date, distances or business contacts.

Keep the landscape hero separate from listing identity. Reuse a property thumbnail only when identifying the same record; use actual alternate photographs for its gallery. About uses an illustrative planning context. Form, receipt, legal and failure states do not need decorative land photos.

Location blocks show a pending-data placeholder, not a verified map. Enable an external location link only after staff approve the destination. A button drawn in a mockup does not authorize publishing an invented link.

## Responsive and bilingual behavior

The boards cover principal desktop layouts and representative English/Bangla mobile screens, as V1/V2 did. They do not contain a separate raster of every page at every viewport in both languages. The same component rules apply throughout: stack columns in reading order, keep essential facts visible, make forms full width on phones and let supporting pages reflow to a single readable column.

Language switching preserves the selected project and view. All controls, validation, status announcements, disclosure and policy text require human-approved translation. ASCII numerals are a design convention for these samples, pending native-user review. Confirm Bangla glyphs and longer labels at 320 CSS pixels and zoom; do not infer linguistic accuracy from a generated raster.

Home uses one primary hero action. Mobile menus need a visible close control, sensible focus order and focus restoration. Launchers and action bars must not cover controls, content, keyboard focus or device safe areas. No chat popup opens automatically.

## Gallery and media behavior

Gallery opens a selected image with its project/caption, previous/next, a visible close action and a return path. Keyboard arrows may supplement labeled controls; Escape closes and returns focus to the originating thumbnail. Provide meaningful alternative text, no automatic slideshow and no trap when images fail.

Video and panorama load after explicit selection. Keep project identity visible when switching media modes. Video needs native controls, captions and transcript as applicable. A 360° panorama rotates the supplied view; it is not a movable 3D model or live location feed. Start without auto-rotation. Provide zoom, movement, fullscreen exit, return-to-project and photo/text alternatives. Do not intercept normal page scrolling indefinitely on phones.

## AI and inquiry boundary

Show AI identity and external-service disclosure before chat, with a close/back path and a non-AI contact alternative. Use approved public project facts and application-rendered authoritative cards. Keep replies concise. The model cannot see staff data, unpublished content or inquiries.

Inquiry collection is a separate form, reachable without using chat. Fields: optional name, required callback phone, selected project and optional short message. Permission starts unchecked and is specific to responding to this inquiry; do not imply marketing consent. Include the actual privacy notice and recipient before production use.

The form's name, phone and message never become AI payload fields. A visitor might type private information into free-text chat; disclosure, screening, limits and provider review remain necessary as described in SECURITY.md. Do not infer a proven privacy boundary from these pictures.

Submission confirmation appears only after successful storage. It confirms an inquiry, not a booking, sale or callback deadline. Label the visitor's masked number as “Your submitted number” and keep the approved business contact separate. Pending contact placeholders must not be published as active phone actions.

Normalize generated UI details during implementation: hide or quiet the Ask AI launcher while its panel is already open; use one consistent project-detail template across the two records; and preserve the visitor's explicit permission choice after recoverable errors. The recovery board's unchecked failure example is an illustrative state, not an instruction to erase a prior affirmative choice. Initial forms remain unchecked. The MFA invalid-code message is a failure variant, not the default challenge. Draft-policy sample wording must be replaced by an accurate company-approved notice.

## Staff workflows

Use a compact staff shell: Projects, Inquiries, FAQs and Public contacts. These boards describe focused Django-admin customization, not a commitment to build a separate dashboard application. Active navigation matches the current workflow. No public marketing navigation/footer is needed inside staff tools.

Keep public publication state, draft revision state and availability distinct. Editing a draft revision does not remove an existing published version. Publication review covers facts, both languages and media rights. FAQ and business-contact edits also have draft/review/publish stages. Exact approver permissions remain a company decision.

Staff authentication needs MFA, recovery, throttling, individual accounts and server-side authorization. Inbox data is synthetic and masked on the boards. Revealing a phone requires actual permission enforcement; hiding a button or masking pixels is insufficient. No export, bulk messaging or CRM pipeline is introduced. Deletion/retention controls depend on approved roles and privacy rules.

## State specification

| Trigger | Intended response |
| --- | --- |
| Invalid form field or missing permission | Text error and focusable summary; focus moves to the summary; preserve useful values and the visitor's explicit checkbox choice |
| Submission in progress | Sending label and disabled repeat-submit action; announce status; server also prevents duplicate storage |
| Submission network/server failure | No receipt; keep values in the current screen, show Retry/Edit, permit resubmission safely; no promise of persistence after reload |
| Submission success | Announce confirmation, selected project and visitor-submitted contact separately from business contact |
| AI outage or quota | Clear temporary-unavailability message, contact/inquiry alternatives and continued browsing; no invented retry countdown |
| Media fails or unsupported viewer | Retry and photo/text fallback; exit/back remains available |
| No published projects | “Project information is being updated” with contact path; no draft records or stale availability claims |
| No staff inquiries | “No inquiries yet”; keep navigation and any permitted status controls; no fake sample records in production |
| Staff access denied | Explain lack of access, show a permitted return/sign-out path and expose no private content |
| Unsaved staff edit | Warn before navigation; Stay/Discard; do not silently publish or lose the draft |
| Staff save/publication succeeds | Announce the precise outcome: Draft saved or Revision published; preserve distinct availability state |
| Invalid/expired MFA | Explain failure, allow safe retry under throttling and offer recovery; do not expose whether arbitrary staff identities exist |
| Password/MFA recovery | Neutral request confirmation, expiring single-use recovery process and clear return path; exact operational owner must be named |
| Retention/deletion action | Restricted authorized action with confirmation/audit; apply approved policy and backup cleanup rather than an unapproved default |

Board 14 visualizes principal feedback/failure patterns; this table specifies additional states without requiring a separate raster for each one. During implementation, test these behaviors rather than copying messages without their data/control boundaries.

## Review and implementation boundary

The complete V3 pack is ready for page-by-page review against the approved homepage direction. Only that homepage direction has already been selected by the user; the new screens have not automatically received final approval. Real content, native translation, roles, contacts, privacy rules, hosting and budgets remain company inputs.

Static visual review cannot prove keyboard/screen-reader behavior, exact contrast, security, media playback, performance or legal compliance. No application tests apply yet. After design review and the user's instruction to implement, begin the PLAN.md thin functional path: one published project in both languages, editable by permitted staff, with environment separation and relevant checks from the first code change.
