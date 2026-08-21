# Prompt für die Bild-KI: echte 32×32-Pixel-Sprites (Paket D)

Erstellt 21.08.2026. Zweck: Aus der Bild-KI **technisch verwertbare** Pixel-Art holen –
nicht wieder weichgezeichnete Illustrationen im Pixel-Look.

## Warum der erste Versuch nicht verwertbar war (gemessen)
Die Mockups vom 21.08. hatten **kein Pixelraster** (jeder Punkt eine eigene Farbe) und
**35.919 bzw. 61.646 Farben**. Echte Pixel-Art hat 8–40 Farben und klare Blöcke.
Ursache: Der Auftrag verlangte „Pixel-Art", nannte aber keine harten technischen Grenzen.
Dieser Prompt schließt genau diese Lücke.

## Strategie (wichtig!)
1. **Nicht alle 32 Zustände in ein Bild.** Je mehr Figuren pro Bild, desto weniger Pixel pro
   Figur – daran ist der erste Versuch gescheitert. **Ein Bild = ein Charakter, ein Level,
   beide Posen** (Idle links, Attack rechts). Ergibt **16 Bilder**.
2. **Kein transparenter Hintergrund verlangen** – Bild-KIs liefern das selten sauber.
   Stattdessen **grelles Magenta `#FF00FF`**, das rechne ich später zuverlässig weg.
3. **Keine Aura anfordern.** Die Level-4-Aura zeichnet die App selbst im Code. Im Bild würde
   sie nur Farbverläufe erzeugen und das Raster zerstören.
4. **Erst EIN Testbild** schicken (Vorschlag: Ninja Level 2). Ich messe es und sage dir, ob
   der Weg funktioniert – erst dann die restlichen 15 erzeugen. Spart Zeit und Credits.

## Der Prompt (englisch – Bildmodelle folgen technischen Vorgaben darin zuverlässiger)

Kopiere den Block und ersetze nur die drei Zeilen unter `SUBJECT`, `POSE LEFT`, `POSE RIGHT`
aus der Tabelle weiter unten.

```
Pixel art character sprites: exactly TWO figures side by side, canvas 1024 x 512 pixels.

STRICT TECHNICAL RULES — these override every aesthetic consideration:
- The artwork must look as if it was drawn on a 32 x 32 pixel grid per figure and then
  enlarged with nearest-neighbour scaling. Every art pixel must be a perfectly square,
  perfectly FLAT block of ONE single colour, 16 x 16 output pixels in size, aligned to a
  strict regular grid.
- Hard edges only. NO anti-aliasing. NO gradients. NO blur. NO soft shadows. NO glow.
  NO bloom. NO texture. NO noise. NO airbrushing. No semi-transparent pixels.
- MAXIMUM 16 distinct colours in the entire image, including the background.
- Shading only in 2-3 discrete flat tone steps per material. Never a smooth transition.
- Background: ONE single flat colour, pure magenta #FF00FF. No pattern, no vignette,
  no gradient, no shadow under the figures.
- No text, no labels, no numbers, no frames, no borders, no watermark, no UI elements.
- Both figures centred in their own half of the canvas, full body visible, small margin.
- Both figures identical in size, proportions, palette and head position — only the pose
  differs. Same character, two poses, not two different characters.

STYLE:
16-bit era JRPG chibi game sprite. Front-facing three-quarter view. Roughly 3 heads tall.
Friendly, appealing, clearly readable when displayed small. Bold silhouette, minimal
interior detail, strong colour separation. Not cute-baby, not realistic, not vector art.

SUBJECT:
<<< hier die Charakter-/Level-Beschreibung aus der Tabelle einsetzen >>>

POSE LEFT (idle):
<<< hier die Idle-Pose einsetzen >>>

POSE RIGHT (attack):
<<< hier die Attack-Pose einsetzen >>>
```

## Die 16 Einsetz-Texte

**Wichtig für die Konsistenz:** Zuerst Level 2 erzeugen (das ist der Standard-Look), dieses
Bild dann als Referenz-/Vorlagenbild für die anderen drei Level desselben Charakters mitgeben,
falls das Werkzeug das unterstützt. Dazu den Satz ergänzen:
„Keep the figure identical to the reference image, change ONLY what is described below."

### Ninja — POSE LEFT: `standing upright, relaxed, both arms down at the sides.`
### Ninja — POSE RIGHT: `right arm fully extended to the right, hand open, having just thrown a shuriken; body slightly leaning forward.`
| Level | SUBJECT |
|---|---|
| 1 | `A ninja in plain grey training clothes, face mask covering mouth and nose, simple plain grey headband, no ornaments, low contrast, clearly a beginner.` |
| 2 | `A ninja in dark navy blue ninja garb, face mask covering mouth and nose, red headband, simple belt, professional look.` |
| 3 | `A ninja in near-black garb, face mask, bright strong red headband, extra straps and belt details, experienced and slightly menacing.` |
| 4 | `A ninja in black garb, face mask, GOLDEN headband, a few small golden accents on belt and straps, elite appearance. No glow, no aura.` |

### Samurai — POSE LEFT: `standing upright, feet apart, katana held down at the right side.`
### Samurai — POSE RIGHT: `katana raised and extended to the right in a wide slash, both hands on the hilt, body turned slightly.`
| Level | SUBJECT |
|---|---|
| 1 | `A samurai in simple brown leather armour, plain undecorated helmet, short moustache, dull grey unpolished katana blade, humble beginner.` |
| 2 | `A samurai in classic red lacquered plate armour, helmet with golden crescent crest horns, moustache, polished steel katana.` |
| 3 | `A samurai in deeper red armour with noticeably more golden ornaments and trim, more elaborate helmet crest, finely polished katana, prestigious.` |
| 4 | `A samurai in ornate red and gold armour with rich golden accents, elaborate helmet crest, golden-yellow katana blade. No glow, no aura.` |

### Geisha — POSE LEFT: `standing upright, calm, hands together in front, closed fan held low.`
### Geisha — POSE RIGHT: `right arm extended to the right holding a fully OPEN folding fan, other hand at the waist.`
| Level | SUBJECT |
|---|---|
| 1 | `A geisha in a plain muted dusty-rose kimono, black hair in a simple bun, one small plain hair ornament, plain undecorated folding fan, modest.` |
| 2 | `A geisha in a classic red kimono with a wide belt, black hair in a bun with decorative hair ornament, pink folding fan.` |
| 3 | `A geisha in a richer crimson kimono with flower patterns and golden trim, elaborate hair ornament with flowers, decorated fan, elegant and refined.` |
| 4 | `A geisha in a magnificent crimson kimono with pink and gold pattern accents, opulent hair ornament, richly decorated pink-and-gold fan. No glow, no aura.` |

### Sumo — POSE LEFT: `low wide crouching stance, hands on thighs, looking forward.`
### Sumo — POSE RIGHT: `pushing forward aggressively, both arms extended forward, weight on the front leg.`
| Level | SUBJECT |
|---|---|
| 1 | `A sumo wrestler, heavy compact build, bare torso, small topknot hairstyle, plain WHITE mawashi belt, beginner.` |
| 2 | `A sumo wrestler, heavy compact build, bare torso, topknot hairstyle, BLUE mawashi belt.` |
| 3 | `A sumo wrestler, heavy compact build, bare torso, well-groomed topknot, PURPLE mawashi belt, stronger muscle definition.` |
| 4 | `A sumo wrestler, heavy compact build, bare torso, formal topknot, BLACK mawashi belt, grand champion presence. No glow, no aura.` |

## Zusätzlich: die zwei Effekt-Bilder
Gleicher Prompt, aber diese Zeilen ersetzen:
- Kopf: `canvas 512 x 256 pixels, exactly TWO objects side by side` und
  `as if drawn on a 16 x 16 pixel grid per object … 16 x 16 output pixels per art pixel`
- `SUBJECT: LEFT: a metal shuriken (four-pointed ninja throwing star), grey steel with a
  darker outline and a small centre hole. RIGHT: an open Japanese folding fan, pink paper
  with a dark wooden handle and thin ribs.`
- Posen-Zeilen entfallen.

## Abnahmetest – bitte VOR dem Senden prüfen
1. **Hineinzoomen** (400–800 %). Es müssen **harte Quadrate** zu sehen sein. Sieht der Rand
   weich, verwaschen oder „luftgepinselt" aus → **unbrauchbar**, neu erzeugen.
2. **Hintergrund** muss durchgehend gleichmäßig magenta sein, ohne Schatten unter der Figur.
3. **Keine Aura, kein Leuchten**, auch nicht bei Level 4.
4. Beide Figuren gleich groß, Kopf auf gleicher Höhe.

Wenn dasselbe Werkzeug zweimal weichgezeichnete Bilder liefert, ist es das falsche Werkzeug –
dann einen spezialisierten Pixel-Art-Generator nutzen statt eines allgemeinen Bildmodells.

## Was ich brauche
Die PNGs unverändert (nicht nachskaliert, nicht als JPG!), benannt nach dem Schema
`ninja_l1.png`, `ninja_l2.png`, … `sumo_l4.png`, `effekte.png`.
Ablage: `H:\Meine Ablage\Projekte\kana-trainer\kana-dojo-v4\sprites-quelle\`

**Bitte zuerst nur `ninja_l2.png`** – ich messe Raster, Farbanzahl und Kantenschärfe und sage
dir, ob der Weg trägt, bevor du die restlichen 15 erzeugst.

## Was ich damit mache
1. Magenta-Hintergrund entfernen, Bild auf 32×32 zurückrechnen (Blockmittelwert, damit auch
   leicht verschobene Raster sauber werden), Farben auf ≤16 reduzieren.
2. Ergebnis in das bestehende Zeichenraster-Format (Buchstaben + Palette) umwandeln.
3. In `index.html` integrieren: `SPRITES` je Level, Skalierung 3 im Quiz (96 px) und 4 in der
   Charakterauswahl (128 px). `charLevel`, `charPalette`, `charAura`, `levelStars`, `drawSprite`,
   `S.charOk` und die Schwellen `[0,500,2500,10000]` bleiben unverändert.
4. Aura für Level 4 weiter im Code (nicht im Bild).
