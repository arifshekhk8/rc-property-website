# Design

Last updated 21 November 2026.

## Status

The V3 **Open Horizon** design is built into this repo with custom CSS (`app/static/css/site.css`) and AI-generated sample media. The 14 design boards are in [design/concepts/v3/](../design/concepts/v3/README.md), and the interaction rules are in [DESIGN_NOTES.md](../design/concepts/v3/DESIGN_NOTES.md). The later "Grounded Premium" redesign was built in `rcpdl-website`, not here.

## Direction

Welcoming and premium: clear type, generous space, real imagery, restrained colour and predictable controls. Design around the buyer's questions: where is the plot, how big is it, what does it cost, is it available, and who do I talk to?

- Navigation: Home, Projects, Gallery, About, Contact, plus a বাংলা / English switch. Privacy and Terms go in the footer.
- Keep the cinematic hero, white sections, navy headings, blue buttons and green availability labels.
- Keep the copy short, but always show price, both area units, location, availability and the next action.
- Never invent testimonials, statistics, awards or approval badges.
- Label photos, renders and proposals clearly as different things. Describe location in text even when a map or panorama exists.

## Design history

| Version | Date | Outcome |
| --- | --- | --- |
| V1 | 15 Oct | 9 boards. Manager: broadly fine but too wordy |
| V2 | 15 Oct | 11 boards with brighter plot imagery. Arif rejected the repeated images, so 8 boards were corrected |
| V3 | 23 Oct | 3 homepage options; Arif chose A / Open Horizon. Full 14-board pack, built into the app the same day |

V1 and V2 are kept locally (git-ignored). Every land image in every version is an AI-generated illustration, not a photo of the real plots.

## Logo

The supplied logo (`RCPDL.png`, 7284 × 1526 px, transparent background) combines an RC monogram with a roof-and-window shape, blue lettering and several greens. The `.ai` file is PDF-compatible and sits on an A4 artboard. Web versions are optimised copies; never edit the originals.

Colours sampled from the PNG (not an official brand spec):

| Colour | Hex | Contrast on white |
| --- | --- | --- |
| Blue | #2287C8 | 3.91:1 |
| Light green | #86C44F | 2.10:1 |
| Lettering green | #1DAF4C | 2.88:1 |
| Darker green | #189C49 | 3.57:1 |

These are too light for body text or white button labels, so the interface uses darker tones. The logo itself is exempt from text-contrast rules; navigation and buttons are not. The full logo is wide, so check that the company name stays readable on phones.

## Interface palette

These match the CSS custom properties in `site.css`.

| Use | Token | Hex | Contrast on white |
| --- | --- | --- | --- |
| Main text | `--body` | #172C3D | 14.34:1 |
| Secondary text | `--muted` | #45596A | 7.27:1 |
| Headings | `--ink` | #123B5D | 11.61:1 |
| Links, primary buttons | `--blue` | #165F96 | 6.75:1 |
| Positive accent | `--green` | #146B3A | 6.57:1 |
| Soft background | `--sage` | #F6F8F4 | main text on it: 13.42:1 |

Use the light logo green only as decoration. Hover, focus, disabled, error and overlay states still need contrast checks. Availability always uses words, not colour alone.

## Typography

- Self-hosted Noto Sans (English) and Noto Sans Bengali, with licences in `app/static/fonts/`. No font requests to third parties.
- Body text is 18 px in both languages. Line height is 1.65 for English and 1.8 for Bangla.
- h1 scales from 38 to 68 px and h2 from 30 to 42 px (CSS `clamp`).
- Numbers use ASCII digits in both languages for now (৳45,00,000). A native reader should confirm this.
- All Bangla copy needs a native speaker's review before launch.

## Page layout

- **Home:** image hero with a short heading and one main button, then both listings, a gallery mosaic, the Virtual Site Visit band and the contact band.
- **Listing cards:** same image shape, location, area, price, availability and one "View project" button. No search, sorting or pagination for two items.
- **Project page:** photos, then a summary with price, area and status, shown beside the photos on desktop and below them on mobile. Then the description, location, media buttons and the inquiry button. Nothing essential is hidden in tabs.

## Video and panorama

- **Video:** poster image, native controls, captions, `preload="none"`, no autoplay.
- **Panorama:** self-hosted Pannellum. It loads only after the visitor presses "Load sample 360° view", with no auto-rotation and `escapeHTML: true`. A panorama rotates a fixed view; it is not a 3D model. Check the real file's projection and size before swapping it in.
- Always offer photos and text as a fallback.

## Assistant and inquiry

- "Ask AI" opens a dialog only when pressed. For now it explains that AI is coming and links to the projects and the inquiry form.
- The live assistant must say it is AI, in both languages, and explain its limits. Price, contact and listing cards come from app data.
- Inquiry form: optional name, required phone, the project preselected, optional message, permission box unchecked by default. Say who receives the inquiry and why before it's sent. Don't promise a callback time until staff agree one.

## Accessibility targets

Target WCAG 2.2 AA: 4.5:1 text contrast (3:1 for large text), visible focus, a skip link, landmarks, labels, clear errors, reflow at 320 px, reduced motion, no focus traps. Buttons and form fields are at least 44 px tall; check text links and the consent checkbox on touch screens. Test both languages on Android Chrome and iPhone Safari with zoom, long labels, the on-screen keyboard and a slow network. Ask 3–5 representative users to find a price, locate a plot, open the media and contact staff.

Built so far: skip link, `aria-current` on navigation, labelled dialogs, a focused error summary with `aria-invalid` and `aria-describedby` on fields, native `<dialog>` focus handling, reduced-motion CSS. Not done yet: screen-reader testing, real-device testing, an automated axe run.

## Reference sites

| Site | Learn from |
| --- | --- |
| [Shanta Holdings](https://shantaholdings.com/) | Property-focused imagery and featured projects |
| [bti](https://btibd.com/) | Cards that show location and key specs at a glance |
| [Bay Developments](https://baydevelopments.com/) | Short project stories with obvious inquiry paths |

Use them for ideas only. Don't copy their text, photos or branding. We haven't checked their accessibility or performance.
