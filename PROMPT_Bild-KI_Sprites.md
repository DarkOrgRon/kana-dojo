# Prompt für die Bild-KI: echte Pixel-Sprites (Paket D) — Fassung 2

Stand 21.08.2026, **nach dem erfolgreichen Testbild**. Diese Fassung ersetzt Fassung 1.

## Was sich gegenüber Fassung 1 geändert hat
Das Testbild (Ninja Level 2) war **verwertbar** – die Verarbeitungskette funktioniert.
Zwei Erkenntnisse daraus sind eingearbeitet:

1. **Zielauflösung ist jetzt 64×64 pro Figur statt 32×32.** Die KI hat von sich aus mit
   ~64×64 gezeichnet, und das ist besser: Beim Herunterrechnen auf 32×32 zerfällt das
   Gesicht (Augen, Maske, Gürtelknoten verschmelzen), bei 64×64 bleibt alles lesbar.
   Die Figur wird in der App dadurch **128 px groß statt 80 px** (+60 %).
2. **Die Leinwandgröße wird nicht mehr exakt vorgegeben**, nur noch das Seitenverhältnis 2:1
   und das Kunstraster. Grund: Das Testbild kam als 1774×887 zurück, obwohl 1024×512 verlangt
   war – Bildmodelle halten exakte Pixelmaße ohnehin nicht ein. Meine Verarbeitung rechnet
   inzwischen auch mit gebrochenen Rastergrenzen korrekt.

**Bereits erledigt:** `ninja_l2.png` ✅ (das Testbild ist verwertbar und wird verwendet).
**Offen:** die restlichen **15 Bilder** + `effekte.png`.

## Wichtiger Hinweis zum Speichern
Das Testbild hatte **60.751 Farben** statt 16 und ein zu `#fa03f9` verschmiertes Magenta –
Signatur einer verlustbehafteten Komprimierung. Meine Kette kompensiert das, aber **je
saubererer die Quelle, desto besser das Ergebnis**:
- **PNG verlustfrei** exportieren, **nicht** JPG, **nicht** nachskalieren, **keinen Screenshot**.
- Wenn das Werkzeug „Originalgröße herunterladen" anbietet: das nehmen.

## Strategie
1. **Ein Bild = ein Charakter, ein Level, beide Posen** (Idle links, Attack rechts).
   Nicht alle Zustände in ein Bild – daran ist der erste Anlauf gescheitert.
2. **Magenta `#FF00FF` als Hintergrund**, keine Transparenz verlangen (liefern Bild-KIs selten
   sauber). Ich rechne das Magenta zuverlässig weg.
3. **Keine Aura anfordern, auch bei Level 4 nicht.** Die zeichnet die App im Code. Im Bild
   würde sie nur Farbverläufe erzeugen und das Raster zerstören.
4. **Referenzbild für Konsistenz:** Pro Charakter zuerst Level 2 erzeugen, dieses Bild dann
   bei den anderen drei Leveln als Vorlage mitgeben. Für den Ninja ist das schon vorhanden
   (`ninja_l2.png`) – bitte für Level 1, 3 und 4 als Referenz verwenden.

## Der Prompt (englisch – Bildmodelle folgen technischen Vorgaben darin zuverlässiger)

Kopiere den Block und ersetze die drei Zeilen unter `SUBJECT`, `POSE LEFT`, `POSE RIGHT`
aus der Tabelle weiter unten.

```
Pixel art character sprites: exactly TWO figures side by side. Image aspect ratio exactly
2:1 (twice as wide as tall).

STRICT TECHNICAL RULES — these override every aesthetic consideration:
- The artwork must look as if it was drawn on a 64 x 64 pixel grid PER FIGURE (128 x 64 for
  the whole image) and then enlarged with nearest-neighbour scaling. Every art pixel must be
  a perfectly square, perfectly FLAT block of ONE single colour, aligned to a strict regular
  grid. All blocks exactly the same size.
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
Friendly, appealing, clearly readable when displayed small. Bold silhouette, strong colour
separation, clean readable face. Not cute-baby, not realistic, not vector art.

SUBJECT:
<<< hier die Charakter-/Level-Beschreibung aus der Tabelle einsetzen >>>

POSE LEFT (idle):
<<< hier die Idle-Pose einsetzen >>>

POSE RIGHT (attack):
<<< hier die Attack-Pose einsetzen >>>
```

**Zusatzsatz, wenn ein Referenzbild mitgegeben wird:**
`Keep the figure identical to the reference image — same body, same face, same proportions,
same pose. Change ONLY what is described under SUBJECT.`

## Die Einsetz-Texte

### Ninja — POSE LEFT: `standing upright, relaxed, both arms down at the sides.`
### Ninja — POSE RIGHT: `right arm fully extended to the right, hand open, having just thrown a shuriken; body slightly leaning forward.`
| Level | Status | SUBJECT |
|---|---|---|
| 1 | offen | `A ninja in plain grey training clothes, face mask covering mouth and nose, simple plain grey headband, no ornaments, low contrast, clearly a beginner.` |
| 2 | ✅ fertig | — |
| 3 | offen | `A ninja in near-black garb, face mask, bright strong red headband, extra straps and belt details, experienced and slightly menacing.` |
| 4 | offen | `A ninja in black garb, face mask, GOLDEN headband, a few small golden accents on belt and straps, elite appearance. No glow, no aura.` |

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

## Zusätzlich: die zwei Effekt-Bilder (`effekte.png`)
Gleicher Prompt, aber diese Zeilen ersetzen:
- `exactly TWO objects side by side` und
  `as if drawn on a 16 x 16 pixel grid PER OBJECT (32 x 16 for the whole image)`
- `SUBJECT: LEFT: a metal shuriken (four-pointed ninja throwing star), grey steel with a
  darker outline and a small centre hole. RIGHT: an open Japanese folding fan, pink paper
  with a dark wooden handle and thin ribs.`
- Die beiden Posen-Zeilen entfallen.

## Abnahmetest – bitte VOR dem Senden prüfen
1. **Hineinzoomen** (400–800 %). Es müssen **harte Quadrate** zu sehen sein, alle gleich groß.
   Sieht der Rand weich, verwaschen oder „luftgepinselt" aus → **unbrauchbar**, neu erzeugen.
2. **Hintergrund** durchgehend gleichmäßig magenta, ohne Schatten unter der Figur.
3. **Keine Aura, kein Leuchten**, auch nicht bei Level 4.
4. Beide Figuren gleich groß, **Kopf auf gleicher Höhe**, erkennbar dieselbe Figur.
5. Gesicht muss klar lesbar sein (Augen als getrennte Formen erkennbar).

Wenn dasselbe Werkzeug zweimal weichgezeichnete Bilder liefert, ist es das falsche Werkzeug –
dann einen spezialisierten Pixel-Art-Generator nutzen statt eines allgemeinen Bildmodells.

## Ablage
Als PNG, verlustfrei, unverändert, benannt nach diesem Schema:
`ninja_l1.png`, `ninja_l3.png`, `ninja_l4.png`, `samurai_l1.png` … `sumo_l4.png`, `effekte.png`
in `H:\Meine Ablage\Projekte\kana-trainer\kana-dojo-v4\sprites-quelle\`
(`ninja_l2.png` = das bereits abgenommene Testbild bitte ebenfalls dort ablegen.)

## Was ich damit mache (getestet, funktioniert)
1. Magenta-Hintergrund mit Toleranz entfernen (auch bei verschmierten Werten wie `#fa03f9`).
2. Auf **128×64 Kunstpixel** zurückrechnen (64×64 pro Figur), per Blockmittelwert über die
   inneren 60 % jedes Blocks – dadurch stören auch gebrochene Rastergrenzen und
   Kompressionsrauschen nicht.
3. Farben auf **16 reduzieren**, Ergebnis in das bestehende Zeichenraster-Format (Buchstaben
   + Palette) umwandeln.
4. In `index.html` integrieren: `SPRITES` je Charakter und Level, **Skalierung 2** im Quiz
   (= 128 px Figur) und **3** in der Charakterauswahl. Dazu die Heldenspalte von 100 auf
   132 px verbreitern – nachgerechnet: passt auf einem 375-px-Handy (336 von 343 px).
5. Aura für Level 4 weiter im Code (nicht im Bild).
6. `charLevel`, `charPalette`, `charAura`, `levelStars`, `drawSprite`, `S.charOk` und die
   Schwellen `[0,500,2500,10000]` bleiben unverändert.
