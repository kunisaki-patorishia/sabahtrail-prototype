"""
Export the six SabahTrail wireframe screens as individual, bezel-free PNGs
sized for Figma (390 x 844 logical points, rendered at 3x = 1170 x 2532 px).

Re-uses the exact drawing code from ../../make_figures.py so the Figma kit
matches Figures 4 and 5 in the report pixel-for-pixel.

    cd /home/user/assignment/prototype/figma_kit && python3 export_screens.py
"""
import os, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
import make_figures as mf  # noqa: E402

mf.S = 3  # 3x export (crisp on Retina / in Figma's prototype viewer)
W, H = mf.W, mf.H


BG = [mf.WHITE]  # background used by flat_frame (switched to dark for the camera screen)


def flat_frame(self):
    """Replace the phone bezel + notch with a plain, square-cornered screen background."""
    self.d.rectangle(self.box(0, 0, W, H), fill=BG[0])


mf.Screen.frame = flat_frame

SCREENS = [
    ("screen1_onboarding", mf.screen_onboarding),
    ("screen2_home", mf.screen_home),
    ("screen3_trail_mode", mf.screen_trail),
    ("screen4_identify_camera", mf.screen_camera),
    ("screen5_result", mf.screen_result),
    ("screen6_offline_privacy", mf.screen_settings),
]

DARK = (28, 36, 30)  # camera viewfinder colour used in make_figures.screen_camera

for name, fn in SCREENS:
    is_cam = fn is mf.screen_camera
    BG[0] = DARK if is_cam else mf.WHITE
    img = Image.new("RGB", (W * mf.S, H * mf.S), BG[0])
    sc = mf.Screen(img, 0, 0)
    fn(sc)
    if is_cam:  # flat export: hide the drawn notch pill (no bezel in Figma frames)
        sc.rect(W / 2 - 46, 6, 92, 28, fill=DARK)
    out = os.path.join(HERE, name + "@3x.png")
    img.save(out, optimize=True)
    print("saved", out, img.size)

# 1x contact sheet (handy for the README / quick preview)
sheet = Image.new("RGB", (len(SCREENS) * (W + 20) + 20, H + 40), (235, 235, 235))
for i, (name, _) in enumerate(SCREENS):
    im = Image.open(os.path.join(HERE, name + "@3x.png")).resize((W, H), Image.LANCZOS)
    sheet.paste(im, (20 + i * (W + 20), 20))
sheet.save(os.path.join(HERE, "all_screens_preview.png"), optimize=True)
print("saved contact sheet", sheet.size)
