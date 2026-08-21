from PIL import Image, ImageDraw
import re, math

js = open("sprites_neu.js", encoding="utf-8").read()
# --- sprites_neu.js einlesen ------------------------------------------------
chars = {}
for m in re.finditer(r"\n  (\w+):\{emoji:'[^']*',name:'([^']*)',w:(\d+),h:(\d+),anchor:(\d+),levels:\{(.*?)\n  \}\},", js, re.S):
    key, name, w, h, ank, body = m.group(1), m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(5)), m.group(6)
    levels = {}
    for lm in re.finditer(r"\n    (\d):\{palette:\{(.*?)\},\n      idle:\[(.*?)\],\n      attack:\[(.*?)\],\n    \},", body, re.S):
        lv = int(lm.group(1))
        pal = dict(re.findall(r"(\w+):'(#\w+)'", lm.group(2)))
        idle = re.findall(r"'([^']*)'", lm.group(3))
        atk  = re.findall(r"'([^']*)'", lm.group(4))
        levels[lv] = (pal, idle, atk)
    chars[key] = dict(name=name, w=w, h=h, anchor=ank, levels=levels)
print("gelesen:", {k: (v['w'], v['h'], v['anchor'], len(v['levels'])) for k, v in chars.items()})

AURA = {"ninja": (232,200,122), "samurai": (255,223,107), "geisha": (255,183,197), "sumo": (232,200,122)}
SCALE, BODY_X = 2, 44

def zeichne(bild, rows, pal, x0, y0, aura=None, ank=None):
    d = ImageDraw.Draw(bild, "RGBA")
    if aura:
        cx = x0 + (ank+0.5)*SCALE; cy = y0 + len(rows)*SCALE*0.55
        r = len(rows)*SCALE*0.7
        for i in range(28, 0, -1):
            rr = r*i/28; a = int(115*(1-i/28)**1.6)
            d.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=(*aura, a))
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            c = pal.get(ch)
            if c:
                rgb = tuple(int(c[i:i+2], 16) for i in (1, 3, 5))
                d.rectangle([x0+x*SCALE, y0+y*SCALE, x0+x*SCALE+SCALE-1, y0+y*SCALE+SCALE-1], fill=rgb)

# Eine Bühne = Handy-Breite 343, Held links (Spalte 92 breit), Karte 200x200 ab x=96
def buehne(key, lv, pose):
    sp = chars[key]; pal, idle, atk = sp["levels"][lv]
    rows = idle if pose == "idle" else atk
    B, H = 343, 232
    bild = Image.new("RGB", (B, H), (10, 10, 20))
    d = ImageDraw.Draw(bild)
    # Kana-Karte (200x200, unten ausgerichtet)
    ky = H-200-8
    d.rounded_rectangle([96, ky, 296, ky+200], radius=20, fill=(16, 12, 10), outline=(232,200,122), width=3)
    d.text((176, ky+92), "か", fill=(245,240,232))
    # Held: Leinwand-Ursprung nach derselben Formel wie in der App
    links = round(BODY_X-(sp["anchor"]+0.5)*SCALE)
    unten = H-8-20
    y0 = unten - len(rows)*SCALE
    zeichne(bild, rows, pal, links, y0, AURA[key] if lv == 4 else None, sp["anchor"])
    d.rectangle([0, 0, 91, H-1], outline=(60,60,80))      # Heldenspalte zur Orientierung
    d.text((4, 4), f"{sp['name']} L{lv} {pose}", fill=(150,150,170))
    return bild

for key in chars:
    teile = [buehne(key, lv, p) for lv in (2, 4) for p in ("idle", "attack")]
    ges = Image.new("RGB", (343*2+12, 232*2+12), (30, 30, 40))
    for i, t in enumerate(teile):
        ges.paste(t, ((i % 2)*(343+12), (i//2)*(232+12)))
    ges.save(f"buehne_{key}.png")
    print("  geschrieben: buehne_" + key + ".png")
