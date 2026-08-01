# The Intelligence Atelier — redesign handoff

Branch: **`feat/atelier-redesign`** · commit `8d8b49e`
Status: **not published.** `main` and the live site are untouched.

---

## 1 · Changed files

| File | Change |
|---|---|
| `index.html` | Rebuilt. 2,949 → 2,444 lines. |
| `assets/og-atelier.png` | New. 1200×630 Open Graph image, 159 KB. |
| `REDESIGN-HANDOFF.md` | New. This document. |

Nothing else was touched. `blog/`, `legal/`, `products/`, `guide/`, `checklist/`,
`free-agent-course/`, `links/`, `assets/*`, and `CNAME` are unchanged.

---

## 2 · Information architecture

The old page ran 10 sections with overlapping explanations (pricing appeared in the
engagement section, the FAQ, and the JSON-LD; services were described in the hero, the
services grid, and again in process). The rebuild is 11 chapters, each with one job:

| # | Chapter | Anchor | Why it exists |
|---|---|---|---|
| 1 | Hero — operational promise | `#top` | State the offer and show a live-feeling artifact |
| 2 | Signature demonstration | `#demonstration` | Prove the workflow before asking for anything |
| 3 | Three practices | `#practices` | What we do, as working exhibits |
| 4 | Outcomes & evidence | `#evidence` | What you hold at the end |
| 5 | Process | `#process` | Five stages, decision gate at each |
| 6 | Selected demonstrations | `#work` | System patterns, labeled as demonstrations |
| 7 | Engagement & pricing | `#engagement` | Selector → recommendation, then tiers |
| 8 | Field Manual | `#handbook` | Low-intent capture |
| 9 | Founder & Zara | `#practice-team` | Who and what you are working with |
| 10 | FAQ | `#faq` | Objection handling |
| 11 | Conversion | `#contact` | Book the call, or send a message |

The old `#testimonials` section was removed — see §8.

---

## 3 · Preserved integrations

Verified present and byte-identical in behaviour:

- **Cloudflare Turnstile** — script tag, both widgets, sitekey `0x4AAAAAADYpApsWgjxZo3_L`
- **Honeypots** — both `input.hp-honey[name="website"]`, same off-screen CSS
- **forms-api endpoints** — `/api/field-manual` and `/api/schedule-call` on
  `forms-api-jax-1509s-projects.vercel.app` (Resend + Turnstile verification + rate limiting)
- **`postToBackend()`** — unchanged, including the `data.ok !== false` contract
- **Field Manual PDF** — same direct-download trigger on success
- **Cookie consent** — same `tza_cookie_consent_v1` key, so existing visitors are not re-prompted
- **Calendly** — `https://calendly.com/thezaraai/discovery-call`, 5 links, all with UTMs
- **Reduced-motion** — expanded, not just preserved

Two improvements to the forms: `autocomplete` attributes were added, and the failure path
now renders an inline `role="alert"` message instead of `alert()`.

---

## 4 · Performance

Measured with Chrome DevTools Protocol against a local server.

| Metric | Desktop 1440 | Mobile 390 (4× CPU throttle, ~1.6 Mbps) | Threshold |
|---|---|---|---|
| LCP | **928 ms** | **1088 ms** | < 2500 ms |
| FCP | 928 ms | 1088 ms | < 1800 ms |
| CLS | **0.0019** | **0.0394** | < 0.1 |

| Asset | Raw | Gzip |
|---|---|---|
| `index.html` before | 107.6 KB | 25.6 KB |
| `index.html` after | 155.1 KB | **35.5 KB** |
| `og-atelier.png` | 159 KB | crawler-only, not on the critical path |

The page grew ~10 KB gzipped and gained a seven-step demonstration, three SVG practice
diagrams, a scroll-drawn process path, and an engagement selector.

- **Zero animation libraries.** No GSAP, Motion, Three.js, Lottie, or jQuery. All motion is
  native CSS plus `IntersectionObserver` and two `requestAnimationFrame` scroll handlers.
- **Zero WebGL/Canvas.** Every visualization is DOM/CSS/SVG, so it is inspectable, styleable,
  and screen-reader labelable.
- **One raster image on the page** (`jax-headshot.jpg`), lazy-loaded with explicit dimensions.
- **Blocking third parties:** Google Fonts CSS (preconnected) and Turnstile (`async defer`).

**Caveat:** measured from `127.0.0.1`, so document latency and CDN behaviour are excluded.
Real-world LCP will be higher. Run Lighthouse against the live origin after publishing —
that number is the one that counts, and it cannot be obtained from a protected preview.

---

## 5 · Accessibility

- **Contrast.** The old pale accent (`--rose` #B87560, 3.47:1 on ivory) was used for body-size
  text. All body-size accent text now uses `--rose-deep` (#9B5E4A, **4.86:1** — AA). `--rose`
  is retained only for large text, rules, and UI fills, where the 3:1 threshold applies.
  On navy, `--rose-light` measures 6.99:1 and cream 13.3:1.
- **Demonstration.** Real `role="tablist"` with roving `tabindex`, `aria-selected`,
  `aria-controls`, and Arrow/Home/End key support. The caption is `role="status"`
  `aria-live="polite"`, so step changes are announced.
- **Motion.** `prefers-reduced-motion` disables all transitions, converts the pinned theatre
  to stacked panels, renders the process path fully drawn, and stops the Zara orbits. Verified
  by re-running the whole QA suite under `--force-prefers-reduced-motion`: every interaction
  still works.
- **Keyboard.** Skip link, visible focus rings on all interactive elements (`--rose-deep` on
  light, `--rose-light` on dark), Escape closes the mobile drawer and returns focus.
- **Structure.** One `<h1>`, every form control has a `<label for>`, all images have `alt`,
  SVG diagrams carry `role="img"` with descriptive labels.
- **Tap targets.** No interactive control below 44 px. The demo step rail uses a 3 px visual
  bar with a 44 px hit area via an `::after` overlay.

---

## 6 · QA performed

Headless Chrome, scripted, run at 1440×900, 1280×800, 768×1024, 390×844, 375×812.

| Check | Result |
|---|---|
| Broken in-page anchors | 0 |
| Console errors | 0 (excluding expected Turnstile 110200 — see §9) |
| Failed network requests | 0 |
| Horizontal overflow | none at any of the 5 widths |
| Calendly links correct + UTM'd | 5 / 5 |
| Turnstile widgets / honeypots | 2 / 2 |
| Form labels | all present |
| Demonstration | 7 steps, panel + tab + rail + caption stay in sync |
| FAQ accordion | opens, `aria-expanded` correct |
| Engagement selector | returns recommendation, reveals CTA |
| Services theatre | all 3 practices reachable by scroll, click, and keyboard |
| Case-study panels | expand, `aria-expanded` correct |
| Mobile drawer | opens, 11 links, Escape closes |
| Cookie accept / decline | banner dismisses, key written |
| Analytics gating | events blocked before consent, fire after |
| Reduced-motion | full suite re-run, everything functional |

Two real bugs were found and fixed during QA:

1. **Mobile overflow (453 px page on a 375 px viewport).** The demo sidebar is a grid item,
   and grid items default to `min-width: auto` — so its `nowrap` tab strip widened the whole
   page instead of scrolling inside itself. Fixed with `.app-body > * { min-width: 0 }`. A
   second contributor was `.btn { white-space: nowrap }` on the long CTA label; buttons now
   wrap below 600 px.
2. **Process path rendered as an 18 px bar.** The SVG used `preserveAspectRatio="none"` across
   the full container, which scaled the 1.5 px stroke horizontally by ~12×. Fixed by
   constraining the SVG to the 92 px gutter and adding `vector-effect="non-scaling-stroke"`.

---

## 7 · Analytics

No tracker is installed on this site. Rather than install one you did not choose, events run
through `window.zaraTrack(event, params)`, which is consent-gated on
`tza_cookie_consent_v1` and forwards to `gtag`, `dataLayer`, or `plausible` — whichever
exists. Verified: nothing is emitted before consent; events flow immediately after.

Wired: `hero_book_call_click`, `hero_demo_start`, `demo_step`, `demo_complete`,
`service_practice_view`, `case_study_open`, `pricing_recommendation_complete`,
`field_manual_start`, `field_manual_submit`, `final_book_call_click`, `contact_submit`,
`book_call_click`.

The funnel metric worth watching is `demo_complete` against `final_book_call_click`.

---

## 8 · Content integrity — please read

**The three testimonials were removed and not replaced.**

The live site carries quotes attributed to "Sarah M.", "Richard K.", and "Tyler B." with
five-star ratings and hard claims: *"saved our team 15+ hours a week"*, *"paid for itself in
the first week"*, *"3 hours per client to 15 minutes"*, *"found three shadow AI tools"*.

Your brief said not to fabricate testimonials or invent time-saved and security outcomes. I
cannot verify these, and I could not rewrite them without fabricating client speech. So I
left them out and built the evidence chapter on things that are verifiable: the artefacts
every engagement produces, your actual credentials, and a standing offer of references.

**This is your call, and it is easily reversed.** If they are real and approved, tell me and
I will restore them in the anonymized role/sector form your brief specifies — without the
star ratings, which imply a public review platform you are not on. If they were placeholders
from a template, they should stay gone: unsubstantiated testimonial claims are exactly what
the FTC endorsement guidance covers.

The evidence chapter states plainly that no customer counts or outcome numbers are published
and invites the visitor to ask on the call. For a boutique practice selling judgement, that
reads as more confident than unverifiable statistics.

---

## 9 · Open items

1. **Founder portrait.** `assets/jax-headshot.jpg` is a bright pink-to-yellow gradient
   portrait. Against the ivory/navy/terracotta system it is the single loudest element on the
   page and works directly against the "expensive boutique" goal. I did not alter or replace
   it — that is a decision about your own likeness. A neutral-background portrait, or the
   short founder video your brief mentions, would lift this chapter more than any code change
   I could make.
2. **Turnstile on the preview domain.** The sitekey is domain-locked to `thezaraai.com`, so
   the preview throws `Turnstile Error 110200` and forms will not submit there. This is
   expected and disappears on the real domain. To test forms on the preview, add the preview
   hostname to the widget's allowed domains in the Cloudflare dashboard.
3. **Preview is behind Vercel auth.** The deployment returns 302 to Vercel SSO. You can view
   it logged in as `jax-1509`. To share it with anyone else, disable Deployment Protection for
   that project — I did not change that setting.
4. **`/home-services`** is still on its own branch (`feat/home-services-page`), also unpushed.
   The two branches are independent and can merge in either order.
5. **Analytics** — pick GA4 or Plausible and the events light up.
6. **`sitemap.xml`** at the repo root is still a 0-byte file.

---

## 10 · Preview

```
https://thezaraai-atelier-preview-l0vb4vv5v-jax-1509s-projects.vercel.app
```

Or run it locally, which avoids the Turnstile domain issue entirely only for layout review:

```bash
cd "/Users/jaxs./Documents/Claude/Projects/theZaraAi/.git-clone"
git checkout feat/atelier-redesign
python3 -m http.server 8899
# → http://127.0.0.1:8899/
```

---

## 11 · Deploy

The live site is GitHub Pages on `jayopenclaw33/thezaraai.com`, `CNAME` → `thezaraai.com`.
Pushing `main` publishes.

```bash
cd "/Users/jaxs./Documents/Claude/Projects/theZaraAi/.git-clone"
git checkout main
git merge feat/atelier-redesign
git push origin main
```

Then, within a few minutes of the Pages build:

- Hard-reload `https://thezaraai.com` and confirm the Turnstile widgets render with no console error
- Submit the Field Manual form with a real address and confirm the PDF downloads and the email arrives
- Submit the contact form and confirm it reaches you
- Re-scrape the Open Graph card (LinkedIn Post Inspector / X Card Validator) to pick up `og-atelier.png`

## 12 · Rollback

The redesign is a single commit touching one existing file, so rollback is one command.

```bash
# Option A — revert the merge, keep the history
git checkout main
git revert -m 1 <merge-commit-sha>
git push origin main

# Option B — restore just the old homepage, keep everything else
git checkout main
git checkout <pre-merge-sha> -- index.html
git commit -m "rollback: restore previous homepage"
git push origin main
```

The pre-redesign `index.html` is whatever `main` pointed at before the merge — capture that
SHA before merging (`git rev-parse main`) and rollback is trivial. No database, no build
step, no CDN cache to purge beyond a hard refresh.

---

## 13 · Key design decisions

**Evolved the tokens rather than replacing them.** Same ivory, ink navy, terracotta, Cormorant
Garamond, and Inter. The brand equity is in that restraint. What changed is how the tokens are
used: one accent, hairline rules, a `3.5rem` paper grid on the evidence chapter, and much more
negative space.

**Product proof before persuasion.** The old page explained the offer three times before
showing anything working. The demonstration is now chapter two, above the practices — the
visitor sees the thing operate before being asked to believe a claim about it.

**Sticky, not hijacked.** The services theatre pins with `position: sticky` over a 300vh
track. Scroll velocity, momentum, and the scrollbar all behave normally; the visitor can leave
at any moment. Below 880 px and under reduced-motion it becomes three stacked panels with the
same content and the same diagrams — not a degraded version, a different correct version.

**Etched diagrams instead of decoration.** The three practice visuals are line drawings that
carry actual information — data flow for automation, a governance stack for vCISO, a control
boundary for security. As SVG they cost about a kilobyte each, scale losslessly, restyle with
CSS variables, and carry real accessible descriptions.

**Zara is drawn, never photographed.** An abstract orbital mark, labeled "AI agent · not a
person". Your brief was explicit, and it is also the honest choice — a face on an automation
layer misrepresents what the client is buying.

**A recommendation, not a quote.** The engagement selector returns a shape and says so
plainly. Fake precision is the fastest way to lose a buyer who knows their own project is not
knowable from four dropdowns.

**Absence as a signal.** The evidence chapter states that no customer counts or outcome
numbers are published, and explains why. For a security-led practice, refusing to publish
unverifiable numbers is itself the credential.
