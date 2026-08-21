# Kana Dojo v4 – Kana-Trainer mit Pixel-Charakteren

## Projektbeschreibung
Eigenständige Weiterentwicklung des Kana-Trainers (basiert auf `..\index.html`, Stand v3).
Browser-App zum Lernen von Hiragana & Katakana mit Gamification – alles in einer
einzigen Datei `index.html`, kein Build und kein Server nötig.

Das alte Projekt im übergeordneten Ordner bleibt unberührt; diese App nutzt einen
eigenen Spielstand-Speicher (localStorage-Key `kana_dojo_v4`).

## IST-Stand (21.08.2026, aktuellste Version live)
Alle Änderungen sind auf GitHub gepusht und live unter https://darkorgron.github.io/kana-dojo/.
Aktueller Service-Worker-Cache: `kana-dojo-v14`. Letzter Commit: „Paket C: Badge-Erklaerung
durch Antippen …" (`f90bb53`). Deployed sind die Ausbau-Pakete 1–5 (08.08.2026) sowie die
Pakete A, B und C aus dem Testlauf-Feedback (21.08.2026). Badge-Gesamtzahl: **74**.

## ⏭️ WO WEITERMACHEN (Stand 21.08.2026, abends)
**Pakete A, B und C sind umgesetzt, deployed und live verifiziert** (Commits `c6713e5`,
`bbaa936`, `f90bb53`; Cache jetzt `kana-dojo-v14`). Nachweise und Abweichungen stehen im
Abschnitt „✅ UMSETZUNGSPLAN Pakete A–C".

**Aktuelle Phase:** Ronny testet die drei Pakete auf dem Handy. Bis zu seiner Rückmeldung
keine weiteren Features bauen („Testen vor Weiterentwicklung").

Reihenfolge danach:
1. ~~Pakete A → B → C~~ ✅ erledigt 21.08.2026
2. **Paket D – Sprite-Überarbeitung 32×32** (Charakter-Optik; eigener Lauf, Vorarbeit
   dokumentiert im Abschnitt „Paket D" weiter unten). Wartet auf echte 32×32-Pixel-PNGs.
3. **Paket 7 – Tastatur-Eingabe bei Wörtern** (Ronnys Idee vom 08.08.2026, Details unten)
4. **Paket 6 – iBj-Eigenwerbung** (Splash beim Start + dezent alle 50 Fragen, hart kodiert,
   kein Werbenetzwerk – bewusst zurückgestellt bis nach dem Testlauf)
5. **Play-Store-Veröffentlichung als TWA** (Trusted Web Activity; braucht Google Play
   Developer-Konto ~25 USD einmalig, Datenschutzerklärung, Store-Assets)
Fernziel (großes, eigenes Projekt, erst wenn die App etabliert ist): Registrierung/Accounts
mit Bonuspunkten als Shop-Rabattcodes – Registrierung läuft dann über Shopify (iBj), damit
liegt dort auch die E-Mail-Einwilligung (DSGVO: separate Checkbox + Double-Opt-in, keine
Kopplung). Monetarisierungs-Ziel laut Ronny: primär Reichweite/Branding, Rabattcodes sekundär.

## ✅ UMSETZUNGSPLAN Pakete A–C (freigegeben UND umgesetzt am 21.08.2026)
Grundlage: 5 Befunde aus Ronnys Testlauf (09.–16.08.2026). Alle Ursachen wurden am
21.08.2026 im Code verifiziert (Zeilennummern beziehen sich auf Commit `d2ac171`).

**Umsetzungsstand (alles deployed und live verifiziert):**
| Paket | Commit | Cache | Backup vorher |
|---|---|---|---|
| A – Bugfixes | `c6713e5` | `kana-dojo-v12` | `index_v13_2026-08-21_pre-paketA.html` |
| B – Fairness | `bbaa936` | `kana-dojo-v13` | `index_v14_2026-08-21_pre-paketB.html` |
| C – Badge-Info | `f90bb53` | `kana-dojo-v14` | `index_v15_2026-08-21_pre-paketC.html` |

Abweichungen von der Spezifikation (bewusst, beim Bauen entschieden):
- **C1:** Die Beschreibungen liegen in einer separaten Tabelle `BADGE_DESC` (plus Helfer
  `badgeDesc(id)`) statt als `desc`-Feld in jedem der 74 Badge-Einträge. Funktional gleich,
  aber ein Eingriff statt 74 – deutlich weniger Fehlerrisiko. Vollständigkeit ist geprüft:
  74 Badges, 74 Beschreibungen, keine verwaisten Einträge.
- **C2 Layout:** Der erste Entwurf ließ die Karte beim Umdrehen um 34 px wachsen und schob
  die Nachbarkarten (auf 375 px gemessen). Behoben durch kürzere Beschreibungen (max. 46
  Zeichen) **und** feste Mindesthöhe `.badge-card{min-height:88px}` → größte Abweichung jetzt
  **3 px**, Gesamtraster ±3 px. ⚠️ Wer Beschreibungen erweitert, muss diese Messung wiederholen.
- **B2 Migration:** `perfectEvalDate` wird beim ersten Laden auf *gestern* gesetzt, die Zählung
  beginnt also ab heute und **nicht rückwirkend**. Sonst würden Tage aus dem Altverlauf gegen
  das heutige Freischalt-Gate geprüft und könnten unverdient zählen.

**Nachweise (lokal im Browser gegen den echten Code gefahren):**
- A1: Bei 00:30 Ortszeit liefert `getToday()` den neuen Tag, der alte UTC-Weg lieferte den
  Vortag. Zeitumstellung 29.03. und 25.10.2026 je gestern/heute/morgen korrekt; für den
  kritischen Fall (00:30 am Umstellungstag) nachgewiesen, dass das alte Verfahren einen
  falschen Tag liefert, das neue nicht. 14-Tage-Reihe lückenlos, heutiger Tag rechts.
- A2: `charOk` 2499 → Stufe 2 und **kein** Badge; 2500 → Stufe 3 **und** Badge (gemeinsam).
  Gegenprobe 99.999 Antworten bei 100 richtigen → Stufe 1, kein Badge (genau Ronnys Befund).
- Migration: Altspielstand mit UTC-Datumsschlüsseln, ohne `charOk`/`box`/`recent`/Missions-
  und Profifelder lädt fehlerfrei, Fortschritt bleibt erhalten, fehlende Felder werden ergänzt.
  ⚠️ Bereits verdiente Badges werden nie aberkannt – ein altes „Meister"-Badge bleibt also
  bestehen, auch wenn es nach neuer Regel noch nicht zustünde (für Ronny irrelevant, er setzt zurück).
- B1: Antwort nach Vorstellungs-Karte lässt `total`, `correct`, `dailyTotal`, `combo`, `recent`,
  `gStats`, `history`, `charOk`, `rowRun` unverändert, erhöht aber die Leitner-Box; Meldung
  „(Übungsfrage – zählt nicht)". 💡 während einer normalen Frage setzt das Flag **nicht** –
  die Antwort zählt normal (Missbrauch ausgeschlossen). Im Profimodus: kein Countdown,
  kein Herzverlust, `proStats` unverändert, Box bei Fehler auf 1.
- B2: 50/0 Fehler → 1 perfekter Tag · 1 Fehler → 0 · 49 Antworten → 0 · Gate nicht erfüllt → 0 ·
  Lücke von 3 Tagen mit 2 perfekten Tagen → beide nachgezählt · zweite Auswertung desselben
  Tages → kein Doppelzählen · laufender Tag wird nie gezählt · Badge-Stufen bei 5 korrekt.
- C: 74/74 Beschreibungen vorhanden, Umdrehen funktioniert in beide Richtungen, gesperrte
  Badges zeigen die Anforderung, `cursor:pointer`, kein seitlicher Überlauf auf 375 px.
- Gesamttest frischer Spielstand: 10 Antworten = 7 Übungsfragen + 3 gewertete →
  `total` 3, Verlauf 3, Leitner-Boxen 7. Zähler und Verlauf konsistent.

### Offen / nächster Schritt
Ronny testet die drei Pakete auf dem Handy (Reset empfohlen, um den Anfängerpfad neu zu
erleben). Danach **Paket D** (32×32-Sprites, siehe eigenen Abschnitt), dann Paket 7, dann
Paket 6, dann Play Store.

---

## Spezifikation Pakete A–C (Referenz, wie umgesetzt)

### Verbindliche Arbeitsregeln (für JEDES Paket einzeln)
1. **Backup vorher:** `index_vN_2026-MM-TT_zweck.html` in den Projektordner (nicht ins Repo,
   ist per `.gitignore` ausgeschlossen).
2. **`CACHE`-Version in `sw.js` hochzählen** (aktuell `kana-dojo-v14`), sonst sieht Ronnys
   Handy die alte Version.
3. **Syntax-Check** des Script-Blocks vor dem Deploy (JS aus `index.html` extrahieren,
   `node --check`).
4. **Funktionstest im Browser** – inklusive **Migrationstest mit Altspielstand** (Spielstand
   ohne die neuen Felder laden: darf nicht abstürzen, Fortschritt muss erhalten bleiben).
5. **Nach dem Push byte-genau prüfen**, dass die live ausgelieferten Dateien dem Repo-Stand
   entsprechen (`curl` + `cmp` gegen `git show origin/main:…`) – nicht auf „erfolgreich"-
   Meldungen verlassen.
6. **STOPP nach jedem Paket** – Ronny testet auf dem Handy, erst danach das nächste Paket.
7. Neue Zustandsfelder **immer in `defaultState()`** ergänzen (dann deckt `resetAll()` sie
   automatisch mit ab) und **additiv** halten (bestehende Spielstände dürfen nicht brechen).
8. KI-Modelle, Schwellenwerte und Spiellogik **nicht eigenmächtig** ändern – nur was hier steht.

---

### Paket A – Bugfixes

#### A1: Tageswechsel auf Ortszeit umstellen (Befund 16.08.)
**Symptom (Ronny):** „Tageskombo wird nicht korrekt gezählt. Scheinbar greift hier ein
24-Stunden-Zeitraum und nicht wirklich ein tagesgenauer Abgleich."
**Verifizierte Ursache:** `getToday()` (Zeile 843) und `dateOffset()` (Zeile 844) bilden das
Datum über `toISOString()` – das ist **UTC**. In deutscher Sommerzeit wechselt der Tag dadurch
erst um **02:00 Uhr Ortszeit**. Alles zwischen 00:00 und 02:00 wird noch dem Vortag zugerechnet.
**Soll:** Tageswechsel um **00:00 Uhr nach Gerätezeit** (Ronnys Vorgabe).
**Umsetzung:** beide Funktionen auf lokale Datumsbestandteile umstellen:
```js
function pad2(n){return String(n).padStart(2,'0');}
function fmtLocal(d){return d.getFullYear()+'-'+pad2(d.getMonth()+1)+'-'+pad2(d.getDate());}
function getToday(){return fmtLocal(new Date());}
function dateOffset(o){const d=new Date();d.setDate(d.getDate()+o);return fmtLocal(d);}
```
⚠️ **Wichtig bei `dateOffset`:** Kalender-Arithmetik über `setDate()` verwenden, **nicht**
`Date.now()+o*86400000`. Die Millisekunden-Rechnung verschluckt bzw. dupliziert an den
Zeitumstellungstagen einen Tag – genau dort würden Streak und der 14-Tage-Verlauf falsch laufen.
**Wirkt sich aus auf (alle Aufrufstellen prüfen):** Zeile 821/823 (Streak-Prüfung beim Laden),
950 (`proResetIfNewDay` – Herzen), 1119/1128 (`handleAnswer` – Tageszähler, Streak, Lerntage),
1392 (`renderHistory` – 14-Tage-Diagramm), 1826 (`resetAll`).
**Migrationshinweis:** Bestehende Datumsschlüssel im Spielstand sind UTC-basiert. Nach der
Umstellung können `lastDate`, `dailyDate` und Schlüssel in `history` um einen Tag abweichen –
das kann einmalig zu einem Streak-Sprung führen. **Nicht nachträglich „reparieren"** (Ronny
setzt die App ohnehin zurück); die App muss den Fall nur fehlerfrei überstehen.

#### A2: Charakter-Badges auf richtige Antworten umstellen (Befund 16.08.)
**Symptom (Ronny):** „Samurai Meister als Badge erhalten, aber weiterhin nur ein Stern."
**Verifizierte Ursache:** Die 8 Charakter-Badges (Zeilen ~779–787) prüfen `s.charStats[...]`
= **alle** Antworten. Die Charakterstufe prüft seit 08.08. `S.charOk` = **nur richtige**.
Ronny hatte 500+ Antworten gesamt, aber unter 500 richtige.
**Soll (Ronnys Entscheidung):** Richtige Antworten zählen, und zwar deckungsgleich mit den Stufen.
| Badge-ID | alt | **neu** |
|---|---|---|
| `ninja1`, `samurai1`, `geisha1`, `sumo1` | `charStats >= 1` | `charOk >= 1` |
| `ninja500`, `samurai500`, `geisha500`, `sumo500` | `charStats >= 500` | **`charOk >= 2500`** |
Die „…-Meister"-Badges rücken damit auf **2.500 richtige** – identisch mit Stufe 3 „Meister"
(★★★). Badge-Beschriftungen bleiben unverändert. `charStats` bleibt im Spielstand erhalten
(wird nur nicht mehr für Badges ausgewertet).
Optional, **nur auf ausdrücklichen Wunsch Ronnys** (nicht Teil des Auftrags): eine vierte
Stufe „…-Legende" bei 10.000 richtigen ergänzen.

---

### Paket B – Fairness der Wertung

#### B1: Vorstellungs-Fragen nicht mitzählen (Befund 09.08.)
**Symptom (Ronny):** „Neue Karten sollten in die Zählung von Bewertungen nicht mit einfließen,
da bei diesen schließlich angezeigt wird, was die Karte bedeutet. Aufgefallen bei der Zählung
von 10 richtigen und auch bei Tageszielen."
**Sachlage:** Nach einer Vorstellungs-Karte (`maybeShowIntro`) folgt direkt die Abfrage genau
dieses Zeichens – die Lösung stand gerade groß auf der Karte. Diese Antwort zählt derzeit voll
für Kombo, Tagesquests, Serien-Missionen, Trefferquote und Freischaltung.
**Soll:** Diese eine Frage wird zur **ungewerteten Übungsfrage**.
- **Wird trotzdem gemacht:** Leitner-Box setzen (richtig → höher, falsch → Box 1) und das
  Zeichen als gesehen markieren (`S.seen`). Begründung: Das ist Lernstand, keine Bewertung.
- **Wird NICHT verändert:** `total`, `correct`, `dailyTotal`, `dailyCorrect`, `combo`,
  `bestCombo`, `dailyBestCombo`, `recent`, `gStats` (⚠️ steuert `computeUnlocks` – Reihen
  werden dadurch etwas später freigeschaltet, das ist gewollt), `rowRun`, `charStats`,
  `charOk`, `history`, `proStats`, Herzverlust, Badge- und Missionsprüfung.
- **Umsetzung:** Modul-Variable `practiceQ` in `renderQuestion` aus dem Rückgabewert von
  `maybeShowIntro(q)` setzen; `handleAnswer` verzweigt darauf **vor** dem Statistikblock.
- ⚠️ **Missbrauchsschutz:** Das Flag darf **nur** die automatische Erst-Vorstellung setzen,
  **nicht** der 💡-Button (`openIntroForCurrent`). Sonst könnte man jede Frage durch Antippen
  von 💡 zur Übungsfrage machen.
- **Profimodus:** Für Übungsfragen **keinen Countdown** starten und kein Herz abziehen
  (`startProTimer` überspringen) – eine ungewertete Frage darf nicht bestrafen.
- **Sichtbarkeit für den Nutzer:** In der Rückmeldezeile kennzeichnen, z. B.
  „Übungsfrage – zählt nicht mit". Sonst wirkt es wie ein Fehler, wenn Zähler stehen bleiben.
- **Folge für den 14-Tage-Verlauf:** `history` enthält künftig nur gewertete Antworten. Das
  Diagramm zeigt damit minimal weniger Balkenhöhe als bisher – **bewusst so**, weil „Perfekter
  Tag" (B2) aus `history` ausgewertet wird und beide Definitionen identisch sein müssen.

#### B2: „Perfekter Tag" neu als Sammelziel (Befund 08.08.)
**Symptom (Ronny):** „Abzeichen ‚perfekter Tag' ist zu einfach. Dadurch, dass beim Start immer
die Hinweistafeln kommen, hat man es faktisch schon am ersten Tag." Plus Wunsch: Sammelspiel
daraus machen, und „es sollte erst ab 50 Karten gelten".
**Alt:** `perfect30` (Zeile 781): `dailyTotal>=30 && dailyCorrect===dailyTotal` – sofort geprüft.
**Soll – ein Tag gilt als perfekt, wenn ALLE drei Bedingungen erfüllt sind:**
1. **≥ 50 gewertete Antworten** an diesem Tag (Ronnys Vorgabe; Übungsfragen zählen nach B1 nicht),
2. **kein einziger Fehler** an diesem Tag,
3. **Freischalt-Gate:** mindestens **8 von 16** Hiragana-Reihen **ODER** mindestens 8 von 16
   Katakana-Reihen freigeschaltet (= Ronnys „50 % der Hiragana oder Katakana"). Zur Einordnung:
   `GROUP_ORDER` enthält 16 Hiragana-Reihen (`あ行`…`組合`), 16 Katakana-Reihen (`ア行`…`カ組`)
   und 5 Wortgruppen (insgesamt 37).
**Auswertung am Tagesende (Ronnys Entscheidung):** Nicht sofort prüfen, sondern **rückblickend**,
damit ein Fehler um 23:50 den Tag noch entwerten kann.
- Neue Felder: `perfectDays` (Zähler) und `perfectEvalDate` (bis wann ausgewertet wurde).
- Beim App-Start und beim ersten Tageswechsel während der Laufzeit: alle Tage aus `S.history`
  durchgehen, die **nach `perfectEvalDate` und vor heute** liegen, jeden gegen die drei
  Bedingungen prüfen, `perfectDays` erhöhen, danach `perfectEvalDate = gestern` setzen.
  Die Schleife über alle offenen Tage ist wichtig, damit auch Tage zählen, an denen Ronny die
  App am Folgetag nicht geöffnet hat (`history` hält 60 Tage, das reicht).
- Bedingung 3 wird zum **Auswertungszeitpunkt** anhand des aktuellen Freischaltstands geprüft
  (Näherung – der historische Stand wird nicht gespeichert; bewusst akzeptiert, weil
  Freischaltungen nur zunehmen).
**Badges:** `perfect30` entfällt und wird durch eine Sammelreihe ersetzt:
| Neue ID | Bedingung | Vorschlag Beschriftung |
|---|---|---|
| `perfectDay1` | `perfectDays >= 1` | Perfekter Tag 💯 |
| `perfectDay5` | `perfectDays >= 5` | 5 perfekte Tage 🌟 |
| `perfectDay10` | `perfectDays >= 10` | 10 perfekte Tage 🏅 |
| `perfectDay25` | `perfectDays >= 25` | 25 perfekte Tage 👑 |
Badge-Gesamtzahl damit **71 → 74**. Eine eventuell im Altspielstand vorhandene ID `perfect30`
wird verwaist – unschädlich, `renderBadges` läuft über `BADGES`, nicht über `S.badges`.
**Anzeige:** neue Kachel im Fortschritt-Tab, z. B. „💯 Perfekte Tage".

---

### Paket C – Badge-Erklärung durch Antippen (Befund 16.08.)
**Symptom (Ronny):** „Bei manchen Badges weiß man nicht, warum man diese erhalten hat. Gut wäre,
wenn man drauf klickt, dass sich das Badge umdreht und man nachlesen kann, wofür man es bekommen hat."
**Umsetzung:**
- **C1:** Jedem Badge-Eintrag ein Feld `desc` mit der Anforderung in Klartext ergänzen – für
  **alle 74** Badges, deutsch, kurz, mit echten Umlauten. Beispiele: „Beantworte 25 Fragen
  richtig, ohne einen Fehler" · „Übe an 7 verschiedenen Tagen" · „Erreiche 2.500 richtige
  Antworten mit dem Samurai".
  ⚠️ Die Texte müssen zur **tatsächlichen** Bedingung passen – nach Paket A2/B2 haben mehrere
  Badges neue Schwellen. Beschreibungen aus der `cond`-Funktion ableiten, nicht aus dem Label raten.
- **C2:** Antippen einer Badge-Karte zeigt die Anforderung statt der Beschriftung, erneutes
  Antippen dreht zurück. **Empfohlen:** einfache Umschaltung des Inhalts mit kurzer Übergangs-
  Animation (robust auf allen Handys). Ein echter 3D-Umdreh-Effekt ist optional – nur wenn er
  im 2-spaltigen Raster (`.badge-grid`, Zeile 141) auf 375 px Breite nicht zu Layout-Sprüngen
  führt, weil beide Kartenseiten unterschiedlich hoch sind.
- **Gesperrte Badges (Ronnys Entscheidung):** zeigen auf der Rückseite ebenfalls die
  Anforderung – als Motivation, was man dafür tun muss. Die Vorderseite bleibt wie bisher
  verdeckt (`❓` / `???`).
- Karten müssen als antippbar erkennbar sein (Zeigefinger-Cursor, ausreichend große Trefffläche).

---

### Testfälle, die vor dem Push nachgewiesen werden müssen
| # | Paket | Test | Erwartung |
|---|---|---|---|
| 1 | A1 | Gerätezeit auf 23:59 → 00:01 stellen | Tageszähler und Tagesquests springen um **00:00 Ortszeit**, nicht um 02:00 |
| 2 | A1 | Altspielstand mit UTC-Datumsschlüsseln laden | kein Fehler, Fortschritt erhalten |
| 3 | A1 | 14-Tage-Diagramm | zeigt weiterhin 14 zusammenhängende Tage, heutiger Tag rechts |
| 4 | A2 | `charOk.samurai` = 2499 → 2500 setzen | Badge „Samurai-Meister" **und** Stufe ★★★ erscheinen gemeinsam |
| 5 | B1 | Frage direkt nach einer Vorstellungs-Karte beantworten | Kombo, Tagesquest, Serie, Trefferquote **unverändert**; Leitner-Box **steigt** |
| 6 | B1 | Während einer normalen Frage 💡 antippen, dann antworten | Antwort zählt **normal** (kein Missbrauch möglich) |
| 7 | B1 | Übungsfrage im Profimodus | kein Countdown, kein Herzverlust |
| 8 | B2 | Tag mit 50 gewerteten Antworten, 0 Fehler, Gate erfüllt → Folgetag öffnen | `perfectDays` +1, Badge `perfectDay1` |
| 9 | B2 | Tag mit 50 richtigen und 1 Fehler | **kein** perfekter Tag |
| 10 | B2 | Tag mit 49 gewerteten Antworten, 0 Fehler | **kein** perfekter Tag (Grenze 50) |
| 11 | B2 | Gate nicht erfüllt (nur 3 Reihen frei), sonst alles perfekt | **kein** perfekter Tag |
| 12 | B2 | App 3 Tage nicht öffnen, davor 2 perfekte Tage | beide werden beim nächsten Start nachgezählt |
| 13 | B2 | Zweimal am selben Tag starten | kein doppeltes Zählen (`perfectEvalDate` greift) |
| 14 | C2 | Badge antippen, erneut antippen | Anforderung erscheint, dann zurück; kein Layout-Sprung auf 375 px |
| 15 | alle | Kompletter Reset über „Alles zurücksetzen" | alle neuen Felder auf Startwert, App läuft normal weiter |

### Nicht Teil dieser Pakete
- **Charakter-Optik** (Befund 12.08.: „Aktuell wirken diese zu blass") → **Paket D**, eigener
  Lauf, siehe unten. Bewusst getrennt, weil es Grafik-Zulieferung braucht.
- Tastatur-Eingabe bei Wörtern → Paket 7.

## Paket D (geplant): Charakter-Optik / echte 32×32-Pixel-Art
Ronnys Befund vom 12.08.2026: „Optik der Charaktere verbessern, aktuell wirken diese zu blass."
Ziel: die heutigen 16×16-Sprites durch hochwertige 32×32-Pixel-Art ersetzen, 4 Charaktere ×
4 Level × 2 Posen = **32 Zustände**, plus Shuriken und Fächer.

**Messergebnis vom 21.08.2026 (wichtig, verhindert einen Fehlweg):** Die von einer Bild-KI
gelieferten Mockups (`E:\Downloads\{ninja,samurai,geisha,sumo}_mockup_alle_level_8x_nearest.png`)
sind **keine Pixel-Art**, sondern weichgezeichnete Illustrationen im Pixel-Look:
- kein Pixelraster (Blockgröße 2 zeigt bereits 63 % Abweichung – jeder Punkt hat eine eigene Farbe)
- **35.919 Farben** (Ninja) bzw. **61.646** (Sumo) – echte Pixel-Art hat 8–40
- native Größe 1536×196 pro Streifen, ca. 150 px pro Figur (nicht 32×32)
Sie sind daher **nur als Stil-, Posen- und Level-Referenz** verwendbar, **nicht** als technische
Sprite-Quelle. Ein Auslesen/Umrechnen dieser Dateien führt zu matschigem Ergebnis.

**Beschlossener Weg (Arbeitsteilung):**
1. **Bild-KI liefert echte Pixel-PNGs** mit harten Vorgaben: Leinwand **exakt 32×32** (nicht
   größer und danach verkleinert), **max. 16 Farben**, **kein Anti-Aliasing**, transparenter
   Hintergrund, eine Datei pro Zustand. Prüftest: hineinzoomen – es müssen harte Blöcke sein.
2. **Konverter-Skript** (PNG → Zeichenraster + Palette) und Integration in `index.html`.
3. **Rückfallebene**, falls Schritt 1 nicht liefert: Sprites von Hand als Raster zeichnen,
   Mockups als Stilvorlage, Kontrolle über Browser-Screenshots. Realistische Erwartung:
   klar besser als heute, aber nicht auf Mockup-Niveau.
Alternative mit dem besten Ergebnis: lizenziertes Pixel-Art-Asset-Pack (itch.io, OpenGameArt,
teils CC0) oder beauftragter Pixel-Artist – Konverter bleibt identisch.

**Technische Randbedingungen (am 21.08.2026 im Code geprüft):**
- Rastergröße und Anzeigegröße sind **entkoppelt** (`drawSprite` rechnet Raster × Skalierung).
  32×32 braucht **keine** Layout-Änderung: `#hero-wrap` ist 100 px breit, 32×32 bei Skalierung
  **3** ergibt 96 px – rund 20 % größer als heute (16×16 bei Skalierung 5 = 80 px).
- Skalierung muss eine **ganze Zahl** bleiben, sonst landen die Farbfelder auf halben
  Bildpunkten und die Kanten werden weich.
- In der Charakterauswahl ist mehr Platz (2-Spalten-Raster, ca. 140 px nutzbar): dort 32×32 bei
  Skalierung 4 = 128 px möglich, also deutlich größer als heute (96 px).
- `imageSmoothingEnabled=false` ist **nicht nötig** – `drawSprite` malt echte Rechtecke, es wird
  kein Bild skaliert. `image-rendering:pixelated` steht zusätzlich bereits im CSS (Zeile 161, 191).
- Aura bleibt **getrennt** vom Pixelraster (5. Parameter von `drawSprite`), wie bisher.
- Erhalten bleiben müssen: `charLevel`, `charPalette`, `charAura`, `levelStars`, `drawSprite`,
  `S.charOk` und die Schwellen `[0,500,2500,10000]`.
- Pro Level eigene Sprite-Varianten sind erwünscht (nicht nur Farbtausch), aber Kopf- und
  Körperposition müssen über alle 4 Level identisch bleiben, sonst „springt" die Figur beim
  Aufstieg. Idle und Attack unterscheiden sich möglichst nur in Arm/Waffe/Haltung.

**Rechtliches (von Ronny am 21.08.2026 geklärt):** Nutzungsrechte an den KI-Grafiken liegen vor
(Pro-Account). Ein EU-AI-Act-Hinweis ist nach Ronnys Einordnung nicht erforderlich, da es sich
um klar fiktive Spielfiguren ohne Verwechslungsgefahr mit realen Aufnahmen handelt.

**Briefing-Dateien (Ronnys Vorarbeit, im Download-Ordner):**
`KI-Anweisung zur Überarbeitung der Kana-App-Charaktere.md` und
`Übergabeanweisung für die andere KI zur Erstellung echter Pixel-Sprites aus den Kana-Charakter-Mockups.md`.
⚠️ Beide Dokumente verlangen von *einer* KI zugleich das Zeichnen **und** die Ausgabe als
Code-Raster. Diese Kombination ist der Grund, warum beim ersten Versuch eine 150-px-Illustration
statt Pixel-Art entstand: Bild-KIs zeichnen gut, geben aber keine sauberen Raster aus;
Text-KIs geben Raster aus, zeichnen dabei aber blind. Deshalb die Arbeitsteilung oben.

## Paket 7 (geplant): Tastatur-Eingabe bei Wörtern
Ronnys Test-Befund: Wörter sind mit 4 Antwort-Buttons zu leicht zu erraten (Ratequote 25 %,
plus Ausschluss über einzelne erkannte Zeichen). Buttons testen nur Wiedererkennen,
Tippen testet aktives Lesen-Können.
**Konzept:** Sobald Wortgruppen (2文字 …) dran sind, wird die Antwort per Tastatur (Romaji,
deutsche Tastatur reicht – nur a–z nötig) eingegeben statt per Button gewählt.
Einzelzeichen bleiben bei Buttons.
Bei der Umsetzung beachten (Feedback-Notizen vom 08.08.2026):
- Eingabefeld: `autocomplete/autocorrect/autocapitalize` aus, `Enter` = absenden,
  bei Fehler die richtige Lösung anzeigen (wie bisher).
- **Schreibweisen-Toleranz:** Hepburn ist Anzeige-Standard, aber gängige Kunrei-Varianten
  als richtig akzeptieren (shi/si, tsu/tu, fu/hu, chi/ti, ji/zi …). Groß-/Kleinschreibung
  und Leerzeichen egal.
- **Profimodus:** Countdown für Wörter von 10 s auf ~15 s erhöhen (Tippzeit).
- Mobile-Layout testen (aufklappende Tastatur verkleinert den Viewport).
- Optionale Kür (NICHT Teil des Pakets): freiwilliger Tastatur-Modus auch für Einzelzeichen.

## Ausbauplan 2026-08 (mit Ronny abgestimmt, 08.08.2026)
Sechs Pakete, nach jedem Paket Push + Test durch Ronny auf dem Handy:
1. ✅ **Leitner-System** (deployed 08.08.2026, siehe unten)
2. ✅ **Anfänger-Lernpfad** (deployed 08.08.2026, siehe unten)
3. ✅ **Missionen** (deployed 08.08.2026, siehe unten)
4. ✅ **Profimodus** (deployed 08.08.2026, siehe unten)
5. ✅ **Charakter-Level** (deployed 08.08.2026, siehe unten)
6. iBj-Eigenwerbung: Splash beim Start + dezent alle 50 Fragen, hart kodiert, kein Werbenetzwerk.
   **Bewusst zurückgestellt (Ronny, 08.08.2026):** erst nachdem die App ein paar Tage getestet wurde.
Danach (separat, erst nach Ronnys Test): Play-Store-Veröffentlichung als TWA.

**Fortschreibung 21.08.2026:** Der Testlauf ist gelaufen. Die daraus entstandenen Pakete A–C
haben jetzt Vorrang vor Paket 6 – die aktuelle Reihenfolge steht im Abschnitt
„⏭️ WO WEITERMACHEN" ganz oben und die Spezifikation im Abschnitt „🔧 UMSETZUNGSPLAN Pakete A–C".

## Paket 5: Charakter-Level (08.08.2026)
- **4 Stufen je Charakter**: Schüler → Kämpfer → Meister → Legende (`LEVEL_NAMES`).
- **Nachschärfung am selben Tag (Ronnys Entscheidung):** Stufen zählen nur noch
  **richtige** Antworten – Status muss man sich verdienen. Neuer Zähler `S.charOk`
  (startet bei 0, bewusst ohne Migration – Ronny setzt die App eh zurück),
  `CHAR_LEVELS`=[0,500,2500,10000]. `S.charStats` (alle Antworten) bleibt unverändert
  die Basis der „Weg des …"-Badges – nur die STUFE hängt an `charOk`.
  ⚠️ **Überholt seit 21.08.2026:** Genau diese Trennung war Ronnys Befund vom 16.08.
  (Badge „Samurai-Meister" erhalten, aber weiterhin nur ★). **Paket A2** stellt die 8
  Charakter-Badges ebenfalls auf `charOk` um und hebt die Meister-Schwelle auf 2.500 an.
  Maßgeblich ist der Abschnitt „🔧 UMSETZUNGSPLAN Pakete A–C", nicht dieser Absatz.
- **Optik je Stufe** als Paletten-Überschreibung (`LEVEL_STYLES`, Stufe 2 = bisheriger Look,
  niemand wird optisch „zurückgestuft" – Bestandszähler unter 100 sehen Stufe 1):
  Ninja: grau → Standard → schwarz/rotes Band → goldenes Band · Samurai: Leder → Standard →
  Prunk/Gold → glühende Klinge · Geisha: schlicht → Standard → prächtig → leuchtend ·
  Sumo: Mawashi weiß → blau → lila → schwarz (echte Rang-Anmutung).
- **Stufe 4 = goldene/rosa Aura**: radialer Glow hinter dem Sprite, gezeichnet in
  `drawSprite` (neuer 5. Parameter `aura`); `_aura`-Schlüssel im Style-Objekt.
- **Anzeige:** unterm Quiz-Helden „Ninja · Kämpfer ★★☆☆" (`levelStars`), in der
  Charakterauswahl je Karte eine `.cs-level`-Zeile (bei jedem Öffnen aktualisiert).
- **Stufenaufstieg:** in `handleAnswer` erkannt (Level vor/nach Zähler-Inkrement),
  sofortiges Neuzeichnen + Toast „Stufenaufstieg!" über die gemeinsame Toast-Leiste.
- Getestet (lokal): Schwellen (499→1, 500→2, 2499→2, 2500→3, 9999→3, 10000→4),
  alter Zähler beeinflusst Stufe nicht mehr, falsche Antwort erhöht nur charStats,
  richtige erhöht beide, Live-Aufstieg mit Toast bei der 500. richtigen Antwort,
  Sumo-Mawashi-/Stirnband-Pixelfarben je Stufe, Aura nur Stufe 4 (Pixel-Alpha-Messung),
  Auswahl-Karten zeigen Stufen, Reload sauber.
- Backups: `index_v11_2026-08-08_pre-charakterlevel.html` (vor Level-Einbau),
  `index_v12_2026-08-08_pre-level-nur-richtige.html` (vor Umstellung auf richtige Antworten)

## Paket 4: Profimodus (08.08.2026)
- **Aktivierung:** Button „🔥 Profi" in der Schalter-Leiste (`#pro-toggle`, `toggleProMode()`).
  Nicht persistiert – nach App-Neustart startet immer der Normalmodus.
- **Mechanik:** 3 Herzen pro Tag (`S.proHearts`, `S.proDate`), Countdown pro Frage
  (7 s Einzel-Kana, 10 s Wörter) als schrumpfender Farbbalken (`#pro-timer`, grün→gold→rot).
  Fehler ODER Zeitablauf = 1 Herz weg (`loseHeart()`). Timeout läuft über `handleAnswer(null,null)`
  und zählt überall als falsche Antwort (Leitner Box 1, Kombo-Reset, Serien-Reset, recent 0).
- **Sperre:** Bei 0 Herzen schaltet der Modus selbst ab (💔-Toast); erneutes Einschalten am
  selben Tag zeigt nur die Sperr-Meldung. **Bewusste Design-Entscheidung mit Ronny:** Die Sperre
  gilt NUR für den Profimodus – freies Üben (und damit das Leitner-Lernen) geht immer weiter.
  Neuer Tag → `proResetIfNewDay()` (beim Laden + bei jedem Toggle/Herzverlust) → 3 Herzen.
- **Belohnung:** 3 exklusive Badges (71 gesamt): Profi-Novize 🔥 (25 richtige im Profimodus),
  Profi-Krieger ⚡ (100), Profi-Legende 👑 (500). Zähler: `S.proStats {a,c}`.
- **Details:** Countdown startet erst nach Schließen einer Vorstellungs-Karte; 💡-Spick-Blick
  während einer Frage pausiert den Timer NICHT (Nachschauen kostet Zeit, bewusst).
  Die Schriftsystem-Button-Logik lässt `#pro-toggle` in Ruhe (id-Ausnahme an beiden Stellen).
- Getestet (lokal): Timer läuft/färbt, richtige Antwort kostet kein Herz, Fehler kostet eins,
  Timeout kostet eins (feuerte im Test real), 0 Herzen → Auto-Aus + Sperr-Meldung,
  Tages-Reset gibt 3 Herzen, Normalmodus unberührt (kein Timer, keine Herzen), Reload sauber.
- Backup vor Umbau: `index_v10_2026-08-08_pre-profimodus.html` (lokal, nicht im Repo)

## Paket 3: Missionen (08.08.2026)
- **Drei Missions-Arten:**
  - **Tagesquests** (`DAILY_QUESTS`, täglich neu): 30 Fragen, 20 richtige, eine 8er-Kombo.
    Erfüllung wird in `S.dailyClaimed` vermerkt (Reset mit den Tages-Zählern, an beiden
    Reset-Stellen). Neu dafür: `S.dailyBestCombo` (beste Kombo des Tages).
  - **Reihen-Missionen** (`ROW_TIERS` = 10/25/50 richtige **in Folge** pro Gruppe, einmalig):
    Serien-Zähler `S.rowRun[gruppe]`, Fehler in der Gruppe setzt auf 0. Erfüllte IDs
    (`row_<gruppe>_<stufe>`) in `S.missionsDone`.
  - **Schriftrollen-Stücke:** Reihe komplett gemeistert (alle Zeichen Box 4+, `scrollPieceDone`)
    → `scroll_<gruppe>` in `S.missionsDone`. Anzeige als „Hiragana-/Katakana-Rolle X/16".
- **UI:** `#mission-strip` unterm Quiz zeigt die erste offene Tagesquest + die Reihen-Mission
  der aktuellen Gruppe (Mini-Fortschrittsbalken, live nach jeder Antwort). Im Fortschritt-Tab
  neue Sektion „Missionen" (`renderMissions`): alle Tagesquests, beide Schriftrollen,
  Gesamtzähler Serien-Missionen (X von 111).
- **Toasts:** Badge- und Missions-Meldungen laufen über denselben Toast (`showBadgeToast`,
  jetzt mit variabler Überschrift `head`), Missionen mit 🎯/🏹/📜 + Partikeln.
- **Bugfix Schriftsystem-Filter (vorbestehend, beim Testen entdeckt):** Die Umschalt-Buttons
  speichern `'hiragana'`/`'katakana'`, `pickQ` prüfte aber auf `'h'`/`'k'` – der Filter hat
  **nie** gegriffen (es kamen immer beide Schriftsysteme). Gefixt durch Normalisierung in
  `pickQ`; Initial-Highlight der Buttons zusätzlich null-sicher gemacht.
- Getestet (lokal): Serie 10/25-Anbahnung + Toast bei Stufe 10, Fehler-Reset der Serie,
  kombinierter Badge+Missions-Toast, Tagesquest-Autovervollständigung (8er-Kombo),
  Schriftrollen-Stück, Fortschritt-Panel, Persistenz nach Reload, Katakana-/Hiragana-Filter
  greift jetzt wirklich, Streifen passt auf 375px.
- Backup vor Umbau: `index_v9_2026-08-08_pre-missionen.html` (lokal, nicht im Repo)

## Paket 2: Anfänger-Lernpfad (08.08.2026)
- **Vorstellungs-Karte:** Overlay `#intro-card` erscheint, bevor ein neues Einzel-Kana zum
  ersten Mal abgefragt wird (Zeichen groß, Romaji, Schriftsystem, 💡-Eselsbrücke). Für Wörter
  (WORD_GROUPS) keine Karte – sie bestehen aus bekannten Zeichen.
- **Eselsbrücken:** `MNEMO` = 92 deutsche Merkhilfen für alle Basis-Kana (Form-Assoziationen,
  inkl. Verwechsler-Hinweise シ/ツ und ソ/ン). Dakuten/Handakuten/Kombis werden in
  `getDefaultMnemo()` automatisch abgeleitet (Unicode: Dakuten = Basiszeichen+1, Handakuten +2;
  Kombis über kleines ゃゅょ erkannt).
- **Eigene Merkhilfen:** Textfeld auf der Karte → `S.myMnemo[zeichen]` (nur lokal auf dem Gerät,
  überschreibt nichts – Standard-Eselsbrücke bleibt sichtbar).
- **💡-Button** oben rechts auf der Quiz-Karte öffnet die Karte fürs aktuelle Zeichen erneut
  („Zeichen-Info", auch zum Nachtragen eigener Merkhilfen). Bewusste Entscheidung: Damit kann
  man während einer Frage „spicken" – für eine Lern-App gewollt (besser nachschauen als raten).
- **Neue Spielstand-Felder (additiv):** `S.seen` (Zeichen → vorgestellt), `S.myMnemo`.
  Migration: Bestandsnutzer bekommen alle bereits geübten Zeichen (cStats-Keys) als `seen`
  markiert → keine Karten-Flut nach dem Update.
- Getestet (lokal): Bestandsnutzer-Migration, Karte bei neuem Zeichen, eigene Merkhilfe
  speichern/vorbefüllen, 💡-Reopen, Dakuten-/Kombi-Ableitung, Neu-Nutzer-Ablauf
  (Charakterwahl → erste Karte), Overlay passt auf 375px-Viewport, keine Konsolenfehler.
- Backup vor Umbau: `index_v8_2026-08-08_pre-lernpfad.html` (lokal, nicht im Repo)

## Paket 1: Leitner-System (08.08.2026)
- **Neue Spielstand-Felder (additiv, kein Reset):** `S.box` (Zeichen → Box 1–5),
  `S.recent` (letzte 500 Ergebnisse als 0/1, rollend).
- Richtig → Box +1 (max. 5), falsch → zurück in Box 1. Ungesehen = „Neu" (Box 0).
- **Abfrage-Gewichtung** in `pickQ` jetzt nach Box: Neu=6, Box1=8, Box2=5, Box3=3, Box4=2, Box5=1
  (ersetzt die alte Quoten-Gewichtung über cStats).
- **Fortschritt-Tab:** neue Sektion „Leitner-Boxen" – „Gemeistert: X von 208 Zeichen (ab Box 4)"
  + Balken je Box (`renderLeitner`). 208 = alle Einzel-Kana inkl. Dakuten/Kombis; Wörter laufen
  intern mit, werden aber nicht angezeigt.
- **Genauigkeits-Badges (acc70–acc99) umgestellt:** zählen erst, wenn alle Kana-Reihen
  freigeschaltet sind (`組合` + `カ組`), und messen die Quote über die letzten 500 Antworten
  (`recentAcc`) statt über die Lebenszeit. Bereits verdiente Badges bleiben erhalten.
  Grund: alte Version war zu früh zu leicht UND später mathematisch unerreichbar.
- Getestet (lokal, Browser): Box-Auf-/Abstieg, Persistenz nach Reload, Migration alter
  Spielstände ohne die neuen Felder, keine Konsolenfehler.
- Backup vor Umbau: `index_v7_2026-08-08_pre-leitner.html` (lokal, nicht im Repo)

## Erweiterung v5 (07.07.2026)
- **4 Charaktere:** Geisha 🎎 (Fächer-Wirbel) und Sumo 🍙 (Stampf-Schockwelle) ergänzen Ninja und Samurai – alle 4 aus dem ursprünglichen Konzept damit umgesetzt. 4 neue Badges (Weg/Meister je Charakter) → 68 gesamt.
- **Soundeffekte:** per Web Audio API im Code erzeugt (keine Audiodateien). Töne bei richtig/falsch, Badge-Freischaltung und Kombo-Meilenstein. 🔊/🔇-Schalter im Header, Einstellung wird gespeichert.
- **Lern-Verlauf:** Balkendiagramm der letzten 14 Tage im Fortschritt-Tab (Balkenhöhe = Antworten, Farbe = Trefferquote grün/gold/rot). Daten in `S.history` pro Tag, maximal 60 Tage aufbewahrt.
- Backup vor Erweiterung: `index_v5_2026-07-07_pre-erweiterung.html` (lokal, nicht im Repo)

## Fixes nach v5 (07.07.2026)
- **Charakterauswahl-Layout:** mit 4 Charakteren wurden auf Smartphones die oberste/unterste Figur abgeschnitten (Overlay zentrierte starr, kein Scrollen). Behoben: `.cs-cards` ist jetzt ein festes CSS-Grid mit 2 Spalten (2×2), `#char-select` ist bei Bedarf scrollbar (`overflow-y:auto`) und zentriert per `margin:auto` an erstem/letztem Kind.
- **Update-Strategie (wichtig):** Service Worker von Cache-First auf **Network-First für Seitenaufrufe** umgestellt. Neue Versionen erscheinen jetzt sofort beim nächsten Öffnen, Offline-Betrieb bleibt über Cache-Fallback erhalten. Damit entfällt das frühere „2× öffnen" nach Updates (galt nur noch einmalig beim Umstieg auf diesen Service Worker).
- Service-Worker-Cache auf `kana-dojo-v5` erhöht.
- Backup vor Scroll-Fix: `index_v6_2026-07-07_pre-scrollfix.html` (lokal, nicht im Repo)

## Neu gegenüber v3 (07.07.2026)
- **Charakterauswahl beim ersten Start:** Ninja 🥷 oder Samurai ⚔️ als animierte
  Pixel-Art-Sprites (per Canvas Pixel für Pixel gezeichnet, keine Bilddateien).
  Wechsel jederzeit über den Button im Header.
- **Kampf-Animationen:** Charakter steht links neben der Kana-Karte.
  Richtige Antwort → Angriff (Ninja: Shuriken-Wurf, Samurai: Katana-Slash),
  falsche Antwort → Zusammenzucken (Shake + Grau-Effekt).
- **Lerntage gesamt 📅:** zählt jeden Tag mit mindestens einer Antwort
  (unabhängig vom Streak), sichtbar im Header und im Fortschritt-Tab.
- **20 neue Badges → 62 gesamt:** Lerntage (1–365), Gesamt-Antworten (100–10.000),
  Perfekter Tag, Weg des Ninja/Samurai, Ninja-/Samurai-Meister (500 Antworten),
  Hiragana/Katakana komplett.
- **Schwierigere Antwortauswahl (Clustering):**
  - Einzel-Kana: falsche Antworten aus derselben Reihe (あ → a/i/u/e/o) und
    derselben Vokal-Spalte (a → ka/ma/ta/ra), gemischt
  - Wörter: immer gleiche Silbenzahl (2er zu 2er, 3er zu 3er usw.)

## Starten
`index.html` doppelklicken – oder im übergeordneten Ordner
`npx http-server -p 4173` und dann `http://localhost:4173/kana-dojo-v4/` öffnen.

## Online-Version & GitHub (seit 07.07.2026)
- **Live-URL:** https://darkorgron.github.io/kana-dojo/
- **GitHub-Repo:** https://github.com/DarkOrgRon/kana-dojo (öffentlich, Account DarkOrgRon)
- Hosting über GitHub Pages (Branch `main`, Root-Verzeichnis)
- **Updates veröffentlichen:** Änderungen in diesem Ordner machen, dann
  `git add -A`, `git commit -m "Beschreibung"`, `git push` – nach 1–2 Minuten ist die Live-Seite aktuell.
  Bei geänderten Dateien (Icons, sw.js-Logik) zusätzlich die `CACHE`-Version in `sw.js` hochzählen.
  Seit der Network-First-Umstellung erscheinen Updates auf dem Handy direkt beim nächsten Öffnen (kein „2× öffnen" mehr nötig).
- **gh CLI:** liegt unter `/c/Program Files/GitHub CLI` (in Bash per `export PATH="$PATH:/c/Program Files/GitHub CLI"` ergänzen). Login besteht (Account DarkOrgRon).
- **Versionierung auf GitHub:** jeder `git commit` ist ein dauerhaft abrufbarer Stand in der Historie (`git log`), einsehbar auch unter https://github.com/DarkOrgRon/kana-dojo/commits/main. Frühere Stände lassen sich jederzeit wiederherstellen. Die lokalen `index_vN_*.html`-Backups sind per `.gitignore` bewusst NICHT im Repo (Git-Historie übernimmt diese Rolle online).

## PWA (installierbare App)
- `manifest.json` – App-Name, Icons, Standalone-Modus (ohne Browserleiste), Hochformat
- `sw.js` – Service Worker, macht die App nach dem ersten Besuch offline nutzbar
- `icon-192.png` / `icon-512.png` – App-Icons (goldenes 道-Zeichen auf dunklem Grund)
- Installation auf Android: Live-URL in Chrome öffnen → Menü ⋮ → „App installieren"
- Backup vor PWA-Umbau: `index_v4_2026-07-07_pre-pwa.html` (lokal, nicht im Repo)

## Konventionen
- Backups mit Versionsnummer im Dateinamen in diesem Ordner ablegen
  (z.B. `index_v4_2026-07-07.html`), bevor größere Änderungen gemacht werden.
- Spielstand-Key bei inkompatiblen Änderungen an der Datenstruktur hochzählen.
