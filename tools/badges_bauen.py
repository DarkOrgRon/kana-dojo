# Erzeugt BADGES-Array und BADGE_DESC fuer Paket E
import io

B = []   # (kategorie, id, label, emoji, cond, desc)

def add(kat, bid, label, emoji, cond, desc):
    B.append((kat, bid, label, emoji, cond, desc))

# ── Erste Schritte ───────────────────────────────────────────────────────────
add('Erste Schritte', 'first', 'Erste Antwort', '⚡', 's.total>=1',
    'Beantworte deine erste Frage.')

# ── Kombo ────────────────────────────────────────────────────────────────────
kombo = [(5,'\U0001f525'),(10,'\U0001f4a5'),(25,'✨'),(50,'\U0001f31f'),(75,'⚡'),
         (100,'\U0001f338'),(150,'\U0001f4ae'),(200,'\U0001f977'),(500,'\U0001f3ef')]
for n, e in kombo:
    add('Kombo', f'combo{n}', f'{n}er Kombo', e, f's.bestCombo>={n}',
        f'{n} richtige Antworten in Folge.')

# ── Streak ───────────────────────────────────────────────────────────────────
streak = [(3,'\U0001f4c5'),(7,'\U0001f5d3️'),(14,'\U0001f319'),(25,'\U0001f30a'),
          (50,'\U0001f3b4'),(75,'\U0001f33f'),(100,'\U0001f38b'),(150,'⛩️'),
          (200,'\U0001f5fb'),(250,'\U0001f3d4️'),(300,'\U0001f304'),(365,'\U0001f38c')]
for n, e in streak:
    add('Streak', f'streak{n}', f'{n} Tage Streak', e, f's.streak>={n}',
        f'Übe an {n} Tagen hintereinander.')

# ── Genauigkeit (unveraendert) ───────────────────────────────────────────────
for n, e in [(70,'\U0001f393'),(80,'\U0001f3af'),(90,'\U0001f50d'),(95,'\U0001f31f'),(99,'\U0001f48e')]:
    lab = {70:'70% Auf dem Weg',80:'80% Genauigkeit',90:'90% Scharfsinnig',
           95:'95% Meister',99:'99% Fast Perfekt'}[n]
    add('Genauigkeit', f'acc{n}', lab, e, f'allKanaUnlocked(s)&&recentAcc(s)>={n/100}',
        f'Alle Kana frei + {n} % der letzten 500 richtig.')

# ── Fragen an einem Tag ──────────────────────────────────────────────────────
fragen = [(10,'\U0001f423','Erster Schritt'),(25,'\U0001f4dd','Einsteiger'),
          (50,'✅','50 Fragen'),(100,'\U0001f4da','Fleißig'),
          (200,'\U0001f4aa','200 Fragen'),(500,'\U0001f33a','500 Fragen')]
for n, e, lab in fragen:
    add('Fragen an einem Tag', f'q{n}', lab, e, f's.dailyTotal>={n}',
        f'Beantworte {n} Fragen an einem Tag.')

# ── Freischaltungen ──────────────────────────────────────────────────────────
add('Freischaltungen', 'kata', 'Katakana freigesch.', 'カ', "s.unlocked.includes('カ行')",
    'Schalte die Reihe カ行 frei.')
add('Freischaltungen', 'dak', 'Dakuten freigesch.', '゛', "s.unlocked.includes('が行')",
    'Schalte die Reihe が行 frei.')

# ── Wortstufen: freigeschaltet ───────────────────────────────────────────────
wu = [('2文字','2-Silben','\U0001f524'),('3文字','3-Silben','\U0001f521'),
      ('4文字','4-Silben','\U0001f520'),('5文字','5-Silben','\U0001f4d6'),
      ('混合','Gemischt','\U0001f4d4')]
ids_u = ['w2_unlock','w3_unlock','w4_unlock','w5_unlock','mix_unlock']
for (g, name, e), bid in zip(wu, ids_u):
    txt = 'Schalte gemischte Wörter frei.' if g == '混合' else f'Schalte Wörter mit {name[0]} Silben frei.'
    add('Wortstufen freigeschaltet', bid, f'{name} freigesch.', e, f"s.unlocked.includes('{g}')", txt)

# ── Wortstufen: gemeistert (NEU: Leitner-Box 5) ──────────────────────────────
wm = [('w2_box5','2-Silben gemeistert','⭐'),('w3_box5','3-Silben gemeistert','\U0001f4a0'),
      ('w4_box5','4-Silben gemeistert','\U0001f4ae'),('w5_box5','5-Silben gemeistert','\U0001f451'),
      ('mix_box5','Gemischt gemeistert','\U0001f3ef')]
namen = {'w2_box5':'2-Silben-Wörter','w3_box5':'3-Silben-Wörter','w4_box5':'4-Silben-Wörter',
         'w5_box5':'5-Silben-Wörter','mix_box5':'gemischten Wörter'}
for bid, lab, e in wm:
    add('Wortstufen gemeistert', bid, lab, e, f"masteryDone(s,'{bid}')",
        f'Alle {namen[bid]} in Leitner-Box 5.')

# ── Kana-Meisterschaft (NEU) ─────────────────────────────────────────────────
km = [('hira_base','Hiragana-Reihen','\U0001f361','Alle Hiragana-Grundreihen in Box 5.'),
      ('hira_daku','Hiragana-Dakuten','\U0001f376','Alle Hiragana-Dakuten in Box 5.'),
      ('hira_kombi','Hiragana-Kombis','\U0001f391','Alle Hiragana-Kombinationen in Box 5.'),
      ('kata_base','Katakana-Reihen','\U0001f365','Alle Katakana-Grundreihen in Box 5.'),
      ('kata_daku','Katakana-Dakuten','\U0001f375','Alle Katakana-Dakuten in Box 5.'),
      ('kata_kombi','Katakana-Kombis','\U0001f387','Alle Katakana-Kombinationen in Box 5.')]
for bid, lab, e, d in km:
    add('Kana-Meisterschaft', bid, lab + ' gemeistert', e, f"masteryDone(s,'{bid}')", d)

# ── Lerntage gesamt ──────────────────────────────────────────────────────────
lern = [(3,'\U0001f331'),(10,'\U0001f33f'),(25,'\U0001f38d'),(50,'\U0001f3ee'),(100,'\U0001f387'),
        (150,'\U0001f5fb'),(200,'\U0001f409'),(250,'\U0001f305'),(300,'\U0001f3de️'),
        (400,'\U0001f30b'),(500,'\U0001f386'),(600,'⛩️'),(700,'\U0001f54a️'),
        (800,'\U0001f9a2'),(900,'\U0001f320'),(1000,'\U0001f5ff')]
for n, e in lern:
    add('Lerntage gesamt', f'd{n}', f'{n} Lerntage', e, f's.daysLearned>={n}',
        f'Lerne an {n} verschiedenen Tagen.')

# ── Gesamt-Antworten ─────────────────────────────────────────────────────────
ges = [(100,'\U0001f516'),(250,'\U0001f4d7'),(500,'\U0001f4d8'),(1000,'\U0001f4dc'),
       (2500,'\U0001f4d9'),(5000,'\U0001f432'),(7500,'\U0001f4d5'),(10000,'\U0001f30c'),
       (15000,'\U0001f52e'),(20000,'♾️')]
for n, e in ges:
    add('Gesamt-Antworten', f'at{n}', f'{n:,}'.replace(',', '.') + ' Gesamt', e,
        f's.total>={n}', f'Beantworte insgesamt {n:,}'.replace(',', '.') + ' Fragen.')

# ── Perfekte Tage ────────────────────────────────────────────────────────────
perf = [(1,'\U0001f4af'),(5,'\U0001f948'),(10,'\U0001f947'),(25,'\U0001f3c5'),(50,'\U0001f396️'),
        (75,'\U0001f4ab'),(100,'\U0001f31e'),(150,'✴️'),(200,'❇️'),
        (250,'\U0001f506'),(500,'☀️'),(750,'\U0001f31f'),(1000,'\U0001f48e')]
for n, e in perf:
    lab = 'Perfekter Tag' if n == 1 else f'{n} perfekte Tage'
    d = ('Ein Tag mit 50+ Antworten, ohne einen Fehler.' if n == 1
         else f'Sammle {n} perfekte Tage.')
    add('Perfekte Tage', f'perfectDay{n}', lab, e, f'(s.perfectDays||0)>={n}', d)

# ── Charaktere ───────────────────────────────────────────────────────────────
chars = [('ninja','Ninja','dem Ninja',['\U0001f977','\U0001f5e1️','\U0001f311','\U0001f320']),
         ('samurai','Samurai','dem Samurai',['⚔️','\U0001f6e1️','\U0001f38c','\U0001f409']),
         ('geisha','Geisha','der Geisha',['\U0001f38e','\U0001faad','\U0001f338','\U0001f33a']),
         ('sumo','Sumo','dem Sumo',['\U0001f359','\U0001f94b','\U0001f3c6','\U0001f5fe'])]
stufen = [(1,'Weg'),(500,'Kämpfer'),(2500,'Meister'),(10000,'Legende')]
for key, name, dat, emojis in chars:
    for (n, titel), e in zip(stufen, emojis):
        artikel = 'der' if key == 'geisha' else 'des'
        if n == 1:
            lab = f'Weg {artikel} {name}'
            d = f'Beantworte eine Frage mit {dat} richtig.'
        else:
            lab = f'{name}-{titel}' + ('in' if key == 'geisha' and titel == 'Meister' else '')
            d = f'{n:,}'.replace(',', '.') + f' richtige Antworten mit {dat}.'
        add('Charaktere', f'{key}{n}', lab, e, f"charOkOf(s,'{key}')>={n}", d)

# ── Profimodus ───────────────────────────────────────────────────────────────
pro = [(25,'\U0001f525'),(50,'\U0001f4a2'),(75,'⚡'),(100,'\U0001f32a️'),(250,'\U0001f531'),
       (500,'\U0001f451'),(750,'\U0001f3f9'),(1000,'\U0001f3c5'),(2500,'\U0001f9ff'),
       (5000,'\U0001f30b'),(10000,'\U0001f0cf')]
for n, e in pro:
    add('Profimodus', f'pro{n}', f'Profi {n:,}'.replace(',', '.'), e,
        f'((s.proStats&&s.proStats.c)||0)>={n}',
        f'{n:,}'.replace(',', '.') + ' richtige Antworten im Profimodus.')

# ── Schriftsysteme komplett ──────────────────────────────────────────────────
add('Schriftsysteme komplett', 'hira_all', 'Hiragana komplett', '\U0001f338',
    "s.unlocked.includes('組合')", 'Schalte alle Hiragana-Reihen frei.')
add('Schriftsysteme komplett', 'kata_all', 'Katakana komplett', '\U0001f390',
    "s.unlocked.includes('カ組')", 'Schalte alle Katakana-Reihen frei.')

# ── Ausgabe ──────────────────────────────────────────────────────────────────
ids = [b[1] for b in B]
assert len(ids) == len(set(ids)), 'doppelte IDs: ' + str([i for i in ids if ids.count(i) > 1])
zu_lang = [(b[1], len(b[5])) for b in B if len(b[5]) > 46]
print('Abzeichen gesamt:', len(B))
print('Beschreibungen ueber 46 Zeichen:', zu_lang if zu_lang else 'keine')

out = ['const BADGES=[']
kat = None
for k, bid, lab, emo, cond, _ in B:
    if k != kat:
        kat = k
        strich = '─' * max(1, 72 - len(k))
        out.append(f'  // ── {k} {strich}')
    out.append(f"  {{id:'{bid}',label:'{lab}',emoji:'{emo}',cond:s=>{cond}}},")
out.append('];')
out.append('')
out.append('const BADGE_DESC={')
for _, bid, _, _, _, d in B:
    out.append(f"  {bid}:'{d}',")
out.append('};')
io.open('badges_neu.js', 'w', encoding='utf-8').write('\n'.join(out))
print('badges_neu.js geschrieben')
