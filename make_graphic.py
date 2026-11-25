from PIL import Image, ImageDraw, ImageFont
import pathlib

W, H = 1600, 900
BG = (10, 14, 26)
PANEL = (18, 26, 48)
ACCENT = (0, 212, 255)
ACCENT2 = (255, 190, 60)
WHITE = (245, 248, 255)
MUTED = (180, 195, 220)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle grid dots
for x in range(60, W, 80):
    for y in range(50, H, 80):
        d.ellipse([x, y, x+4, y+4], fill=(28, 40, 70))

# accent bar left
d.rectangle([0, 0, 18, H], fill=ACCENT)

# panel
d.rounded_rectangle([70, 60, W-70, H-60], radius=36, fill=PANEL, outline=(45, 70, 120), width=3)

def font(p, s): return ImageFont.truetype(p, s)

# kicker pill
pill = "SPOTLIGHT  •  MUST-FOLLOW ON X"
f_pill = font(BOLD, 34)
tw = d.textlength(pill, font=f_pill)
d.rounded_rectangle([110, 105, 110+tw+44, 105+62], radius=31, fill=ACCENT)
d.text((132, 118), pill, font=f_pill, fill=(4, 18, 28))

# handle
d.text((110, 205), "@crisxai5", font=font(BOLD, 128), fill=WHITE)

# subtitle
d.text((114, 355), "AI & Crypto Expert", font=font(BOLD, 64), fill=ACCENT2)

# divider
d.rectangle([114, 445, 560, 453], fill=ACCENT)

# bullets
bullets = [
    "Practical AI agents & automation",
    "Crypto alpha, explained clearly",
    "Web3 tooling & on-chain workflows",
]
y = 485
for b in bullets:
    d.ellipse([118, y+14, 138, y+34], fill=ACCENT)
    d.text((162, y), b, font=font(REG, 44), fill=WHITE)
    y += 72

# abstract network decoration (right side, no logos/photos)
import random
random.seed(5)
nodes=[(1180,250),(1330,190),(1440,320),(1250,420),(1400,500),(1190,560),(1470,620)]
for i,a in enumerate(nodes):
    for b in nodes[i+1:]:
        if abs(a[0]-b[0])+abs(a[1]-b[1])<420:
            d.line([a,b], fill=(35,80,120), width=3)
for (x,y) in nodes:
    d.ellipse([x-16,y-16,x+16,y+16], fill=ACCENT)
    d.ellipse([x-7,y-7,x+7,y+7], fill=WHITE)
d.ellipse([1290,330,1390,430], outline=ACCENT2, width=5)

# footer url pill
url = "x.com/crisxai5"
f_url = font(BOLD, 42)
uw = d.textlength(url, font=f_url)
d.rounded_rectangle([110, 735, 110+uw+52, 735+76], radius=20, outline=ACCENT, width=3)
d.text((136, 750), url, font=f_url, fill=WHITE)

d.text((114+uw+90, 752), "Follow for sharp, practical insight.", font=font(REG, 36), fill=MUTED)

out = pathlib.Path.home() / "workspace/makefun/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/spotlight-crisxai5.png"
out.parent.mkdir(parents=True, exist_ok=True)
img.save(out)
print(out, img.size)
