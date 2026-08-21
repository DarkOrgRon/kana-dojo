# Baut aus den vier Mockup-Sheets die Sprite-Raster fuer index.html
from PIL import Image
from collections import deque
import json, os, sys

Q = r'H:\Meine Ablage\Projekte\kana-trainer\kana-dojo-v4\sprites-quelle'
AH, FUSS, FIG_H = 64, 58, 53
BUCHSTABEN = "ABCDEFGHIJKLMNOP"     # bis 16 Farben
NAMEN = {"ninja": ("🥷", "Ninja"), "samurai": ("⚔️", "Samurai"),
         "geisha": ("🎎", "Geisha"), "sumo": ("🍙", "Sumo")}
AURA = {"ninja": "rgba(232,200,122,0.45)", "samurai": "rgba(255,223,107,0.45)",
        "geisha": "rgba(255,183,197,0.45)", "sumo": "rgba(232,200,122,0.45)"}

def mag_abstand(c):
    return min(abs(c[0]-255)+abs(c[1])+abs(c[2]-255), abs(c[0]-236)+abs(c[1]-12)+abs(c[2]-239))

def verarbeite(char):
    im = Image.open(os.path.join(Q, f"mockup-{char}.png")).convert("RGB")
    W, H = im.size
    px = im.load()
    def magenta(c):   return mag_abstand(c) < 150
    def weiss(c):     return c[0] > 200 and c[1] > 200 and c[2] > 200
    def figur(c):     return not magenta(c) and not weiss(c)

    def bloecke(profil, s, minlen):
        aus, start = [], None
        for i, v in enumerate(profil):
            if v > s and start is None: start = i
            elif v <= s and start is not None:
                if i-start >= minlen: aus.append((start, i-1))
                start = None
        if start is not None and len(profil)-start >= minlen: aus.append((start, len(profil)-1))
        return aus
    zeilen = [sum(1 for x in range(int(W*0.22), W) if figur(px[x, y])) for y in range(H)]
    rows = sorted(bloecke(zeilen, 3, 60), key=lambda b: b[0])[-4:]
    mitte = W//2

    def komps(x0, x1, y0, y1):
        ges = [[False]*(x1-x0+1) for _ in range(y1-y0+1)]
        out = []
        for sy in range(y0, y1+1):
            for sx in range(x0, x1+1):
                if ges[sy-y0][sx-x0] or not figur(px[sx, sy]): continue
                q = deque([(sx, sy)]); ges[sy-y0][sx-x0] = True; p = []
                while q:
                    x, y = q.popleft(); p.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                        nx, ny = x+dx, y+dy
                        if x0 <= nx <= x1 and y0 <= ny <= y1 and not ges[ny-y0][nx-x0] and figur(px[nx, ny]):
                            ges[ny-y0][nx-x0] = True; q.append((nx, ny))
                if len(p) > 150: out.append(p)
        out.sort(key=len, reverse=True)
        return out

    zellen = []
    for li, (y0, y1) in enumerate(rows, start=1):
        for pi, (x0, x1) in enumerate([(int(W*0.22), mitte-10), (mitte+10, W-1)]):
            k = komps(x0, x1, y0, y1)
            fig = set(k[0])
            xs = [p[0] for p in fig]; ys = [p[1] for p in fig]
            fy0, fy1 = min(ys), max(ys)
            # Anker = MEDIAN der x-Werte aller Figurenpixel. Robust gegen duenne
            # Waffen (Katana, Faecher): die haben wenige Pixel und verschieben den
            # Median kaum, waehrend Minimum/Maximum oder der Mittelwert wegkippen.
            xs_sort = sorted(p[0] for p in fig)
            anker = xs_sort[len(xs_sort)//2]
            zellen.append(dict(level=li, pose="idle" if pi == 0 else "attack", fig=fig,
                               anker=anker, fy1=fy1,
                               links=min(xs), rechts=max(xs),
                               extra=k[1] if len(k) > 1 else None))
    block = (max(p[1] for p in zellen[0]["fig"]) - min(p[1] for p in zellen[0]["fig"]) + 1)/FIG_H
    nl = max((z["anker"]-z["links"])/block for z in zellen)
    nr = max((z["rechts"]-z["anker"])/block for z in zellen)
    AW = int(nl+nr)+4
    ANK = int(nl)+2

    def raster(z):
        gitter = [[None]*AW for _ in range(AH)]
        for ay in range(AH):
            if ay > FUSS: continue
            for ax in range(AW):
                sx = z["anker"] + (ax-ANK)*block
                sy = z["fy1"] - (FUSS-ay)*block
                a, b = int(sx), int(sy)
                c, d = max(a+1, int(sx+block)), max(b+1, int(sy+block))
                pr = [px[x, y] for y in range(max(0,b), min(H, d)) for x in range(max(0,a), min(W, c))
                      if (x, y) in z["fig"] and mag_abstand(px[x, y]) > 240]
                if len(pr) >= max(2, ((c-a)*(d-b))//3):
                    n = len(pr)
                    gitter[ay][ax] = (sum(q[0] for q in pr)//n, sum(q[1] for q in pr)//n, sum(q[2] for q in pr)//n)
        return gitter

    rohe = {(z["level"], z["pose"]): raster(z) for z in zellen}

    # Gemeinsame Begrenzung ueber ALLE 8 Posen -> Fenster beschneiden
    bx0, bx1, by0, by1 = AW, -1, AH, -1
    for g in rohe.values():
        for y in range(AH):
            for x in range(AW):
                if g[y][x]:
                    bx0, bx1 = min(bx0, x), max(bx1, x)
                    by0, by1 = min(by0, y), max(by1, y)
    ANK -= bx0
    breite, hoehe = bx1-bx0+1, by1-by0+1

    # Farbreduktion pro Level ueber beide Posen
    levels = {}
    for lv in (1, 2, 3, 4):
        paar = {p: rohe[(lv, p)] for p in ("idle", "attack")}
        hilfs = Image.new("RGB", (breite*2, hoehe), (255, 0, 255))
        hp = hilfs.load()
        for i, p in enumerate(("idle", "attack")):
            for y in range(hoehe):
                for x in range(breite):
                    c = paar[p][y+by0][x+bx0]
                    if c: hp[i*breite+x, y] = c
        q16 = hilfs.quantize(colors=16, method=Image.MAXCOVERAGE).convert("RGB")
        qp = q16.load()
        # Palette aufbauen
        farben, palette = {}, {}
        for i, p in enumerate(("idle", "attack")):
            for y in range(hoehe):
                for x in range(breite):
                    if paar[p][y+by0][x+bx0]:
                        c = qp[i*breite+x, y]
                        if c not in farben:
                            b = BUCHSTABEN[len(farben)]
                            farben[c] = b
                            palette[b] = "#%02x%02x%02x" % c
        # Magenta-Blend-Farben verwerfen: der Bodenschatten aus dem Sheet landet nach
        # der Quantisierung als eigene lila Farbe (z. B. #63006b). Regel eng gefasst,
        # damit sie den echten lila Mawashi des Sumo (Gruenanteil deutlich > 0) nicht trifft.
        def ist_blend(hexf):
            r, g, b = (int(hexf[i:i+2], 16) for i in (1, 3, 5))
            return g < 35 and r > 60 and b > 60 and abs(r-b) < 50
        weg = {b for b, hexf in palette.items() if ist_blend(hexf)}
        if weg:
            print(f"    Level {lv}: Blend-Farben entfernt: {[palette[b] for b in sorted(weg)]}")
            for b in weg: del palette[b]
        zeilenaus = {}
        for i, p in enumerate(("idle", "attack")):
            aus = []
            for y in range(hoehe):
                s = ""
                for x in range(breite):
                    c = paar[p][y+by0][x+bx0]
                    if not c: s += "."
                    else:
                        b = farben[qp[i*breite+x, y]]
                        s += "." if b in weg else b
                aus.append(s)
            zeilenaus[p] = aus
        levels[lv] = dict(palette=palette, idle=zeilenaus["idle"], attack=zeilenaus["attack"])
        print(f"    Level {lv}: {len(palette)} Farben")

    # Einheitlich beschneiden: Zeilen/Spalten, die in ALLEN 8 Posen leer sind
    def spalte_leer(x): return all(L[p][y][x] == "." for L in levels.values() for p in ("idle","attack") for y in range(hoehe))
    def zeile_leer(y):  return all(set(L[p][y]) == {"."} for L in levels.values() for p in ("idle","attack"))
    l0 = 0
    while l0 < breite-1 and spalte_leer(l0): l0 += 1
    l1 = breite-1
    while l1 > l0 and spalte_leer(l1): l1 -= 1
    o0 = 0
    while o0 < hoehe-1 and zeile_leer(o0): o0 += 1
    o1 = hoehe-1
    while o1 > o0 and zeile_leer(o1): o1 -= 1
    for L in levels.values():
        for p in ("idle", "attack"):
            L[p] = [z[l0:l1+1] for z in L[p][o0:o1+1]]
    breite, hoehe, ANK = l1-l0+1, o1-o0+1, ANK-l0
    print(f"  {char}: Fenster {breite}x{hoehe}, Anker {ANK}, Block {block:.2f}")
    return dict(breite=breite, hoehe=hoehe, anker=ANK, levels=levels)

alles = {}
for c in ("ninja", "samurai", "geisha", "sumo"):
    print(f"  == {c} ==")
    alles[c] = verarbeite(c)

# --- Alle Charaktere auf dieselbe Hoehe bringen ------------------------------
# Leere Zeilen OBEN anfuegen (nicht unten), damit die Fuesse weiter auf derselben
# Zeile stehen. Sonst sind die Karten in der Charakterauswahl unterschiedlich hoch.
maxh = max(d["hoehe"] for d in alles.values())
for c, d in alles.items():
    fehlt = maxh - d["hoehe"]
    if fehlt:
        leer = "." * d["breite"]
        for L in d["levels"].values():
            for pose in ("idle", "attack"):
                L[pose] = [leer]*fehlt + L[pose]
        d["hoehe"] = maxh
        print(f"  {c}: {fehlt} Leerzeile(n) oben ergaenzt -> Hoehe {maxh}")

# --- JS erzeugen -----------------------------------------------------------
out = []
out.append("// Charakter-Sprites: aus Pixel-Art-Mockups erzeugt (21.08.2026, Paket D).")
out.append("// Je Charakter ein eigenes Fenster (Breite unterschiedlich, wegen Waffe/Arm),")
out.append("// je Level eigene Raster UND eigene 16-Farb-Palette. '.' = durchsichtig.")
out.append("// 'anchor' = Spalte, in der die Koerpermitte (Kopf) sitzt – fuer Aura und Ausrichtung.")
out.append("const SPRITES={")
for c in ("ninja", "samurai", "geisha", "sumo"):
    d = alles[c]
    emoji, name = NAMEN[c]
    out.append(f"  {c}:{{emoji:'{emoji}',name:'{name}',w:{d['breite']},h:{d['hoehe']},anchor:{d['anker']},levels:{{")
    for lv in (1, 2, 3, 4):
        L = d["levels"][lv]
        pal = ",".join(f"{k}:'{v}'" for k, v in L["palette"].items())
        out.append(f"    {lv}:{{palette:{{{pal}}},")
        for pose in ("idle", "attack"):
            zs = ",".join(f"'{z}'" for z in L[pose])
            out.append(f"      {pose}:[{zs}],")
        out.append("    },")
    out.append("  }},")
out.append("};")
out.append("const AURA={" + ",".join(f"{k}:'{v}'" for k, v in AURA.items()) + "};")
js = "\n".join(out)
open("sprites_neu.js", "w", encoding="utf-8").write(js)
print(f"\nsprites_neu.js geschrieben: {len(js)/1024:.1f} KB")
json.dump({c: dict(breite=alles[c]["breite"], hoehe=alles[c]["hoehe"], anker=alles[c]["anker"])
           for c in alles}, open("sprites_info.json", "w"), indent=1)
