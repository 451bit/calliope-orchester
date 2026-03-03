# ============================================================
# 🎼 DIRIGENT – Calliope Mini Orchester
# ============================================================
#
# DEINE AUFGABE:
#   Programmiere den Dirigenten! Lies die TODOs unten und
#   fülle die Lücken aus. Die Kommentare erklären dir,
#   was du jeweils tun sollst.
#
# WAS DER DIRIGENT TUN SOLL:
#   - Beim Start: "DIR" auf dem Display anzeigen
#   - Taste A:    "START" per Funk senden, Pfeil-Symbol zeigen
#   - Taste B:    "STOP"  per Funk senden, Kreuz-Symbol zeigen
#   - Taste A+B:  Countdown 3→2→1, dann "START" senden
#
# WICHTIG:
#   Alle Geräte im Orchester müssen dieselbe Funkgruppe
#   verwenden! Wir nehmen Gruppe 42.
# ============================================================

from microbit import *
import radio

# ── Schritt 1: Funk einschalten und Gruppe setzen ───────────
# Der Calliope mini kann per Funk mit anderen Geräten
# kommunizieren – aber nur, wenn alle dieselbe Gruppe haben.

# TODO: Schalte den Funk ein
# radio.on()

# TODO: Setze die Funkgruppe auf 42
#       (Alle Instrumente müssen dieselbe Gruppe haben!)
# radio.config(group=???)


# ── Schritt 2: Begrüßung beim Start ─────────────────────────
# Beim Start soll das Display kurz "DIR" anzeigen,
# damit man weiß: dieses Gerät ist der Dirigent.

# TODO: Zeige "DIR" auf dem Display
# display.scroll(???)


# ── Hauptschleife ────────────────────────────────────────────
# Die while-True-Schleife läuft endlos. Darin prüfen wir
# immer wieder, ob eine Taste gedrückt wurde.

while True:

    # ── Taste A: Sofort starten ──────────────────────────────
    # Wenn Taste A gedrückt wird, schicken wir "START" an
    # alle Instrumente. Sie beginnen dann zu spielen.

    # TODO: Prüfe, ob Taste A (allein) gedrückt wurde
    #       Tipp: button_a.was_pressed() gibt True oder False zurück
    #             Aber: Taste A+B zählt hier NICHT!
    #             → du kannst das prüfen mit:
    #               button_a.was_pressed() and not button_b.is_pressed()
    if False:  # ← ersetze False durch deine Bedingung
        pass   # ← ersetze pass durch deinen Code

        # TODO: Sende "START" per Funk
        # radio.send(???)

        # TODO: Zeige ein Symbol (z. B. Pfeil nach oben)
        # display.show(Image.ARROW_N)
        # sleep(500)
        # display.clear()


    # ── Taste B: Stopp senden ────────────────────────────────
    # Wenn Taste B gedrückt wird, schicken wir "STOP".
    # Die Instrumente hören dann auf zu spielen.

    # TODO: Prüfe, ob Taste B gedrückt wurde
    if False:  # ← ersetze False durch deine Bedingung
        pass   # ← ersetze pass durch deinen Code

        # TODO: Sende "STOP" per Funk
        # radio.send(???)

        # TODO: Zeige ein "Nein"-Symbol
        # display.show(Image.NO)
        # sleep(500)
        # display.clear()


    # ── Taste A+B gleichzeitig: Countdown ───────────────────
    # Wenn beide Tasten gleichzeitig gedrückt werden,
    # zählen wir erst 3→2→1 herunter, dann geht's los.

    # TODO: Prüfe, ob Taste A UND Taste B gleichzeitig gedrückt sind
    #       Tipp: button_a.is_pressed() and button_b.is_pressed()
    if False:  # ← ersetze False durch deine Bedingung
        pass   # ← ersetze pass durch deinen Code

        # TODO: Countdown von 3 bis 1
        #       Tipp: Nutze eine for-Schleife mit range(3, 0, -1)
        #       Zeige die Zahl und warte jeweils 800 ms

        # TODO: Nach dem Countdown "START" senden (wie bei Taste A)


    # Kurze Pause, damit der Calliope nicht zu viel Strom verbraucht
    sleep(100)
