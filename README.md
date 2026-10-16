# SabahTrail – clickable prototype (CBMC4103, Question 2)

Two ways to give the university a **working link**:

| Option | What you get | Effort |
|---|---|---|
| **A. Host `index.html`** (this folder) | A fully interactive prototype – working toggles, geofence simulation, camera recognition animation, downloads, modals – at a permanent URL you control | 5 min |
| **B. Rebuild in Figma** (`figma_kit/`) | A native Figma prototype link (`figma.com/proto/...`), which is what the brief literally names | ~20 min, see `figma_kit/FIGMA_GUIDE.md` |

Doing **both** is ideal: put the Figma link in the report where it is asked for, and
add the HTML link in the same sentence as a "fully interactive version". Either one on
its own satisfies "prototype accessible via a link".

---

## A. Hosting the HTML prototype (free, permanent link)

`index.html` is a single self-contained file – no build step, no external libraries,
no fonts or images to upload. Any static host works.

### GitHub Pages (recommended – permanent, no expiry)

1. Create a free account at <https://github.com> (if you don't have one).
2. Click **+ → New repository**, name it `sabahtrail-prototype`, keep it **Public**,
   tick **Add a README**, click **Create repository**.
3. Click **Add file → Upload files**, drag `index.html` from this folder in, and click
   **Commit changes**.
4. Open **Settings → Pages**. Under **Build and deployment** set
   *Source = Deploy from a branch*, *Branch = main*, folder = `/ (root)`, click **Save**.
5. Wait about one minute and refresh the Pages settings page – it shows your link:
   `https://<your-username>.github.io/sabahtrail-prototype/`
6. Open the link in a private/incognito window to confirm it loads, then paste it into
   the report (Section 12.0 – the yellow placeholder) and the submission form.

Tip: a specific screen can be linked directly, e.g.
`https://<your-username>.github.io/sabahtrail-prototype/#trail` opens Trail Mode.

### Netlify Drop (fastest – no account needed to try)

1. Go to <https://app.netlify.com/drop>.
2. Drag the whole `prototype` folder (or just `index.html`) onto the page.
3. Netlify gives you a link like `https://random-name-123.netlify.app` immediately.
   **Sign up (free) to claim the site**, otherwise anonymous drops are deleted after
   24 hours. After claiming, you can rename it under *Site settings → Change site name*.

### Vercel / Cloudflare Pages / Surge

Also free for static files – drag-and-drop in the dashboard, or
`npx surge ./prototype sabahtrail.surge.sh` from a terminal if you have Node installed.

### What to write in the report

> A clickable prototype of these screens is available at **<link>** (open on a phone or
> in a desktop browser; use the left-hand panel to jump between screens).

---

## B. Figma prototype

See **`figma_kit/FIGMA_GUIDE.md`**. The six screens are exported there at 3× resolution
without a phone bezel (`screen1_onboarding@3x.png` … `screen6_offline_privacy@3x.png`),
ready to drag onto 390 × 844 frames, plus a hotspot wiring table with exact coordinates.

---

## What the HTML prototype does (for your own walkthrough / viva)

| Screen | Interactions |
|---|---|
| 1 Onboarding | language chips (BM/EN/中文 – toast confirms narration language), permission toggles with contextual consequences, **Continue** |
| 2 Home / Explore | trail cards: a downloaded pack opens Trail Mode; a missing pack shows a Wi-Fi-only download sheet with progress; bottom navigation |
| 3 Trail Mode | narration player (play/pause/restart/skip), language cycle, transcript sheet, stop list (locked/unlocked stops), **Walk to next stop** simulates GPS movement into the next geofence → narration auto-starts and a Journal entry is logged |
| 4 Identify | on-device recognition animation (confidence 0 → 92 %), shutter is disabled until ready, dark-mode status bar |
| 5 Result | About/Audio/Video/Nearby tabs, narration progress, Wi-Fi-only video notice, **Save to Journal** |
| 6 Offline packs & privacy | start/pause/resume pack downloads with live storage total, data-saver toggles with explanations, **Delete my Journal and all local data** confirmation modal (really clears the Journal) |
| + Trail Journal | counters update from the actions above; export button |

**Reset prototype** (bottom of the left panel) reloads the initial state.

### How it was built
Hand-written HTML/CSS/JavaScript in one file (~65 KB). The phone chrome, map tiles,
leaves, flower and all icons are inline SVG – nothing is loaded from the network, so the
file works offline and inside the university's LMS preview. Screens are stacked `<section>`s
switched by a tiny hash-based router (`#home`, `#trail`, …); state (stops visited, language,
packs, Journal) lives in one JavaScript object so every screen stays consistent.
The design tokens (colours, radii, 44 pt touch targets) are identical to the report
wireframes, which were drawn by `../make_figures.py` with the same values.
