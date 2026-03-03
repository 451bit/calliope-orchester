# ============================================================
# 🎵 INSTRUMENT – Vorlage
# Melodie: Ode an die Freude (Hauptmelodie / Sopran)
# ============================================================
#
# Das hier ist dein Startpunkt.
# Die Noten der Ode an die Freude sind schon vorbereitet –
# als zwei Listen: eine mit Frequenzen, eine mit Dauern.
#
# DEINE AUFGABE (→ sieh dir Schritt 1 in der Anleitung an):
#   Bringe die Noten zum Klingen!
#   Schreibe eine for-Schleife, die alle Noten der Reihe
#   nach abspielt.
# ============================================================

from microbit import *
import music

# ── Die Melodie ──────────────────────────────────────────────
#
# Jede Note wird durch zwei Werte beschrieben:
#
#   noten[i] → Frequenz in Hertz (Hz)
#              Das ist die Tonhöhe. Höhere Zahl = höherer Ton.
#              0 bedeutet: Pause (kein Ton)
#
#   dauer[i] → Wie lange die Note klingt, in Millisekunden (ms)
#              400 ms = ca. ein Viertelton im Takt
#
# Beide Listen gehören zusammen: Note i und Dauer i
# ergeben zusammen einen Schlag der Melodie.

noten = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
#  Ton:   E4   E4   F4   G4   G4   F4   E4   D4   C4   C4   D4   E4   E4   D4   D4

dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]
#         ♩    ♩    ♩    ♩    ♩    ♩    ♩    ♩    ♩    ♩    ♩    ♩    ♩.   ♪   𝅗𝅥

# Anzahl der Noten (wird automatisch berechnet)
anzahl_noten = len(noten)

# ── TODO: Spiele die Melodie ─────────────────────────────────
#
# Schreibe hier eine for-Schleife, die alle Noten abspielt.
# → Schau dir die Erklärung in der Anleitung (Schritt 1) an!
#
# Tipp für den Anfang:
#   for i in range(anzahl_noten):
#       # Hier kannst du mit noten[i] und dauer[i] arbeiten

while True:
    # Hier kommt deine Schleife rein!
    sleep(1000)
