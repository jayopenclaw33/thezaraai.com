# TheZaraAI Site Cleanup — Master Backlog

Date: 2026-08-10 · Repo: `/Users/jaxs./Documents/Claude/Projects/theZaraAi/.git-clone` · Working tree: `feat/atelier-redesign` @ acb04fc

---

## A. Executive summary

The audit found 30 issues (10 P0, 9 P1, 8 P2, 1 P3) across legal, SEO, mobile, funnel, content, performance, analytics, and design consistency. Reconciliation against the repo shows the unpublished `feat/atelier-redesign` branch **already resolves roughly a third of the P0/P1 load** — mobile navigation, accessibility landmarks and contrast, the $750 JSON-LD lie, unattributed testimonials, performance (measured LCP ~1.1s mobile on the redesign vs 11.7s live), and the editorial design system on the homepage.

What remains, and what this run does, splits cleanly into six parallel lanes with strict file ownership:

1. **legal** — rewrite the terms of service (it still sells a $40/mo subscription business that no longer exists) and retheme five dark legal pages.
2. **blog** — kill the four `/index-modern.html` 404 navs, fix three dead journal cards, bylines/dates/schema, citation pass, retheme 14 dark article templates.
3. **products_guide** — retheme `/products/` and `/guide/` off neon-dark onto the editorial system, copy preserved.
4. **course_links** — retheme `/free-agent-course/`, `/fire-your-todo-list/`, `/links/` off purple-dark; noindex `/links/`.
5. **pricing_homepage** — on the branch homepage only: remove all hour-count framing, reorder the engagement chapter retainer-first, restore JSON-LD Offers that exactly match visible prices.
6. **seo_assets** — sitemap corrections (add /checklist/, drop /links/), `/index-modern.html` redirect stub, image optimization in `assets/`.

**Branch situation (verified):** `feat/atelier-redesign` was cut from c496f96, which IS local main's tip; `git log HEAD..main` is empty, so a future merge is a guaranteed fast-forward. Caveat: **origin/main is one commit behind local main** — the c496f96 pricing commit ($325/mo hosting line, weekly Operations calls) has not been pushed, so the live site may not show it. Pushing and merging are Jax's calls; **no agent runs checkout/switch/commit/push/stash**.

**Authorized price list (the only dollar figures allowed anywhere):** Starter Agent $325 one-time · Integrated Agent $789 one-time · care plan $197/month · Reconnaissance $1,424/month · Operations $3,026/month · Command $8,010/month · hosting & security $325/month on Reconnaissance and Operations, included in Command. (Ancillary digital products: $27/$47 on /products/ and /links/, $297 on /fire-your-todo-list/ — a separate product line, kept as-is.)

---

## B. Already resolved on the unpublished redesign branch

These audit findings are fixed in the working tree (`feat/atelier-redesign`) and need **no work this run** — only Jax's merge/publish decision:

- **Mobile navigation (P0)** — hamburger with `aria-expanded`/`aria-controls`, 11-link drawer, Escape-to-close, focus return (index.html ~950–967, 2122–2132). Main has none.
- **Mobile sticky action bar** — `.mobile-cta` "Book 15-min call" + "Get the manual", 46px targets, cookie-banner/drawer aware.
- **$750 "Agent Build" JSON-LD contradiction (P0)** — removed on branch (main-only bug). Note the removal also dropped correct retainer Offers; the pricing_homepage lane restores them this run.
- **Unattributed testimonials** — "Sarah M."/"Richard K."/"Tyler B." quotes (with banned word "seamless") deleted; replaced by a verifiable evidence chapter.
- **`<main>` landmark, skip link, focus rings, tablist keyboard support, labels, one h1, prefers-reduced-motion** — the bulk of the a11y-remediation item, on the homepage.
- **Contrast** — body accent moved to `--rose-deep #9B5E4A` (4.86:1 AA).
- **Performance (P0 mobile LCP)** — zero JS libraries, one lazy raster image, measured LCP 928ms desktop / 1088ms mobile, CLS ≤0.04. The 11.7s live LCP is a main-branch problem the redesign eliminates.
- **Homepage copy rules** — no banned vocabulary, no invented results.
- **Editorial design system on the homepage** — cream/navy/terracotta, Cormorant Garamond + Inter, no neon/purple/emoji/badges.
- **Integrations preserved** — verified this run: 2 forms-api endpoint refs, 2 Turnstile sitekey instances, 2 honeypots, 6 UTM'd Calendly links, 2 `tza_cookie_consent_v1` refs.

Stale audit claims corrected by reconciliation: the forms already POST via fetch with Turnstile (audit's GET-to-#faq claim is outdated); sitemap.xml is **not** 0-byte (3,819 B, 30 URLs, valid — verified again this run).

---

## C. This run — work by lane

File-ownership rule: each lane edits ONLY its listed paths. No lane runs any git state command (checkout/switch/commit/push/stash). All lanes: editorial design system only; no banned vocabulary; no statistic without a source link; no invented prices, results, or citations.

**Canonical nav spec (all lanes implementing navs):** labels — Services, Assessment, Process, **Pricing** (never "Engagement"), Team, Journal, Field Manual, Book a Call. From subpages, use absolute links to homepage anchors (`/#services`, `/#assessment`, `/#process`, `/#pricing`, `/#team`), `/blog/` for Journal. The pricing_homepage lane adds an `id="pricing"` anchor alias at the engagement chapter (currently `id="engagement"`, line 1696) so `/#pricing` resolves.

### Lane 1 — legal (`legal/` only)

- [ ] Rewrite `legal/terms-of-service.html` services/pricing sections: remove the $40/mo Starter plan, 10-day free trial, Growth/Scale tiers, and any Gumroad references (obsolete lines 156–157); describe the real offer — $325 / $789 fixed-scope builds, $197/mo care plan, $1,424 / $3,026 / $8,010/mo retainers, $325/mo hosting & security on Recon/Ops (included in Command) — as deliverables, never hours.
- [ ] Add a visible "Draft updated 2026-08-10 — pending legal review" notice; update the effective date on this real edit only.
- [ ] Retheme `terms-of-service.html`, `privacy-policy.html`, `cookie-policy.html`, `legal/index.html` (dark #0b0f1a) and `refund-policy.html` (dark #080b12 + neon #00e5a0) onto the editorial system matching `legal/accessibility.html`.
- [ ] Canonical nav + `<main>` landmark + skip link + heading hierarchy on each rethemed page.
- [ ] Sanity-check privacy/cookie text against actual practice (Turnstile, forms-api, `tza_cookie_consent_v1`); flag — never invent — anything unverifiable.
- [ ] Leave `privacy.html` / `terms.html` redirect stubs and the three already-editorial pages alone (nav labels only if divergent).

### Lane 2 — blog (`blog/` only)

- [ ] Repoint every `../index-modern.html` link to `/` in `5-workflows.html`, `ai-without-losing-mind.html`, `sf-to-ai.html`, `security-first-ai.html` (live 404s today).
- [ ] `blog/index.html` dead cards (lines 688/690, 702/704, 716/718): "5 Workflows" → `/blog/5-workflows.html`; the "Shadow AI" and "vCISO" cards have **no files** — replace those two cards with real existing articles (`best-ai-tools-for-beginners-2026.html`, `how-to-use-ai-for-cybersecurity.html`) using their true titles. Audit all remaining `href="#"`.
- [ ] Canonical nav on index + all 14 articles ("Pricing" not "Engagement"; Assessment present).
- [ ] Bylines (Jax Scott, linked bio), genuine dates from git history, BlogPosting JSON-LD with Person author; never Review/AggregateRating.
- [ ] Internal links: ≥3 out per article incl. one service/pricing link in the first three paragraphs, 2+ sibling links, descriptive anchors; one matched contextual CTA (Field Manual primary).
- [ ] Citation pass: every stat gets a primary-source link or is deleted; flag removals for Jax. Banned-vocabulary sweep.
- [ ] Retheme the 14 dark article templates onto the editorial system (after link/content fixes).

### Lane 3 — products_guide (`products/`, `guide/` only)

- [ ] Retheme `products/index.html` (dark + neon + purple + emoji): keep all content, $27/$47 prices, purchase links, and "Tools built by a practitioner, not a theorist"; line-SVG/text icons; editorial text labels instead of badge pills; no glow.
- [ ] Retheme `guide/index.html` and `guide/openclaw-guide.html`; preserve any capture-form behavior byte-for-byte.
- [ ] Canonical nav, `<main>`, skip link, headings; banned-word sweep; flag unsourced stats.
- [ ] No redirects this run — route disposition is deferred (depends on service-page architecture).

### Lane 4 — course_links (`free-agent-course/`, `fire-your-todo-list/`, `links/` only)

- [ ] Retheme `free-agent-course/index.html` (dark + purple + emoji): single-field email capture stays functional and byte-identical in behavior; keep URL and content.
- [ ] Assess `free-agent-course/linkedin-banner.html`: retheme if prospect-facing, minimal touch if a utility.
- [ ] Retheme `fire-your-todo-list/index.html`; keep the $297 offer exactly; no redirect this run.
- [ ] Retheme `links/index.html` minimally; keep $27/$47 links; **add `noindex,follow` meta** (sitemap removal is seo_assets' job).
- [ ] Remove all emoji/lightning bolts; banned-word sweep; flag unsourced stats.

### Lane 5 — pricing_homepage (working-tree `index.html` only, incl. inline JSON-LD)

- [ ] Verify prices against `git show main:index.html`; every authorized figure with currency + billing period stated; hosting footnote preserved.
- [ ] Remove ALL hour framing: cards lines 1799/1812/1824, FAQ line 1954 ("hours-based"), selector-JS `why` strings lines 2332/2338/2341 — convert each hour figure into deliverable-scope language (never delete the scope silently).
- [ ] Reorder engagement chapter retainer-first: three retainers as the primary ladder with outcome-led lines, builds + care plan as a secondary block, cross-linked; care plan = default next step after a build. No price changes (Jax's call).
- [ ] Restore JSON-LD Offers matching visible prices exactly (325 / 789 one-time; 1,424 / 3,026 / 8,010 USD per month) with scope descriptions, no hours, no $750; keep FAQ JSON-LD consistent.
- [ ] Add `id="pricing"` anchor alias at the engagement chapter.
- [ ] Integration counts identical before/after (2 forms-api, 2 Turnstile, 2 honeypot, 6 Calendly, 2 consent-key).

### Lane 6 — seo_assets (`sitemap.xml`, `robots.txt`, `assets/`, plus NEW root stub only)

- [ ] Sitemap: add `/checklist/`, remove `/links/` (being noindexed), verify all URLs 200 on `https://thezaraai.com` (no www), real lastmod from git history only.
- [ ] Create NEW `/index-modern.html` stub (exists nowhere — no ownership conflict): meta-refresh + canonical to `https://thezaraai.com/` + noindex.
- [ ] robots.txt: verify only; **do not** change AI-crawler permissiveness.
- [ ] `assets/`: inventory image sizes; recompress oversized in place (same filenames); generate AVIF/WebP variants alongside; write a recommendations report (preload/fetchpriority/`<picture>` swaps) for the index.html owner — do NOT edit any page HTML.

### P0/P1 items intentionally NOT in this run (single-owner rule or gated)

| Item | Why deferred | Owner / gate |
|---|---|---|
| Form failure states + form_error alerting (P0) | Touches index.html forms + needs forms-api coordination and test sends | Next index.html run, after pricing lane lands |
| Core analytics events (P0) | Parent plan schedules the analytics install as a deferred package | 30-day window |
| Hero assessment CTA + governance stat block (P1) | index.html single-owner rule; pricing lane is bounded to the engagement chapter | Next index.html run |
| Live-ops device label (P0) | Needs Jax's real-vs-illustrative confirmation first | Jax → next index.html run |
| Hero eyebrow clip at 390px (P0) | Main-branch symptom; verify against redesign branch before touching | Next index.html run (verify-first) |
| GSC / Bing verification (P1) | Needs Jax's Google/Microsoft accounts | Jax + 30-day window |
| checklist/index.html "$25M" unsourced claim | checklist/ not owned by any lane this run | Next run (one-line fix: cite or cut) |
| UTM first-touch persistence (P1) | Touches index.html forms; pair with analytics install | 30-day window |

---

## D. Founder decisions needed (nothing ships past these without Jax)

1. **Publish the redesign** — merge `feat/atelier-redesign` (fast-forward, zero conflicts) and push local main's c496f96 to origin (live site is one pricing commit behind). Rollback point: `git rev-parse main` = c496f96.
2. **Testimonial attribution** — re-approach the three quoted clients for named, measured, linkable attribution; or approve a labeled anonymized version; or document why not. Nothing on a proof page until then; nothing invented.
3. **Live-ops numbers provenance** — real (state source + refresh interval) or static (label "Demonstration · illustrative data").
4. **Legal review** — lawyer sign-off on the rewritten ToS (or explicit acceptance of the pending-review marker); confirm disclaimer + data-processing pages match actual practice.
5. **Price tests / price changes** — T1–T6 backlog (retainer-first checkout order, annual prepay, care-plan pre-select, raising the $325 Starter, transparency claim) all hers; published prices stay exactly as-is meanwhile.
6. **Entity naming** — Zara-retailer collision, the standard descriptor ("TheZaraAI, an AI automation and AI security advisory"), any two-practice naming ("AI Operations" / "Secure AI").
7. **Local SEO** — Durham/Research Triangle physical presence: real → GBP + one regional page; remote → documented skip.
8. **Account access** — Google Search Console + Bing Webmaster Tools verification requires her accounts.

---

## E. Deferred — 30 / 60 / 90 days, in priority order

### 30 days
1. **Service-page architecture** — `/ai-operations/` + `/secure-ai/` practices with sub-pages, `/vciso/`, `/build/`, `/work/`, `/about/`, `/field-manual/`, `/book/`, `/pricing/` (~25-page future sitemap). Gated on Jax's naming decision (D6). Many legacy-route redirect targets depend on this.
2. **/pricing/ + /build/ dedicated-page split** — retainer-first `/pricing/` with the security/governance comparison matrix (the one allowed navy section); `/build/` for fixed-scope builds.
3. **Analytics install** — assessment_complete, field_manual_submit, booking_complete (server-side/webhook), form_error with spike + zero-submission alerting; snake_case object_action; consent-gated behind `tza_cookie_consent_v1`; non-blocking. Plus form failure states with 5-pass/5-fail test submissions per form (tests only to jax@thezaraai.com), UTM convention + first-touch cookie passed into form payloads, RUM for LCP/INP/CLS, GSC + Bing verification, Generative AI report.
4. **Canonical host** — pick apex vs www, verify GitHub Pages redirect, self-referencing absolute canonicals, trailing-slash consistency.
5. **Remaining index.html P0/P1s** — form states, hero assessment CTA with risk-reversal microcopy, governance-gap data block (Deloitte/Accenture, every figure source-linked), live-ops label per D3, 320–430px clip verification.

### 60 days
6. **Proof program** — testimonial attribution per D2, day-60 case-study ask in post-engagement email, verifiable case pages.
7. **Legacy-route dispositions** — /products/ copy → editorial builds surface then redirect; /guide/ → Field Manual landing then redirect; /fire-your-todo-list/ referrer check then redirect or rebuild; meta-refresh + canonical stubs, single hop, redirect map in version control. Blog `.html` → `/journal/<slug>/` migration (once, single hop).
8. **Editorial calendar** — 12-week plan, four topic clusters, one first-hand piece weekly, every fourth week updates; week 4 rewrites/consolidates the commodity "best AI tools" article; the missing "Shadow AI" and "vCISO" articles are natural early entries (their demand is proven — the journal index already advertised them).
9. **Lifecycle email program** — welcome W1–W3, ops O1–O4, security S1–S4, book-a-call B1–B4, post-engagement P1–P3.
10. **Lead scoring + routing** — point values, hot/warm/cool/list thresholds, ops-vs-security routing, incident escalation rule.
11. **Organization/Person schema site-wide** + consistent entity descriptor (gated on D6); accessibility.html update after the manual keyboard/screen-reader pass.

### 90 days
12. **"State of AI Operations for SMB" flagship report** at `/report/state-of-ai-operations-2026/`, Field-Manual-gated — highest-leverage citation asset.
13. **Interactive HVAC demo** — MP4/WebM, "Demonstration · fictional data" chip, audit trail as climax, ≤150KB lazy poster.
14. **Experiment backlog E1–E12** with pre-committed decision rules + low-traffic stop rule.
15. **Four-tier measurement dashboard**, monthly review, weekly CRM reconciliation of booking_qualified.
16. **Booking pre-call qualification form** on a future `/book/` (Calendly preserved).
17. **Full technical re-audit against hard gates** — mobile ≥90, LCP ≤2.5s, a11y 100 + manual pass, zero 404s/orphans, single-hop redirects, clean Rich Results on every template; record deltas vs the 2026-08-09 baseline (mobile 68, LCP 11.7s, a11y 89).

**Standing SEO guardrails (never do):** keep robots.txt permissive to AI crawlers; never add llms.txt, AEO/GEO tooling, programmatic page farms, or inauthentic mention campaigns; no Review/AggregateRating on unattributed testimonials; FAQPage only where Q&As are visible; every schema price visible on-page.
