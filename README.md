# 🎵 Calliope Mini Orchester – Projektanleitung

**Klasse:** 10 (Leistungskurs Informatik)  
**Sozialform:** Partnerarbeit  
**Dauer:** ca. 6–8 Unterrichtsstunden  
**Material:** 3–4 Calliope mini (mind. 1 pro Gruppe + 1 als Dirigent), MakeCode (makecode.calliope.cc)

---

## Projektidee

Mehrere Calliope mini bilden gemeinsam ein kleines Orchester. Die Geräte verständigen sich per Funkübertragung: Eines übernimmt die Rolle des **Dirigenten**, die anderen sind **Musiker**. Die Musiker einigen sich zunächst selbstständig darauf, welches Instrument (d.h. welche Melodie/Stimme) jeder von ihnen spielt. Erst wenn der Dirigent ein Startsignal sendet, spielen alle gleichzeitig – im vorgegebenen Takt.

Das Projekt wird **schrittweise** aufgebaut. Ihr fangt mit dem einfachsten Teil an und erweitert das Programm Schritt für Schritt.

---

## Überblick über die Phasen

| Phase | Inhalt | Schwerpunkt |
|-------|--------|-------------|
| 1 | Funkverbindung testen | Radio, Senden & Empfangen |
| 2 | Instrumentenaushandlung | Variablen, Bedingungen, Zufall |
| 3 | Dirigent kommt hinzu | Koordination, Rollen |
| 4 | Melodien einbauen | Musik, Takt, Listen |
| 5 | Fertigstellung & Vorführung | Integration, Fehlersuche |

---

## Phase 1: Funkverbindung herstellen

### Was ihr programmiert
Beide Calliope sollen miteinander per Funk kommunizieren. Gerät A sendet beim Drücken von Taste A eine Nachricht. Gerät B empfängt diese und zeigt sie auf der LED-Matrix an.

### Ziel
Ihr versteht, wie Funknachrichten gesendet und empfangen werden, und habt eine funktionierende Verbindung zwischen zwei Geräten.

### Hinweise zu den Blöcken

**Wichtig zuerst:** Beide Geräte müssen dieselbe **Funkgruppe** verwenden. Verwendet z.B. Gruppe `42`. Den Block dafür findet ihr unter `Funk → Funkgruppe setzen`. Dieser Block kommt in den `beim Start`-Block.

**Senden:**  
Im `wenn Knopf A gedrückt`-Block verwendet ihr `Funk → sende Zeichenkette`. Als Text gebt ihr z.B. `"Hallo"` ein.

**Empfangen:**  
Unter `Funk` gibt es den Block `wenn Funk-Zeichenkette empfangen`. Darin zeigt ihr mit `Anzeige → zeige Zeichenkette` die empfangene Nachricht an. Die empfangene Nachricht steckt automatisch in einer Variable, die MakeCode euch vorgibt (z.B. `receivedString`).

### Aufgaben
1. Baut das beschriebene Programm nach und testet es.
2. Erweitert: Wenn Taste B gedrückt wird, soll eine andere Nachricht gesendet werden.
3. Überlegt: Was passiert, wenn beide Geräte gleichzeitig senden?

---

## Phase 2: Instrumentenaushandlung (ohne Dirigent)

### Was ihr programmiert
Die Musiker-Geräte sollen sich selbstständig darauf einigen, wer welches Instrument spielt – also wer Stimme 0, wer Stimme 1 und wer Stimme 2 übernimmt. Jedes Gerät zeigt am Ende seine Instrumentennummer auf der LED-Matrix an.

### Idee des Aushandlungsprozesses

Jedes Gerät wählt beim Start **zufällig** eine Instrumentennummer (0, 1 oder 2) und sendet diese per Funk an alle anderen. Kommt eine Nachricht an, bei der jemand anderes dieselbe Nummer beansprucht, muss dieses Gerät eine neue, freie Nummer wählen.

Das klingt erst kompliziert – aber mit folgendem Ablauf wird es übersichtlich:

```
1. Beim Start: warte kurz (zufällig, damit nicht alle gleichzeitig senden)
2. Wähle zufällig eine Nummer zwischen 0 und 2
3. Sende: "CLAIM:0" (oder 1 oder 2)
4. Zeige deine Nummer auf der LED-Matrix
5. Wenn du eine Nachricht empfängst:
     → Ist es ein CLAIM mit deiner eigenen Nummer?
       → Konflikt! Wähle eine andere Nummer und sende erneut
     → Ist es ein CLAIM mit einer anderen Nummer?
       → Merke dir, dass diese Nummer vergeben ist
```

### Hinweise zu den Blöcken

**Zufallszahl:** `Mathematik → wähle zufällige Zahl zwischen 0 und 2`

**Warten:** `Grundlagen → pausiere (ms)`. Für den Zufallsversatz kombiniert ihr das mit einer Zufallszahl, z.B. `pausiere (wähle zufällige Zahl zwischen 100 und 500) ms`.

**Variablen:** Ihr braucht mindestens:
- `meinInstrument` – die eigene Nummer (0, 1 oder 2)
- `vergebeneNummern` – eine Liste oder drei einzelne boolesche Variablen (z.B. `instrument0vergeben`, `instrument1vergeben`, `instrument2vergeben`)

**Text zusammensetzen:** Um `"CLAIM:0"` zu senden, nutzt ihr `Text → verbinde "CLAIM:" und meinInstrument`. Den Block findet ihr unter `Text → verbinde`.

**Nachrichten auswerten:** Im Empfangs-Block prüft ihr mit `wenn ... dann`, ob die empfangene Zeichenkette z.B. `"CLAIM:0"` entspricht. Dafür nutzt ihr `Text → enthält` oder einen direkten Vergleich mit `=`.

**Zahl aus Text lesen:** Den letzten Buchstaben (die Nummer) aus `"CLAIM:0"` könnt ihr mit dem Block `Text → Zeichen ab Position ... im Text ...` herauslesen. Die Nummer ist immer das letzte Zeichen. Alternativ könnt ihr für jede mögliche Nachricht einen eigenen Vergleich machen (also `wenn receivedString = "CLAIM:0" dann ...` usw.) – das ist einfacher und für den Anfang empfohlen.

**Neue Nummer finden:** Wenn ein Konflikt festgestellt wurde, müsst ihr prüfen, welche Nummern noch frei sind, und eine davon wählen. Schreibt dafür eine **eigene Funktion** (unter `Fortgeschritten → Funktionen`), die durch 0, 1, 2 geht und die erste freie zurückgibt.

### Aufgaben
1. Implementiert die Aushandlung zunächst für **2 Geräte** (nur Instrumente 0 und 1).
2. Erweitert auf 3 Geräte mit 3 Instrumenten.
3. Testet: Was passiert, wenn ihr gleichzeitig einschaltet? Was passiert beim Neustart?
4. Fügt eine visuelle Rückmeldung hinzu: Das Gerät soll kurz eine Animation zeigen, wenn ein Konflikt gelöst wurde.

---

## Phase 3: Der Dirigent kommt hinzu

### Was ihr programmiert
Ein Gerät bekommt eine besondere Rolle: den **Dirigenten**. Der Dirigent sendet kein CLAIM, sondern wartet auf Tastendruck und schickt dann ein Startsignal. Die Musiker warten nach der Aushandlung darauf, dass der Dirigent loslegt.

### Zwei verschiedene Programme

Ab jetzt habt ihr **zwei unterschiedliche Programme**:
- **Programm A – Dirigent:** Wird auf genau einem Calliope gespielt.
- **Programm B – Musiker:** Wird auf allen anderen Calliope gespielt.

### Dirigent – Was das Programm macht

Der Dirigent hat keine Melodie. Er:
1. Zeigt beim Start ein `"D"` auf der LED-Matrix (für Dirigent).
2. Wenn **Taste A** gedrückt wird: Sendet die Nachricht `"START"` und zeigt ein Herz-Symbol.
3. Wenn **Taste B** gedrückt wird: Sendet die Nachricht `"STOP"` und zeigt ein `"X"`.

**Hinweise:**  
Einfachste Variante: Der Dirigent sendet nur `"START"`. Das Tempo ist erstmal fest im Musiker-Programm eingestellt. Erweiterung: Das Tempo wird als Zahl mitgesendet, z.B. `"START:120"` (120 Schläge pro Minute).

### Musiker – Was sich ändert

Die Musiker führen nach der Aushandlung zunächst **nichts** aus – sie warten einfach auf ein Signal. Das ist in MakeCode der Normalfall: Wenn kein Event ausgelöst wird, passiert nichts.

Im Empfangs-Block wird jetzt **zusätzlich** auf `"START"` und `"STOP"` reagiert:

```
Wenn Funk-Zeichenkette empfangen:
  wenn receivedString = "CLAIM:0" → (wie bisher)
  wenn receivedString = "CLAIM:1" → (wie bisher)
  wenn receivedString = "CLAIM:2" → (wie bisher)
  wenn receivedString = "START"   → setze Variable "spieltGerade" auf wahr
  wenn receivedString = "STOP"    → setze Variable "spieltGerade" auf falsch
```

Ihr braucht also eine neue boolesche Variable `spieltGerade`.

### Hinweise zu den Blöcken

**Boolesche Variable:** Unter `Variablen → erstelle Variable` anlegen, Typ ist automatisch boolean wenn ihr `wahr` / `falsch` zuweist.

**Hauptschleife:** Für das spätere Abspielen der Melodie braucht ihr eine Dauerschleife. Nutzt `Grundlagen → dauerhaft`. Darin prüft ihr: `wenn spieltGerade = wahr dann (Melodie spielen)`.

### Aufgaben
1. Programmiert den Dirigenten.
2. Passt das Musiker-Programm an: Reagiert auf `"START"` und `"STOP"`, und zeigt dabei verschiedene Symbole (z.B. Pfeil nach oben beim Start, Kreuz beim Stopp).
3. Testet die Kommunikation: Reagieren alle Musiker auf das Startsignal?
4. Überlegt: Was passiert, wenn der Dirigent `"START"` sendet, bevor die Aushandlung abgeschlossen ist? Wie könnte man das verhindern?

---

## Phase 4: Melodien einbauen

### Was ihr programmiert
Jetzt bekommt das Orchester seinen Sound! Jeder Musiker spielt seine eigene Melodie (seine „Stimme"), und alle spielen im gemeinsamen Takt, den der Dirigent vorgibt.

### Takt-Synchronisation

Das einfachste und zuverlässigste Modell: Der Dirigent sendet regelmäßig einen **Taktschlag** (`"BEAT"`). Bei jedem empfangenen Beat spielt der Musiker die **nächste Note** seiner Melodie.

**Warum nicht einfach selbst zählen?**  
Wenn jeder Musiker selbst auf die Zeit achtet, entstehen schnell kleine Abweichungen (der eine wartet 500ms, der andere etwas mehr oder weniger). Durch den gemeinsamen Beat-Takt bleiben alle synchron.

### Dirigent – Beat senden

Der Dirigent schickt nach dem Startsignal in regelmäßigen Abständen `"BEAT"`. Nutzt dafür eine Dauerschleife:

```
dauerhaft:
  wenn spieltGerade = wahr:
    sende Zeichenkette "BEAT"
    pausiere 500 ms   ← das ist das Tempo (500ms = 120 BPM)
```

Das Intervall bestimmt das Tempo: 500 ms pro Beat entspricht 120 Schlägen pro Minute. Experimentiert gerne mit dem Wert!

**Hinweis Blöcke:** Der `dauerhaft`-Block läuft immer. Die Variable `spieltGerade` wird beim Drücken von Taste A auf `wahr` und bei Taste B auf `falsch` gesetzt (wie gehabt), zusätzlich aber jetzt auch für das Beat-Senden genutzt.

### Musiker – Melodie abspielen

Ihr braucht jetzt zwei Dinge:

**1. Die Melodie als Liste von Noten**  
In MakeCode könnt ihr eine Variable als **Array** (Liste) anlegen. Unter `Arrays` findet ihr entsprechende Blöcke. Speichert eure Noten als Zeichenketten, z.B.:

```
melodie = ["C", "E", "G", "E", "D", "F", "A", "F"]
```

Oder ihr nutzt direkt die eingebauten Musiknoten-Blöcke (unter `Musik`) und speichert sie als Nummern.

**2. Ein Zähler für die aktuelle Position**  
Eine Variable `taktPosition` startet bei 0. Bei jedem Beat wird die Note an Position `taktPosition` gespielt, dann wird `taktPosition` um 1 erhöht. Wenn `taktPosition` das Ende der Liste erreicht, setzt ihr sie auf 0 zurück (Melodie wiederholt sich).

```
Wenn receivedString = "BEAT":
  wenn spieltGerade = wahr:
    spiele Note: melodie[taktPosition]
    taktPosition = taktPosition + 1
    wenn taktPosition ≥ Länge der Melodie:
      taktPosition = 0
```

**Hinweise zu den Blöcken:**

- `Arrays → hole Wert an Position ... aus ...`: Damit lest ihr eine Note aus der Liste.
- `Arrays → Länge von ...`: Damit prüft ihr, ob ihr am Ende angelangt seid.
- `Musik → spiele Note ... für ... Takt(e)`: Damit spielt ihr eine Note. Nutzt kurze Dauern (z.B. 1/4-Takt), damit der Calliope nicht blockiert wird.
- **Wichtig:** Spielt die Note mit `wait = false` (nicht blockierend), falls diese Option verfügbar ist, damit der Empfangsblock sofort wieder aktiv ist.

### Melodien selbst erfinden

Jedes Paar erfindet jetzt die Melodien für alle drei Instrumente. Denkt dabei an:

- **Stimme 0 (Melodie):** Die Hauptmelodie – die Töne, die man sofort erkennt.
- **Stimme 1 (Bass):** Tiefe Töne, die den Rhythmus tragen. Oft einfacher und sich wiederholend.
- **Stimme 2 (Harmonie):** Mittlere Töne, die die Melodie ergänzen.

Alle Stimmen sollten **gleich lang** sein (z.B. 8 Noten), damit sie sich synchron wiederholen.

Ihr könnt z.B. ein bekanntes Kinderlied aufteilen oder etwas Eigenes komponieren. Achtet darauf, dass die Töne gut zusammenklingen (Töne derselben Tonleiter passen gut zusammen, z.B. C-Dur: C, D, E, F, G, A, H).

### Aufgaben
1. Erfindet eure drei Melodiestimmen auf Papier (Notennamen genügen).
2. Implementiert die Beat-Logik im Dirigenten.
3. Implementiert die Melodie-Wiedergabe im Musiker-Programm.
4. Testet zunächst mit nur einem Musiker, dann mit allen dreien.
5. Passt das Tempo an, bis es euch gefällt.

---

## Phase 5: Integration und Vorführung

### Was ihr fertigstellt

In dieser Phase bringt ihr alles zusammen, testet das komplette System und bereitet die Vorführung vor.

### Checkliste Integration

Geht folgende Punkte systematisch durch:

- [ ] Aushandlung funktioniert zuverlässig, auch wenn alle Geräte gleichzeitig gestartet werden
- [ ] Alle Musiker reagieren auf `"START"` und `"STOP"` des Dirigenten
- [ ] Alle Musiker spielen beim ersten `"BEAT"` mit der Note an Position 0 los
- [ ] Die `taktPosition` wird beim `"STOP"` auf 0 zurückgesetzt (Neustart der Melodie)
- [ ] Die Melodien aller Instrumente passen harmonisch zusammen
- [ ] Das Tempo ist so gewählt, dass man die Melodie gut hören kann

### Mögliche Erweiterungen (für schnelle Paare)

**Tempo ändern:** Der Dirigent kann mit Taste A+B (gleichzeitig) das Tempo ändern. Der Beat-Wert wird als Zahl in `"START:500"` oder `"BEAT:500"` mitgesendet, die Musiker lesen ihn aus.

**Anzeige verbessern:** Die Musiker zeigen auf der LED-Matrix ihre Instrumentennummer als Symbol (z.B. Note, Herz, Stern), solange sie spielen.

**Lautstärke:** Der Calliope kann per Lagesensor (Neigung) die Lautstärke oder das Tempo beeinflussen.

**Runde anzeigen:** Der Takt-Zähler wird als kurzer Balken auf der LED-Matrix dargestellt (z.B. ein Pixel pro Takt).

### Zur Vorführung

Bereitet folgendes vor:
1. Erklärt kurz das Konzept (wer ist Dirigent, wie läuft die Aushandlung ab, wer spielt welche Stimme?).
2. Zeigt den Aushandlungsprozess live (alle Geräte gleichzeitig starten).
3. Der Dirigent startet – das Orchester spielt.
4. Zeigt eine Erweiterung, die ihr eingebaut habt.

---

## Anhang: Wichtige MakeCode-Blöcke auf einen Blick

| Was | Wo in MakeCode | Block |
|-----|----------------|-------|
| Funkgruppe setzen | Funk | `Funkgruppe setzen auf [42]` |
| Nachricht senden | Funk | `sende Zeichenkette [...]` |
| Nachricht empfangen | Funk | `wenn Funk-Zeichenkette empfangen` |
| Zufallszahl | Mathematik | `wähle zufällige Zahl zwischen [0] und [2]` |
| Text verbinden | Text | `verbinde [...] und [...]` |
| Liste erstellen | Arrays | `erstelle Array mit [...]` |
| Listenelement lesen | Arrays | `hole Wert an Position [...] aus [...]` |
| Listenlänge | Arrays | `Länge von [...]` |
| Note spielen | Musik | `spiele Note [...] für [...] Takt(e)` |
| Pause | Grundlagen | `pausiere (ms) [500]` |
| Dauerschleife | Grundlagen | `dauerhaft` |
| Eigene Funktion | Fortgeschritten → Funktionen | `Funktion erstellen` |

---

## Tipps für die Fehlersuche

**Geräte verstehen sich nicht:**  
→ Prüft, ob beide die **gleiche Funkgruppe** haben. Das ist der häufigste Fehler.

**Melodie startet versetzt:**  
→ Stellt sicher, dass `taktPosition` beim Empfang von `"START"` auf 0 gesetzt wird.

**Ton wird nicht gespielt:**  
→ Prüft, ob der Calliope einen Lautsprecher hat / angeschlossen ist. Im Simulator funktioniert Musik manchmal anders als auf dem echten Gerät.

**Aushandlung hört nicht auf:**  
→ Prüft, ob die Abbruchbedingung korrekt ist (z.B. läuft die Aushandlungsschleife auch dann noch, wenn schon alle Instrumente vergeben sind?).

**Alle spielen dasselbe Instrument:**  
→ Achtet darauf, dass jedes Gerät nach dem Senden seines Claims auch wirklich auf Gegennachrichten wartet, bevor es weiterläuft.
