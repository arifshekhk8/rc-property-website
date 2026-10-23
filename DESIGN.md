# UI and UX Design Direction

Last updated: 23 October 2026, Asia/Dhaka. Status: complete V3 design pack ready for review; no interface has been implemented.

The first local implementation is in [app/](app/README.md). It uses custom CSS and generated sample media while actual project assets are pending. Gallery/lightbox and media previews are interactive; AI and inquiry persistence remain explicit preview states. The fourteen V3 design boards remain unchanged.

## Complete V3 design pack: Open Horizon

The user selected **A / Open Horizon as final for now**, following the manager's feedback that V1 was broadly acceptable but too wordy. The [complete V3 pack](design/concepts/v3/README.md) now extends that homepage into fourteen selected review boards, covering every agreed public page type and principal staff flow, with expanded gallery/media views, mobile/Bangla examples and recovery states. Public listing names are **Project 01** and **Project 02**, with Projects navigation and consistent wording in actions/captions. This is display naming; it does not introduce a project/subplot hierarchy. The homepage, [earlier candidates](design/concepts/v3/archive/homepage-options/README.md), V1 and V2 remain preserved.

Keep the selected cinematic hero, white sections, navy typography, blue controls and green availability labels. Reduce prose while retaining price, both area units, location, availability and next action. Gallery shows still images; Virtual Site Visit previews the already-required walkthrough and 360° panorama through user-initiated controls. The [V3 handoff](design/concepts/v3/DESIGN_NOTES.md) specifies responsive/localization rules, media behavior, consent separation, staff draft/publication states and recovery cases. All page types have designs for review; exact responsive behavior, final translations and interactive checks belong to implementation. Only the homepage direction has already been selected; new boards await page-by-page review.

## Previous visual proposal: V2

The user requested a separate improved version using the bright, clearly bounded Dhaka/Purbachal-inspired plot imagery direction. The [V2 review pack](design/concepts/v2/README.md) contains eleven boards: the core public/staff screens, a dedicated Bangla mobile journey, and validation/focus, sending, AI-outage and access-restricted states. V1 remains unchanged.

V2 separates hero text from its main image, gives landscape listing photos more room, emphasizes total price and both area units, and uses a consistent compact staff workspace. Policy pages have no incorrect Home selection. The user rejected the first V2's repetitive imagery; the [imagery correction](design/concepts/v2/imagery-revision/README.md) now supplies eight revised boards with distinct hero/property/context imagery, alternate camera views and fewer decorative photographs. The receipt-phone label also distinguishes the submitted number from business contact information. The [handoff notes](design/concepts/v2/DESIGN_NOTES.md) record remaining consistency details and behavior, including one mobile hero action, consistent brand exports and separate publication/availability states.

The land visuals are labeled AI illustrations. They are invented examples inspired by the requested location, not recent verified photos or accurate views of the company's two plots. Replace them with approved actual media for publication. Exact translated/responsive variants and remaining interaction states still require refinement; static designs do not prove accessibility or security.

## Preserved first visual concept

The [version 1 review pack](design/concepts/v1/README.md) contains nine selected raster boards covering Home, Available Plots, plot detail/media, About, Contact, Privacy, Terms, the AI disclosure/chat/inquiry flow, and staff sign-in/MFA/content/inquiry/FAQ/contact workflows. Core public pages include desktop/mobile examples, with Bangla shown in listing and chat screens. The [full prompt set](design/concepts/v1/PROMPTS.md) records the built-in image-generation work and targeted refinements.

These are proposals, not approved designs or working pages. Photographs, prices, measurements, maps, descriptions, availability, and masked leads are design samples. The company still needs to supply the real plot media/facts and approved business contacts. Full translated/responsive variants, component specifications, and error/loading/focus/accessibility states remain design-refinement work. The review pack records normalization notes for the staff shell and shared navigation.

## Direction

Create a welcoming, premium property website through clear typography, generous spacing, authentic imagery, restrained color, and predictable controls. Design around the local buyer's questions: where the plot is, how large it is, what it costs, what is actually available, and how to speak to a responsible person.

The small catalog should make those answers immediately visible. Use Home, Projects, Gallery, About, and Contact, plus a clearly labeled বাংলা / English control. Gallery links to the requested homepage section; a separate gallery page is not yet confirmed. Privacy and Terms belong in the footer. Use Project 01 / Project 02 as the current public names, including inquiry labels and assistant cards.

## Logo analysis

The supplied logo combines an RC monogram with a roof/window shape, blue lettering, and several greens. The PNG is 7284 × 1526 pixels with transparency. The Illustrator file is PDF-compatible and places the logo on a large A4 artboard. Future web exports should be optimized copies with appropriate bounds; do not modify the originals.

Pixel sampling of the supplied PNG produced these dominant colors and calculated sRGB contrast ratios against white:

| Logo color | Sample | Contrast against white |
| --- | --- | --- |
| Blue | #2287C8 | 3.91:1 |
| Light green | #86C44F | 2.10:1 |
| Lettering green | #1DAF4C | 2.88:1 |
| Darker green | #189C49 | 3.57:1 |

These are sampled asset colors, not an approved brand specification. Preserve the logo while selecting darker interface colors for ordinary text and white button labels. Logo text is exempt from the WCAG text contrast requirement; that exemption does not apply to navigation or controls.

The full logo is wide. Give it sufficient space in the header and test company-name readability on phones. A compact symbol export is a proposal requiring brand approval; retain an accessible full company name if it is used.

## Proposed interface palette

| Purpose | Color | Verified contrast on white |
| --- | --- | --- |
| Main text | #172C3D | 14.34:1 |
| Secondary text | #45596A | 7.27:1 |
| Headings / dark blue | #123B5D | 11.61:1 |
| Links / primary buttons | #165F96 | 6.75:1 |
| Positive accent / green buttons | #146B3A | 6.57:1 |
| Main surface | #FFFFFF | Surface only |
| Soft background | #F6F8F4 | Main text contrast 13.42:1 |

Use the light logo green as decoration, not small text on white. All hover, focus, disabled, validation, and overlay states still need independent checking. Label availability with words as well as color. Select border and focus colors with adequate non-text contrast; a pale decorative divider is not a substitute for an input boundary.

## Typography

Recommend self-hosted Noto Sans for English and Noto Sans Bengali for Bangla, subject to a native-reader review. Include their licenses. Use only needed weights, with system fallbacks and font-display swap. Avoid runtime font requests to third parties.

Start with 18px English body text and 19px Bangla body text. Use line-height around 1.6 for English and 1.7 for Bangla, then verify actual glyphs and conjuncts. Use responsive headings around 30–44px on phones and 40–56px on desktop. Body copy should stay within approximately 60–70 characters per line where practical.

Keep text selectable. Use plain language and short paragraphs. Show clear currency and area labels in both languages; test BDT, ৳, commas, decimal values, and Bangla numerals together. Machine translations require human approval before publication.

## Page composition

Home: a striking photographic hero, a short heading approved by staff, and one clear plot-browsing action. Follow with the two listings, Gallery, a Virtual Site Visit preview, and concise contact options. Avoid large introductory paragraphs and repeated explanatory labels. The homepage candidates explore different arrangements while keeping essential plot facts. Do not invent testimonials, statistics, awards, or approval badges. Use approved real media for publication.

Listing cards: consistent image proportions, location, area, price, textual availability, and a single obvious “View Details” link. With two items, show both; omit a search bar, sorting menus, pagination, and filter drawers.

Plot detail: title and locality, photo gallery, prominent price/area/status, concise specifications, description, media, nearby facilities, location, and a clear interest/contact action. A desktop summary can sit beside the content; on mobile keep facts in reading order. Do not hide essential details behind tabs.

Photos, rendered concepts, and proposed developments must have distinct labels. Prefer a current photo and capture date where provided. Describe location with text even when a map or panorama is available.

## Video and panorama

Use a poster and explicit Play control for video, with captions and a transcript where needed. Do not autoplay or download full video on initial page load.

Use a self-hosted Pannellum viewer for the administrator's compatible panorama. A 360° panorama provides rotational viewing, not a movable architectural 3D model. Label the feature accurately. Verify the supplied projection and dimensions before committing the viewer setup.

Load viewer code and large imagery only after “Explore 360° View” is selected. Keep rotation off initially. Provide visible instructions and controls for changing view, zooming, and leaving fullscreen. Test touch and keyboard behavior, prevent scroll trapping, and provide photos/text when WebGL or navigation is unavailable.

## Assistant and lead capture

Use the selected homepage's “Ask AI” launcher; where a fuller label is needed, use “Ask about a project.” Opening chat is voluntary; do not open it automatically. On phones, an expanded panel may use most of the screen, but must have a visible close control and restore focus when closed. The launcher and any contact bar must not obscure content, keyboard focus, or safe-area insets.

Identify it as an AI assistant in both languages. Explain its information source and limitations briefly. Give starter questions, support typed questions, and keep responses short. Show authoritative plot cards and staff contact from application data rather than inventing contact information.

Offer a separate labeled form for name, phone, interested plot, and optional short message. Recommend an optional name, required callback number, and preselected current plot. State the recipient and purpose before submission; permission is not preselected. Confirm successful storage, avoid duplicate submissions, and preserve entered fields on recoverable validation errors. Do not promise a callback time until staff approve it.

## Accessibility and usability acceptance

Target [WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/). Check text contrast of 4.5:1 for ordinary text and 3:1 for eligible large text, plus applicable non-text contrast. The project proposes 44px minimum touch controls, exceeding the 24px AA minimum in applicable cases.

Provide semantic landmarks, one clear main heading, skip navigation, visible focus, accessible names, meaningful image alternatives, labels, and understandable errors. Support keyboard navigation, screen-reader announcements, text resizing, and reflow at the WCAG equivalent of 320 CSS pixels. Respect reduced motion. Prevent modals, chat, navigation, and media from trapping focus.

Test both languages on Android Chrome and iPhone Safari, including zoom, long translated labels, the on-screen keyboard, orientation changes, slow connections, and failed media/AI requests. Ask three to five representative users to find a price, locate the plot, open media, and contact staff. Record confusion and fixes.

## Reference websites and what to study

| Reference | Useful direction | Application to this project |
| --- | --- | --- |
| [Shanta Holdings](https://shantaholdings.com/) | Property-focused imagery and featured project presentation | Give the two plots strong visual attention and a clear detail path |
| [bti](https://btibd.com/) | Listing cards expose location and key specifications | Make price, area, location, and status easy to compare without extra clicks |
| [Bay Developments](https://baydevelopments.com/) | Project storytelling and prominent inquiry paths | Pair concise descriptions with purposeful images and obvious contact |

Recommend Shanta as a visual starting reference and bti for information hierarchy, adapted to a much smaller catalog and readable bilingual typography. These are design judgments based on public page content and presentation references, not endorsements of their accessibility or security. Their complete mobile layouts and performance have not been audited in this session. Do not copy their text, photographs, or branding.

## Sources

[Bootstrap accessibility guidance](https://getbootstrap.com/docs/5.3/getting-started/accessibility/) confirms that default components/colors still require implementation review. [Pannellum documentation](https://pannellum.org/documentation/reference/) describes viewer options. [Noto Sans Bengali](https://fonts.google.com/specimen/Noto+Sans+Bengali) is the proposed font source.
