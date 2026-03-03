# ============================================================
# 🎵 INSTRUMENT – Schritt 1
# Töne mit Dauer in der for-Schleife abspielen
# ============================================================
#
# In diesem Schritt lernst du:
#   - Wie man eine for-Schleife mit einem Index i nutzt
#   - Wie man mit music.pitch() einen Ton abspielt
#   - Was der Unterschied zwischen Frequenz und Dauer ist
#   - Wie man eine Pause (Frequenz 0) einbaut
#
# Am Ende spielt dein Calliope die Ode an die Freude!
# ============================================================

from microbit import *
import music

# ── Die Noten ────────────────────────────────────────────────
#
# Frequenz = Tonhöhe in Hz (Schwingungen pro Sekunde)
#   Beispiele:
#     261 Hz ≈ C4 (mittleres C)
#     294 Hz ≈ D4
#     329 Hz ≈ E4
#     349 Hz ≈ F4
#     392 Hz ≈ G4
#
# Dauer = wie lange der Ton klingt, in Millisekunden (ms)
#   400 ms = ein normaler Schlag
#   800 ms = doppelt so langer Schlag (Halbe Note)
#   200 ms = kurzer Schlag (Achtel)
#
# Beide Listen sind gleich lang und gehören zusammen:
#   note[i] und dauer[i] bilden immer eine Note.

noten = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
#  Ton:   E4   E4   F4   G4   G4   F4   E4   D4   C4   C4   D4   E4   E4   D4   D4

dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]


# ── Wie die for-Schleife funktioniert ───────────────────────
#
#   for i in range(len(noten)):
#
#   → range(len(noten)) erzeugt die Zahlen 0, 1, 2, ..., 14
#   → beim ersten Durchlauf ist i = 0
#   → beim zweiten Durchlauf ist i = 1
#   → ...
#   → beim letzten Durchlauf ist i = 14
#
#   In jedem Schritt greifen wir mit noten[i] auf die
#   aktuelle Note zu, und mit dauer[i] auf ihre Länge.


def spiele_melodie():
    """Spielt die gesamte Melodie einmal ab."""

    display.show(Image.MUSIC_QUAVERS)  # Symbol während des Spielens

    for i in range(len(noten)):

        freq = noten[i]   # Frequenz der aktuellen Note
        ms   = dauer[i]   # Dauer der aktuellen Note in ms

        if freq == 0:
            # Frequenz 0 bedeutet: Pause – kein Ton
            music.stop()
            sleep(ms)
        else:
            # music.pitch(frequenz, dauer_in_ms)
            # wait=True bedeutet: warte, bis der Ton fertig ist,
            # bevor du weitermachst (Standardverhalten)
            music.pitch(freq, ms)

        # Kleine Lücke zwischen den Noten (macht die Melodie klarer)
        sleep(30)

    display.show(Image.YES)  # ✓ nach dem Spielen
    sleep(800)
    display.clear()


# ── Hauptprogramm ────────────────────────────────────────────
#
# Der Calliope spielt die Melodie einmal beim Start,
# und dann immer wieder, wenn Taste A gedrückt wird.

display.scroll("S1", delay=80)  # "S1" = Schritt 1

while True:
    if button_a.was_pressed():
        spiele_melodie()

    sleep(100)
