# Kana Dojo v4 – Kana-Trainer mit Pixel-Charakteren

## Projektbeschreibung
Eigenständige Weiterentwicklung des Kana-Trainers (basiert auf `..\index.html`, Stand v3).
Browser-App zum Lernen von Hiragana & Katakana mit Gamification – alles in einer
einzigen Datei `index.html`, kein Build und kein Server nötig.

Das alte Projekt im übergeordneten Ordner bleibt unberührt; diese App nutzt einen
eigenen Spielstand-Speicher (localStorage-Key `kana_dojo_v4`).

## IST-Stand (08.08.2026, aktuellste Version live)
Alle Änderungen sind auf GitHub gepusht und live unter https://darkorgron.github.io/kana-dojo/.
Aktueller Service-Worker-Cache: `kana-dojo-v6`. Letzter Commit: „Leitner-System …" (`ed0b716`).

## Ausbauplan 2026-08 (mit Ronny abgestimmt, 08.08.2026)
Sechs Pakete, nach jedem Paket Push + Test durch Ronny auf dem Handy:
1. ✅ **Leitner-System** (deployed 08.08.2026, siehe unten)
2. ✅ **Anfänger-Lernpfad** (deployed 08.08.2026, siehe unten)
3. ✅ **Missionen** (deployed 08.08.2026, siehe unten)
4. ✅ **Profimodus** (deployed 08.08.2026, siehe unten)
5. Charakter-Level: 3–4 sichtbare Aufstiegsstufen pro Charakter (Sumo nach Mawashi-Rängen),
   Basis: vorhandene charStats-Zähler.
6. iBj-Eigenwerbung: Splash beim Start + dezent alle 50 Fragen, hart kodiert, kein Werbenetzwerk.
Danach (separat, erst nach Ronnys Test): Play-Store-Veröffentlichung als TWA.

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
