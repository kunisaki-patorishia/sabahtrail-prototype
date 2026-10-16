# SabahTrail – Building the clickable Figma prototype (≈ 20 minutes)

Figma cannot be driven from outside its own editor, so the file has to be assembled
by hand. Everything you need is in this folder: the six screens are exported at
**3× (1170 × 2532 px)** without a phone bezel, so each one drops exactly onto a
**390 × 844** Figma frame. Follow the steps in order; the hotspot table at the end
tells you which rectangle links to which screen.

---

## Step 1 – Create the file and the frames

1. Go to <https://www.figma.com>, sign in (a free Starter plan is enough – prototypes
   and share links are included) and click **New design file**.
2. Rename the file (top-centre tab) to `CBMC4103 – SabahTrail prototype – <your name>`.
3. Press **F** (Frame tool). In the right-hand panel choose a phone preset – pick
   **iPhone 14 & 15 Pro (393 × 852)** – then type **390** and **844** into the W/H
   boxes so the frame is exactly 390 × 844.
4. Rename the frame (double-click its name on the canvas) to `1 Onboarding`.
5. Duplicate it five times (**Ctrl/Cmd + D**) and rename the copies:
   `2 Home`, `3 Trail Mode`, `4 Identify`, `5 Result`, `6 Offline & Privacy`.
   Space them out left-to-right in that order (select all six → right panel →
   **Tidy up** icon, or set the gap to 80).

## Step 2 – Drop in the screens

1. Drag `screen1_onboarding@3x.png` from this folder straight onto the `1 Onboarding`
   frame. Figma imports it as an image fill 1170 px wide – with it selected set
   **W = 390, H = 844, X = 0, Y = 0** in the right panel (or press
   **Shift + A** → it snaps to the frame). It should fill the frame edge-to-edge.
2. Repeat for the other five PNGs → frames 2–6.
3. In the Layers panel, **lock** each image (right-click → Lock/Unlock) so you don't
   drag it by mistake while drawing hotspots.

## Step 3 – Draw the hotspots

A hotspot is just an invisible rectangle with a prototype link on it.

1. Select frame `1 Onboarding`, press **R** and draw a rectangle over the green
   **Continue** button.
2. In the right panel set **Fill opacity to 0 %** (keep the fill – fully transparent
   layers still receive taps). Optional: name the layer `→ Home`.
3. Repeat for every row in the hotspot table below. Tip: draw one hotspot, then
   **Alt-drag** it to copy, and resize.

## Step 4 – Wire the hotspots

1. Switch to the **Prototype** tab (right panel, top).
2. Select a hotspot rectangle; a small **+** circle appears on its right edge.
   Drag it to the destination frame.
3. In the interaction pop-up leave **On tap → Navigate to**, and set
   **Animation = Smart animate** or **Move in → Left** (≈ 300 ms, Ease out) for forward
   steps and **Move out → Right** for "Back" chevrons. Use **Instant** for the
   bottom-navigation tabs.
4. Tick **Scroll to → Reset scroll position** off (default) and leave overlays alone –
   all six screens are full frames.

## Step 5 – Flow start, device and share link

1. Still on the Prototype tab, click an empty part of the canvas, then under
   **Flow starting point** click **+** on frame `1 Onboarding`; name the flow
   `SabahTrail – main flow`.
2. Under **Prototype settings → Device** choose **iPhone 14 & 15 Pro** and a
   background colour (e.g. `#F2F4F3`), so the viewer shows the screens inside a phone.
3. Press **▶ Present** (top-right) and click through all 14 links – every tap in the
   table should land on the right screen, and the Back chevrons must return.
4. Click **Share** (top-right) → **Share prototype** → set
   **"Anyone with the link" → "can view"** → **Copy link**.
   The link looks like `https://www.figma.com/proto/XXXXXXXX/...?node-id=…&scaling=scale-down&starting-point-node-id=…`.
5. Paste that link into the report (Section 12.0 placeholder) and into the
   assignment submission form. Open the link in a private/incognito window once to
   make sure it works without being signed in.

---

## Hotspot wiring table (15 rows, 14 links)

Coordinates are in **frame points** (origin = top-left of each 390 × 844 frame).
They match the exported PNGs – you can also just draw over the visible control.

| # | From frame | Draw rectangle over … | Approx. box (x, y, w, h) | On tap → Navigate to | Animation |
|---|---|---|---|---|---|
| 1 | 1 Onboarding | **Continue** button | 24, 748, 342, 50 | 2 Home | Move in ← |
| 2 | 1 Onboarding | Language segmented control (BM / EN / 中文) | 32, 326, 322, 36 | *(no link – optional: three frames with a different chip highlighted)* | — |
| 3 | 2 Home | Trail card **Tawau Hills – Canopy Trail** | 24, 402, 342, 92 | 3 Trail Mode | Move in ← |
| 4 | 2 Home | Bottom-nav **Identify** | 97, 766, 98, 78 | 4 Identify | Instant |
| 5 | 2 Home | Bottom-nav **Settings** | 292, 766, 98, 78 | 6 Offline & Privacy | Instant |
| 6 | 3 Trail Mode | **‹ Back** chevron | 0, 44, 44, 44 | 2 Home | Move out → |
| 7 | 3 Trail Mode | **Identify** button | 16, 690, 173, 44 | 4 Identify | Move in ← |
| 8 | 3 Trail Mode | Bottom-nav **Settings** | 292, 766, 98, 78 | 6 Offline & Privacy | Instant |
| 9 | 4 Identify | **‹ Back** chevron | 0, 44, 44, 44 | 3 Trail Mode | Move out → |
| 10 | 4 Identify | **Shutter** (white ring) | 159, 704, 72, 72 | 5 Result | Dissolve |
| 11 | 5 Result | **‹ Back** chevron | 0, 44, 44, 44 | 4 Identify | Move out → |
| 12 | 5 Result | **Save to Journal** button | 24, 597, 165, 44 | 2 Home *(or a Journal frame if you add one)* | Move in ← |
| 13 | 5 Result | Bottom-nav **Explore** | 0, 766, 97, 78 | 2 Home | Instant |
| 14 | 6 Offline & Privacy | **‹ Back** chevron | 0, 44, 44, 44 | 2 Home | Move out → |
| 15 | 6 Offline & Privacy | Bottom-nav **Explore** | 0, 766, 97, 78 | 2 Home | Instant |

Minimum for the rubric: links 1, 3, 6, 7, 9, 10, 11, 14 (the main path
Onboarding → Home → Trail → Identify → Result and all Back buttons).

## Optional polish (worth doing if time allows – "effort beyond what was required")

* **Toggle states**: duplicate frame 6, flip one toggle in the copy (draw a 51 × 31
  rounded rectangle, `#1F7A5C` on / `#D0D0D0` off), and link the toggle in both
  directions with **On tap → Change to** (needs the frames as *component variants*)
  or simply **Navigate to** with **Instant**.
* **Geofence demo**: duplicate frame 3, move the blue user dot onto Stop 4 and change
  the "NOW PLAYING" card to *Stop 4 of 12 – Canopy walkway*; link an invisible
  hotspot over the map with **After delay → 3000 ms → Navigate to** the copy
  (Smart animate) – this shows auto-triggered narration without any coding.
* **Camera progress**: duplicate frame 4 twice with the confidence at 34 % → 78 % → 92 %
  and chain them with **After delay 600 ms**; the viewer sees the on-device model
  "thinking" before the shutter becomes active.
* Add a **cover frame** (any size) with the app name, your name/matric number, course
  code and the date; set it as the first frame so the link opens on it.

## Design tokens (if you want to edit anything natively in Figma)

| Token | Value |
|---|---|
| Accent (forest green) | `#1F7A5C` |
| Accent light | `#D6ECE2` |
| Ink / text | `#212121` |
| Secondary text | `#787878` |
| Divider | `#E1E1E1` |
| Map background | `#E8F0E6` |
| Alert red | `#D32F2F` |
| Amber (battery saver) | `#F59E0B` |
| Type | Inter / SF Pro (any neutral sans), 28/16/13/11 pt |
| Touch targets | ≥ 44 × 44 pt (Apple HIG) / 48 dp (Material 3) |
| Corner radius | cards 12, buttons 12, chips 11 |

The same tokens are used by the HTML prototype (`../index.html`) and by
`make_figures.py`, so the three artefacts stay visually consistent.
