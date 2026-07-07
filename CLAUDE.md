# Kana Dojo v4 – Kana-Trainer mit Pixel-Charakteren

## Projektbeschreibung
Eigenständige Weiterentwicklung des Kana-Trainers (basiert auf `..\index.html`, Stand v3).
Browser-App zum Lernen von Hiragana & Katakana mit Gamification – alles in einer
einzigen Datei `index.html`, kein Build und kein Server nötig.

Das alte Projekt im übergeordneten Ordner bleibt unberührt; diese App nutzt einen
eigenen Spielstand-Speicher (localStorage-Key `kana_dojo_v4`).

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

## Konventionen
- Backups mit Versionsnummer im Dateinamen in diesem Ordner ablegen
  (z.B. `index_v4_2026-07-07.html`), bevor größere Änderungen gemacht werden.
- Spielstand-Key bei inkompatiblen Änderungen an der Datenstruktur hochzählen.
