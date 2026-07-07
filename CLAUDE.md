# Kana Dojo v4 – Kana-Trainer mit Pixel-Charakteren

## Projektbeschreibung
Eigenständige Weiterentwicklung des Kana-Trainers (basiert auf `..\index.html`, Stand v3).
Browser-App zum Lernen von Hiragana & Katakana mit Gamification – alles in einer
einzigen Datei `index.html`, kein Build und kein Server nötig.

Das alte Projekt im übergeordneten Ordner bleibt unberührt; diese App nutzt einen
eigenen Spielstand-Speicher (localStorage-Key `kana_dojo_v4`).

## IST-Stand (07.07.2026, aktuellste Version live)
Alle Änderungen sind auf GitHub gepusht und live unter https://darkorgron.github.io/kana-dojo/.
Aktueller Service-Worker-Cache: `kana-dojo-v5`. Letzter Commit: „Charakterauswahl als festes 2x2-Raster, Updates sofort sichtbar".

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
