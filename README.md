# 🎵 Calliope Mini Orchester – Projektanleitung (Python)

**Klasse:** 10 Informatik  
**Sozialform:** Partnerarbeit  
**Dauer:** ca. 6–8 Unterrichtsstunden  
**Material:** 3–4 Calliope mini (mind. 1 pro Gruppe + 1 als Dirigent)  
**Programmierumgebung:** [python.microbit.org](https://python.microbit.org) (MicroPython, läuft direkt im Browser)

---

## Projektidee

Mehrere Calliope mini bilden gemeinsam ein kleines Orchester. Sie verständigen sich per **Funk**: Ein Gerät übernimmt die Rolle des **Dirigenten**, alle anderen sind **Instrumente**. Alle Instrumente spielen dieselbe Melodie (*Ode an die Freude*), aber jedes eine andere **Stimme** (Sopran, Alt, Tenor, Bass). Erst wenn der Dirigent das Startsignal gibt, spielen alle gleichzeitig.

Das Projekt wird **schrittweise** aufgebaut – ihr fangt einfach an und kommt immer weiter.

---

## Python auf dem Calliope mini

Alle Dateien in diesem Projekt sind **MicroPython**-Dateien (`.py`). So überträgst du sie auf den Calliope:

1. Öffne [python.microbit.org](https://python.microbit.org) im Browser.
2. Kopiere den Code der gewünschten Datei in den Editor.
3. Verbinde den Calliope mini per USB-Kabel.
4. Klicke auf **„Senden"** (Flash). Der Calliope lädt kurz und startet dann neu.

**Wichtige Python-Grundlagen für dieses Projekt:**

| Was du brauchst | Python-Code | Bedeutung |
|---|---|---|
| Alles importieren | `from microbit import *` | Zugriff auf Display, Tasten, … |
| Musik-Modul laden | `import music` | Töne abspielen |
| Funk-Modul laden | `import radio` | Funkkommunikation |
| Warten | `sleep(500)` | 500 Millisekunden pausieren |
| Taste A prüfen | `button_a.was_pressed()` | True, wenn A seit letzter Prüfung gedrückt |
| Taste A halten | `button_a.is_pressed()` | True, solange A gerade gehalten wird |
| Text scrollen | `display.scroll("Hallo")` | Text über Display scrollen |
| Symbol anzeigen | `display.show(Image.HEART)` | Symbol zeigen |
| Display löschen | `display.clear()` | Alles ausschalten |
| Ton spielen | `music.pitch(440, 500)` | 440 Hz für 500 ms spielen |
| Ton stoppen | `music.stop()` | Ton sofort ausschalten |
| Funk senden | `radio.send("START")` | Text per Funk senden |
| Funk empfangen | `radio.receive()` | Empfangenen Text (oder None) |

---

## Überblick über die Dateien

| Datei | Zweck |
|---|---|
| `dirigent_vorlage.py` | Vorlage – **du** programmierst den Dirigenten |
| `instrument_vorlage.py` | Startpunkt – Melodie vorbereitet, Schleife fehlt noch |
| `instrument_schritt1.py` | Schritt 1 – Töne mit der `for`-Schleife abspielen |
| `instrument_schritt2.py` | Schritt 2 – Zwischen Stimmen per Taste A wechseln |
| `instrument_schritt3.py` | Schritt 3 – Auf Dirigenten reagieren (Funk) |

Die Schritte bauen aufeinander auf. Fange mit `instrument_vorlage.py` an und arbeite dich bis zu `instrument_schritt3.py` vor.

---

## Teil 1: Der Dirigent

### Deine Aufgabe

Öffne `dirigent_vorlage.py`. Darin findest du **TODO-Kommentare**, die erklären, was du programmieren sollst. Das ist kein Lückentext – du schreibst den Code selbst!

### Was der Dirigent können soll

| Aktion | Was passiert |
|---|---|
| Beim Start | "DIR" auf dem Display anzeigen |
| Taste A (allein) | `"START"` per Funk senden, Pfeilsymbol zeigen |
| Taste B | `"STOP"` per Funk senden, Kreuz anzeigen |
| Taste A+B gleichzeitig | Countdown 3→2→1 anzeigen, dann `"START"` senden |

### Hinweise zur Umsetzung

**Funk einschalten:**  
Bevor du Funk nutzen kannst, musst du ihn einschalten und eine Gruppe wählen. **Alle Geräte im Orchester müssen dieselbe Gruppe haben** – wir nehmen Gruppe 42.

```python
radio.on()
radio.config(group=42)
```

**Nachricht senden:**

```python
radio.send("START")
```

**Taste A (aber nicht A+B):**  
`button_a.was_pressed()` gibt `True` zurück, wenn A seit der letzten Prüfung gedrückt wurde.  
Damit du A und A+B unterscheidest, prüfst du, ob B *nicht* gleichzeitig gehalten wird:

```python
if button_a.was_pressed() and not button_b.is_pressed():
    # Nur A wurde gedrückt
```

**Taste A und B gleichzeitig:**

```python
if button_a.is_pressed() and button_b.is_pressed():
    # Beide Tasten gleichzeitig gehalten
```

**Countdown mit for-Schleife:**  
`range(3, 0, -1)` zählt rückwärts: 3, 2, 1.

```python
for i in range(3, 0, -1):
    display.show(str(i))   # str() wandelt Zahl in Text um
    sleep(800)
display.clear()
```

**Symbole:**

```python
display.show(Image.ARROW_N)   # Pfeil nach oben
display.show(Image.NO)        # Kreuz (X)
display.show(Image.HEART)     # Herz
display.show(Image.YES)       # Häkchen
```

---

## Teil 2: Das Instrument – Schritt für Schritt

### Schritt 0: Die Vorlage verstehen

**Datei:** `instrument_vorlage.py`

Die Datei enthält bereits zwei Listen:

```python
noten = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]
```

**Was bedeutet das?**

- `noten[i]` – die **Frequenz** der i-ten Note in **Hertz (Hz)**.  
  Höhere Zahl = höherer Ton. Der Wert `0` bedeutet Pause (kein Ton).
- `dauer[i]` – die **Länge** der i-ten Note in **Millisekunden (ms)**.  
  400 ms = ein normaler Schlag, 800 ms = ein langer Schlag.

Beide Listen **gehören zusammen**: `noten[0]` und `dauer[0]` bilden den ersten Ton, `noten[1]` und `dauer[1]` den zweiten, usw.

Die Noten der Ode an die Freude (Sopranstimme):

```
E4   E4   F4   G4   G4   F4   E4   D4   C4   C4   D4   E4   E4   D4   D4
329  329  349  392  392  349  329  294  261  261  294  329  329  294  294
```

Deine Aufgabe: Schreibe eine Schleife, die alle Noten abspielt → das lernst du in Schritt 1.

---

### Schritt 1: Töne mit der `for`-Schleife abspielen

**Datei:** `instrument_schritt1.py`

#### Die `for`-Schleife mit Index

Um alle Noten der Reihe nach abzuspielen, brauchen wir einen Zähler `i`, der von `0` bis zur letzten Note hochläuft:

```python
for i in range(len(noten)):
    # i nimmt nacheinander die Werte 0, 1, 2, ..., 14 an
    print(noten[i])   # gibt die i-te Frequenz aus
    print(dauer[i])   # gibt die i-te Dauer aus
```

- `len(noten)` – Anzahl der Noten (hier: 15)
- `range(15)` – erzeugt die Zahlen 0, 1, 2, …, 14
- `noten[i]` – greift auf den **i-ten Eintrag** der Liste zu (*Indexzugriff*). Der erste Eintrag ist immer Index `0`.

#### Einen Ton abspielen mit `music.pitch()`

```python
music.pitch(freq, ms)
```

- `freq` – Frequenz in Hz (z. B. `329` für E4)
- `ms` – Wie lange der Ton klingt, in Millisekunden (z. B. `400`)

Der Calliope wartet, bis der Ton fertig ist, bevor er weitermacht.

#### Pausen behandeln (Frequenz = 0)

Wenn `noten[i]` den Wert `0` hat, soll es still sein:

```python
if freq == 0:
    music.stop()   # Ton ausschalten
    sleep(ms)      # so lange still bleiben
else:
    music.pitch(freq, ms)   # Ton spielen
```

#### Die vollständige Schleife

```python
for i in range(len(noten)):
    freq = noten[i]   # aktuelle Frequenz
    ms   = dauer[i]   # aktuelle Dauer

    if freq == 0:
        music.stop()
        sleep(ms)
    else:
        music.pitch(freq, ms)

    sleep(30)   # kurze Lücke zwischen den Noten
```

Das `sleep(30)` sorgt für eine kleine Lücke zwischen den Tönen – das klingt natürlicher.

#### Aufgaben zu Schritt 1

1. Lade `instrument_schritt1.py` und drücke Taste A. Erkennst du die Melodie?
2. Ändere einzelne Dauern in der Liste. Was passiert mit dem Rhythmus?
3. Setze eine Frequenz auf `0`. Was hörst du an dieser Stelle?
4. Wie kannst du eine Note wiederholen? (Tipp: Einfach nochmal in die Liste eintragen)

---

### Schritt 2: Zwischen Instrumenten (Stimmen) wechseln

**Datei:** `instrument_schritt2.py`

#### Was lernst du hier?

Die Ode an die Freude kann in **vier verschiedenen Stimmen** gespielt werden. Per **Taste A** wechselst du zwischen den Stimmen, per **Taste B** spielst du die aktuelle Stimme ab.

| Stimme | Name | Charakter |
|---|---|---|
| 0 | Sopran | Hauptmelodie – die Melodie, die jeder kennt |
| 1 | Alt | Eine Terz tiefer, ergänzt die Melodie |
| 2 | Tenor | Noch tiefer, Harmonie-Begleitung |
| 3 | Bass | Tiefe Grundtöne mit Pausen |

#### Vier Stimmen als vier Listen

```python
sopran_noten = [329, 329, 349, 392, ...]   # die Hauptmelodie
alt_noten    = [261, 261, 294, 329, ...]   # eine Terz tiefer
tenor_noten  = [196, 196, 220, 247, ...]   # noch tiefer
bass_noten   = [131,   0, 131,   0, ...]   # Grundtöne mit Pausen
```

Alle vier Stimmen haben **dieselben Dauern** – so spielen sie später synchron.

#### Eine Liste von Listen

Damit wir bequem zwischen den Stimmen wechseln können, packen wir alle vier in eine **Liste von Listen**:

```python
alle_stimmen = [sopran_noten, alt_noten, tenor_noten, bass_noten]
```

- `alle_stimmen[0]` gibt `sopran_noten` zurück  
- `alle_stimmen[1]` gibt `alt_noten` zurück  
- `alle_stimmen[2]` gibt `tenor_noten` zurück  
- `alle_stimmen[3]` gibt `bass_noten` zurück  

Wenn wir die aktuelle Stimme in `aktuelle_stimme` speichern, holen wir die Notenliste so:

```python
noten = alle_stimmen[aktuelle_stimme]
```

#### Stimme wechseln mit dem Modulo-Operator

Bei Taste A soll `aktuelle_stimme` um 1 steigen – aber nach `3` wieder bei `0` anfangen. Das erledigt der **Modulo-Operator `%`** (Rest bei Division):

```python
aktuelle_stimme = (aktuelle_stimme + 1) % len(alle_stimmen)
```

Beispieldurchlauf:

```
aktuell=0  →  (0+1) % 4 = 1
aktuell=1  →  (1+1) % 4 = 2
aktuell=2  →  (2+1) % 4 = 3
aktuell=3  →  (3+1) % 4 = 0   ← springt zurück auf 0!
```

#### Die Hauptschleife

```python
while True:
    if button_a.was_pressed():
        aktuelle_stimme = (aktuelle_stimme + 1) % len(alle_stimmen)
        zeige_stimme()          # Stimmnummer auf Display zeigen

    if button_b.was_pressed():
        spiele_melodie(aktuelle_stimme)   # aktuelle Stimme abspielen

    sleep(100)
```

#### Aufgaben zu Schritt 2

1. Lade `instrument_schritt2.py` und teste alle vier Stimmen mit Taste A/B.
2. Lasst je einen Calliope eine andere Stimme wählen und drückt gleichzeitig Taste B. Klingt das zusammen?
3. Was passiert, wenn zwei Calliope dieselbe Stimme spielen?

---

### Schritt 3: Auf den Dirigenten reagieren (Funk)

**Datei:** `instrument_schritt3.py`

#### Was lernst du hier?

Jetzt kommt das Orchester zusammen! Über Funk empfängt jedes Instrument Befehle vom Dirigenten:

- `"START"` → Melodie abspielen
- `"STOP"` → sofort aufhören

#### Funk einrichten

Funk funktioniert nur, wenn **alle Geräte dieselbe Gruppe** haben. Wir nutzen Gruppe 42:

```python
radio.on()
radio.config(group=42, power=7)
# power=7 = maximale Sendeleistung (bessere Reichweite)
```

#### Nachrichten empfangen

`radio.receive()` schaut, ob eine neue Nachricht angekommen ist:

- Ist eine da: gibt den Text als String zurück (z. B. `"START"`)
- Ist nichts da: gibt `None` zurück

```python
nachricht = radio.receive()

if nachricht == "START":
    # Dirigent hat das Startzeichen gegeben!
    spiele_melodie(aktuelle_stimme)
```

**Wichtig:** Rufe `radio.receive()` regelmäßig in der Hauptschleife auf. Jeder Aufruf liest die älteste Nachricht und löscht sie aus dem Puffer. Rufst du ihn zu selten auf, verpasst du Nachrichten.

#### Während der Melodie auf STOP reagieren

Die Melodie dauert mehrere Sekunden. Damit wir in dieser Zeit auf `"STOP"` reagieren können, prüfen wir den Funk **in der for-Schleife** bei jeder Note:

```python
for i in range(len(noten)):
    # Funk prüfen, bevor die Note gespielt wird
    nachricht = radio.receive()
    if nachricht == "STOP":
        break   # Schleife sofort verlassen!

    freq = noten[i]
    ms   = dauer[i]
    # ... Ton spielen ...
```

`break` verlässt die `for`-Schleife sofort. Das Instrument stoppt dann beim nächsten Takt.

#### Die Zustandsvariable `spielt`

Um zu unterscheiden, ob das Instrument gerade spielt oder wartet, nutzen wir eine **boolesche Variable**:

```python
spielt = False   # zu Beginn wartet das Instrument
```

In der Hauptschleife:

```python
while True:
    if not spielt:
        # Taste A: Stimme wechseln (nur wenn wir nicht spielen)
        if button_a.was_pressed():
            aktuelle_stimme = (aktuelle_stimme + 1) % len(alle_stimmen)
            zeige_stimme()

        # Funk prüfen: auf START warten
        nachricht = radio.receive()
        if nachricht == "START":
            spielt = True
            spiele_melodie(aktuelle_stimme)
            spielt = False   # nach dem Spielen wieder bereit

    sleep(50)
```

#### Kompletter Ablauf im Orchester

```
1. Alle Calliope starten – jeder zeigt seine Stimmnummer
2. Jeder Musiker wählt per Taste A seine Stimme (S0, S1, S2 oder S3)
3. Dirigent drückt Taste A  →  sendet "START"
4. Alle Instrumente empfangen "START"  →  spielen gleichzeitig
5. Dirigent drückt Taste B  →  sendet "STOP"
6. Alle Instrumente brechen die Melodie beim nächsten Takt ab
7. Jeder Calliope zeigt wieder seine Stimmnummer – bereit für den nächsten Start
```

#### Aufgaben zu Schritt 3

1. Flashe `instrument_schritt3.py` auf alle Instrument-Calliope und das fertige Dirigenten-Programm auf den Dirigenten.
2. Wähle unterschiedliche Stimmen. Startet der Dirigent das Orchester gleichzeitig?
3. Stoppt STOP wirklich alle Geräte?
4. **Erweiterung:** Lass die Melodie nach `"START"` wiederholt spielen (Endlosschleife), bis `"STOP"` kommt.

---

## Häufige Fehler und Lösungen

| Problem | Ursache | Lösung |
|---|---|---|
| Calliope reagiert nicht auf Funk | Unterschiedliche Funkgruppen | Alle `radio.config(group=42)` prüfen |
| `radio.receive()` gibt immer `None` | `radio.on()` vergessen | `radio.on()` vor der Hauptschleife aufrufen |
| Melodie klingt falsch | Frequenz oder Dauer falsch | Mit den Musterdateien vergleichen |
| Taste A+B wird als A erkannt | A+B-Erkennung zu spät | A+B-Prüfung mit `is_pressed()` **vor** den Einzeltasten-Checks |
| Display zeigt nichts | `display.clear()` zu früh | `sleep()` vor `display.clear()` einfügen |
| Melodie stoppt nicht bei STOP | `radio.receive()` fehlt in der for-Schleife | `receive()`-Aufruf ganz oben im Schleifenkörper einfügen |

---

## Schnell-Referenz: MicroPython auf dem Calliope

```python
# Imports
from microbit import *
import music
import radio

# Display
display.scroll("Text")            # Text scrollen
display.show(Image.HEART)         # Symbol zeigen
display.show("A")                 # Einzelnen Buchstaben zeigen
display.clear()                   # Alles löschen

# Tasten
button_a.was_pressed()            # True, wenn A seit letzter Prüfung gedrückt
button_b.was_pressed()            # True, wenn B seit letzter Prüfung gedrückt
button_a.is_pressed()             # True, solange A gerade gehalten wird
button_b.is_pressed()             # True, solange B gerade gehalten wird

# Musik
music.pitch(440, 500)             # 440 Hz für 500 ms spielen
music.stop()                      # Ton sofort stoppen
sleep(200)                        # 200 ms Pause (Stille)

# Funk
radio.on()                        # Funk einschalten (nicht vergessen!)
radio.config(group=42)            # Gruppe 42 wählen
radio.send("START")               # Text senden
nachricht = radio.receive()       # Text empfangen (oder None)

# Nützliches
len(liste)                        # Anzahl der Elemente in einer Liste
str(zahl)                         # Zahl in Text umwandeln: str(3) ergibt "3"
zahl % n                          # Modulo: Rest bei Division (Ringzähler)
range(n)                          # Zahlen 0, 1, ..., n-1
range(a, b, -1)                   # Rückwärts von a bis b+1
```

## Symbole auf dem Display

```python
Image.HEART           # Herz
Image.YES             # Häkchen
Image.NO              # Kreuz
Image.ARROW_N         # Pfeil hoch
Image.ARROW_S         # Pfeil runter
Image.MUSIC_QUAVERS   # Musiknoten
Image.DIAMOND         # Raute
Image.SMILEY          # Smiley
Image.SAD             # Traurig
```
