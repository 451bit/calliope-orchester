# 🎵 Calliope Mini Orchester – Projektanleitung

**Klasse:** 10 Informatik
**Sozialform:** Partnerarbeit
**Dauer:** ca. 6–8 Unterrichtsstunden
**Material:** 3–4 Calliope mini (mind. 1 pro Gruppe + 1 als Dirigent)
**Programmierumgebung:** [makecode.calliope.cc](https://makecode.calliope.cc) – Blöcke und Python

---

## Projektidee

Mehrere Calliope mini bilden gemeinsam ein kleines Orchester. Sie verständigen sich per **Funk**: Ein Gerät übernimmt die Rolle des **Dirigenten**, alle anderen sind **Instrumente**. Alle Instrumente spielen dieselbe Melodie (*Ode an die Freude*), aber jedes eine andere **Stimme** (Sopran, Alt, Tenor, Bass). Erst wenn der Dirigent das Startsignal gibt, spielen alle gleichzeitig.

Das Projekt wird **schrittweise** aufgebaut – ihr fangt einfach an und kommt immer weiter.

---

## Programmierumgebung: MakeCode

Ihr programmiert mit **Blöcken** in MakeCode. Zusätzlich gibt es Python-Vorlagen zum Importieren – so bekommt ihr einen fertigen Startpunkt, den ihr dann mit Blöcken weiter ausbauen könnt.

### So öffnet ihr MakeCode

1. Öffne [makecode.calliope.cc](https://makecode.calliope.cc) im Browser.
2. Klicke auf **„Neues Projekt"**.
3. Gib dem Projekt einen Namen (z. B. „Instrument" oder „Dirigent").

### So importiert ihr eine Python-Vorlage

Die `.py`-Dateien aus diesem Repository sind Vorlagen, die ihr direkt in MakeCode importieren könnt:

1. Öffne die gewünschte `.py`-Datei (z. B. `instrument_vorlage.py`) und kopiere den gesamten Inhalt.
2. Klicke in MakeCode oben auf **„Python"** (Umschalten von Blöcken zu Python).
3. Lösche den vorhandenen Code und füge den kopierten Code ein.
4. Klicke dann auf **„Blöcke"** – MakeCode wandelt den Python-Code automatisch in Blöcke um.
5. Jetzt könnt ihr die Blöcke weiterbearbeiten!

> **Tipp:** Ihr könnt jederzeit zwischen Blöcken und Python hin- und herwechseln. Blöcke und Python zeigen immer dasselbe Programm – nur in verschiedenen Darstellungen.

### So übertragt ihr das Programm auf den Calliope

1. Verbinde den Calliope mini per USB-Kabel.
2. Klicke auf den **Download-Pfeil** unten links in MakeCode.
3. Die `.hex`-Datei wird heruntergeladen. Kopiere sie auf das Laufwerk „MINI" (erscheint wie ein USB-Stick).
4. Der Calliope blinkt kurz und startet neu – das Programm läuft!

---

## Überblick über die Dateien

| Datei | Zweck |
|---|---|
| `dirigent_vorlage.py` | Vorlage zum Importieren – **du** programmierst den Dirigenten mit Blöcken |
| `instrument_vorlage.py` | Startpunkt – Noten vorbereitet, Schleife noch leer |
| `instrument_schritt1.py` | Schritt 1 – fertige Lösung: Töne mit der `for`-Schleife abspielen |
| `instrument_schritt2.py` | Schritt 2 – fertige Lösung: Stimme per Taste A wechseln |
| `instrument_schritt3.py` | Schritt 3 – fertige Lösung: Auf den Dirigenten reagieren (Funk) |

Die Vorlagen (`_vorlage`) sind Startpunkte für eure Arbeit.
Die Schritt-Dateien (`_schritt1` bis `_schritt3`) sind fertige Lösungen – schaut dort nach, wenn ihr nicht weiterkommt.

---

## Teil 1: Der Dirigent

### Deine Aufgabe

Importiere `dirigent_vorlage.py` in MakeCode (siehe oben) und wechsle in die Blöcke-Ansicht. Die Vorlage enthält schon den Rahmen mit Kommentaren – ergänze die fehlenden Blöcke!

### Was der Dirigent können soll

| Aktion | Was passiert |
|---|---|
| Beim Start | „DIR" auf dem Display anzeigen |
| Taste A (allein) | `"START"` per Funk senden, Pfeilsymbol zeigen |
| Taste B | `"STOP"` per Funk senden, Kreuz anzeigen |
| Taste A+B gleichzeitig | Countdown 3→2→1 anzeigen, dann `"START"` senden |

### Wichtige Blöcke für den Dirigenten

**Funkgruppe setzen** (unter „Funk"):
Alle Geräte müssen dieselbe Gruppe haben – wir nehmen **Gruppe 42**.

```
beim Start
  Funk: Funkgruppe setzen [42]
  Anzeige: zeige Zeichenkette "DIR"
```

**Nachricht senden** (unter „Funk"):
```
wenn Knopf A gedrückt
  Funk: sende Zeichenkette "START"
  Anzeige: zeige Symbol [Pfeil hoch]
  pausiere 500 ms
  Anzeige: lösche Bildschirm
```

**Countdown** (mit einer `for`-Schleife oder einzelnen Schritten):
```
wenn Knopf A+B gedrückt
  Anzeige: zeige Zahl [3]
  pausiere 800 ms
  Anzeige: zeige Zahl [2]
  pausiere 800 ms
  Anzeige: zeige Zahl [1]
  pausiere 800 ms
  Anzeige: lösche Bildschirm
  Funk: sende Zeichenkette "START"
```

### Aufgaben Dirigent

1. Programmiere Taste A (nur START senden).
2. Programmiere Taste B (STOP senden).
3. Ergänze den Countdown für Taste A+B.
4. Teste: Zeigt das Display „DIR" beim Start?

---

## Teil 2: Das Instrument – Schritt für Schritt

### Schritt 0: Die Vorlage verstehen

**Datei zum Importieren:** `instrument_vorlage.py`

Nach dem Import siehst du in den Blöcken zwei Listen:

- **`noten`** – die Tonhöhen als Frequenz in Hertz (Hz). Höhere Zahl = höherer Ton. `0` = Pause.
- **`dauer`** – wie lange jede Note klingt, in Millisekunden (ms). 400 ms = normaler Schlag.

Die Töne der Sopranstimme (Ode an die Freude):

```
E4   E4   F4   G4   G4   F4   E4   D4   C4   C4   D4   E4   E4   D4   D4
329  329  349  392  392  349  329  294  261  261  294  329  329  294  294
```

Beide Listen gehören zusammen: `noten[i]` und `dauer[i]` bilden immer eine Note.

Deine Aufgabe: Schreibe eine Schleife, die alle Noten abspielt → Schritt 1 erklärt, wie.

---

### Schritt 1: Töne mit der `for`-Schleife abspielen

**Referenzdatei:** `instrument_schritt1.py`

#### Was lernst du hier?

Du bringst den Calliope dazu, alle Noten der Reihe nach abzuspielen – mit einer **`für`-Schleife** (in Blöcken: „für Index von 0 bis …").

#### Die Schleife in Blöcken

Unter **„Schleifen"** findest du den Block:

```
für [Index] von [0] bis [14]
```

`14` = Anzahl der Noten minus 1 (weil die Zählung bei 0 beginnt).

In jedem Durchlauf:
- `noten[Index]` → die aktuelle Frequenz (Tonhöhe)
- `dauer[Index]` → die aktuelle Länge

#### Ton abspielen

Unter **„Musik"**:

```
spiele Note mit Frequenz [noten[Index]] für [dauer[Index]] ms
```

#### Pausen (Frequenz = 0)

Wenn `noten[Index]` den Wert `0` hat, soll es still sein. Dafür nutzt du eine **Bedingung** (unter „Logik"):

```
wenn noten[Index] = 0
  pausiere dauer[Index] ms
sonst
  spiele Note mit Frequenz noten[Index] für dauer[Index] ms
```

#### Aufbau der Funktion

Alles kommt in eine eigene Funktion `spieleMelodie()` (unter „Fortgeschritten → Funktionen erstellen"). Die Funktion wird dann bei Tastendruck aufgerufen:

```
wenn Knopf A gedrückt
  rufe spieleMelodie auf
```

#### Aufgaben zu Schritt 1

1. Importiere `instrument_vorlage.py` und ergänze die Schleife in der Funktion.
2. Drücke Taste A – erkennst du die Ode an die Freude?
3. Ändere einzelne Dauern in der Liste. Was ändert sich am Rhythmus?
4. Vergleiche deine Lösung mit `instrument_schritt1.py`.

---

### Schritt 2: Zwischen Stimmen per Taste A wechseln

**Referenzdatei:** `instrument_schritt2.py`

#### Was lernst du hier?

Es gibt vier Stimmen der Ode an die Freude. Per **Taste A** wechselst du zwischen ihnen, per **Taste B** spielst du die aktuelle Stimme ab.

| Stimme | Name | Charakter |
|---|---|---|
| 0 | Sopran | Hauptmelodie – die Melodie, die jeder kennt |
| 1 | Alt | Eine Terz tiefer, ergänzt die Melodie |
| 2 | Tenor | Noch tiefer, Harmonie-Begleitung |
| 3 | Bass | Tiefe Grundtöne, oft mit Pausen |

#### Eine Variable für die aktuelle Stimme

Lege eine Variable `aktuelleStimme` an (unter „Variablen"). Sie speichert, welche Stimme gerade aktiv ist (0, 1, 2 oder 3).

#### Stimme wechseln – der Ringzähler

Bei Taste A soll `aktuelleStimme` um 1 steigen – aber nach 3 wieder bei 0 anfangen:

```
aktuelleStimme = (aktuelleStimme + 1) Mod 4
```

`Mod` (Modulo) gibt den **Rest bei Division** zurück. `(3+1) Mod 4 = 0` – so springt der Zähler zurück. Den „Modulo"-Block findet ihr unter „Mathematik".

#### Die Funktion anpassen

Die Funktion `spieleMelodie()` bekommt jetzt einen **Parameter** `stimme`. Je nach Wert holt sie die passende Notenliste:

```
wenn stimme = 0 → noten = sopranNoten
wenn stimme = 1 → noten = altNoten
wenn stimme = 2 → noten = tenorNoten
wenn stimme = 3 → noten = bassNoten
```

Dann läuft die Schleife wie in Schritt 1.

#### Aufgaben zu Schritt 2

1. Füge die vier Stimmen-Listen ein und programmiere den Wechsel per Taste A.
2. Zeige die aktuelle Stimmnummer kurz auf dem Display (als Zahl).
3. Lass je einen Calliope eine andere Stimme abspielen. Wie klingt das zusammen?
4. Vergleiche mit `instrument_schritt2.py`.

---

### Schritt 3: Auf den Dirigenten reagieren (Funk)

**Referenzdatei:** `instrument_schritt3.py`

#### Was lernst du hier?

Jetzt wird das Orchester komplett! Über Funk empfängt jedes Instrument Befehle vom Dirigenten:

- `"START"` → Melodie abspielen
- `"STOP"` → sofort aufhören

#### Funk einrichten

Unter **„Funk"**: Funkgruppe auf 42 setzen (beim Start). **Alle Geräte müssen dieselbe Gruppe haben!**

#### Nachrichten empfangen

Unter **„Funk"** gibt es den Block:

```
wenn Funk-Zeichenkette empfangen [receivedString]
```

Er wird automatisch aufgerufen, sobald eine Nachricht eintrifft. Darin prüft ihr:

```
wenn receivedString = "START"
  rufe spieleMelodie auf
wenn receivedString = "STOP"
  setze stoppSignal auf wahr
```

#### Auf STOP während der Melodie reagieren

In der Schleife innerhalb von `spieleMelodie()` prüft ihr bei jeder Note, ob `stoppSignal` gesetzt ist:

```
für Index von 0 bis 14
  wenn stoppSignal = wahr
    verlasse Schleife    ← „Schleife verlassen"-Block unter „Schleifen"
  sonst
    spiele Note …
```

#### Kompletter Ablauf im Orchester

```
1. Alle Calliope starten – jeder zeigt seine Stimmnummer
2. Jeder Musiker wählt per Taste A seine Stimme
3. Dirigent drückt Taste A  →  sendet "START"
4. Alle Instrumente empfangen "START"  →  spielen gleichzeitig
5. Dirigent drückt Taste B  →  sendet "STOP"
6. Alle Instrumente brechen beim nächsten Takt ab
7. Jeder Calliope zeigt wieder seine Stimmnummer
```

#### Aufgaben zu Schritt 3

1. Richte den Funk auf Gruppe 42 ein (beim Start).
2. Reagiere auf „START": rufe `spieleMelodie()` auf.
3. Reagiere auf „STOP": setze `stoppSignal` auf wahr.
4. Teste mit dem fertigen Dirigenten.
5. Vergleiche mit `instrument_schritt3.py`.

---

## Häufige Fehler und Lösungen

| Problem | Ursache | Lösung |
|---|---|---|
| Geräte reagieren nicht auf Funk | Unterschiedliche Funkgruppen | Sicherstellen, dass alle Gruppe 42 nutzen |
| Melodie klingt falsch | Falsche Frequenz oder Dauer in der Liste | Mit den Musterdateien vergleichen |
| Taste A+B wird nicht erkannt | Beide Tasten nicht genau gleichzeitig | Im MakeCode-Block „wenn Knopf A+B gedrückt" nutzen |
| Melodie hört nicht auf | `stoppSignal` wird in der Schleife nicht geprüft | Den „wenn stoppSignal"-Block direkt am Anfang des Schleifenköpers einfügen |
| Alle spielen dieselbe Stimme | `aktuelleStimme` wird nicht geändert | Taste-A-Block prüfen – wird die Variable wirklich gesetzt? |

---

## Wichtige MakeCode-Blöcke auf einen Blick

| Was | Kategorie in MakeCode | Wozu |
|---|---|---|
| Funkgruppe setzen | Funk | Alle Geräte auf Gruppe 42 |
| Zeichenkette senden | Funk | „START" oder „STOP" senden |
| Funk-Zeichenkette empfangen | Funk | Auf Signale reagieren |
| Zeige Zeichenkette | Anzeige | Text auf dem Display |
| Zeige Symbol | Anzeige | Symbole anzeigen |
| Für [i] von [0] bis [...] | Schleifen | Noten der Reihe nach abspielen |
| Schleife verlassen | Schleifen | Melodie bei STOP abbrechen |
| Note mit Frequenz spielen | Musik | Ton mit Hz und ms |
| Modulo | Mathematik | Ringzähler für Stimmenwechsel |
| Funktion erstellen | Fortgeschritten | Eigene Funktion wie spieleMelodie() |
