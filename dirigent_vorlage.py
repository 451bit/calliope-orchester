# ============================================================
# 🎼 DIRIGENT – Calliope Mini Orchester  |  MakeCode-Python
# ============================================================
#
# DEINE AUFGABE:
#   Importiere diese Datei in MakeCode (makecode.calliope.cc):
#   Neues Projekt → Python-Ansicht → Code einfügen.
#   Ergänze die fehlenden TODO-Stellen.
#   Du kannst jederzeit in die Blöcke-Ansicht wechseln!
#
# WAS DER DIRIGENT TUN SOLL:
#   - Beim Start:  "DIR" auf dem Display anzeigen
#   - Taste A:     "START" senden → alle Instrumente spielen
#   - Taste B:     "STOP" senden  → alle hören auf
#   - Taste A+B:   Countdown 3→2→1, dann "START" senden
#
# WICHTIG: Alle Geräte müssen dieselbe Funkgruppe nutzen!
#          Wir verwenden Gruppe 42.
# ============================================================


# ── Funk einrichten ──────────────────────────────────────────
# TODO: Setze die Funkgruppe auf 42
# radio.set_group(???)

# TODO: Zeige beim Start "DIR" auf dem Display
# basic.show_string("???")


# ── Taste A: Startsignal senden ──────────────────────────────
def on_button_pressed_a():
    # TODO: Sende "START" per Funk
    # radio.send_string("???")

    # TODO: Zeige ein Symbol (z. B. Pfeil nach oben)
    # basic.show_icon(IconNames.ArrowNorth)
    # basic.pause(500)
    # basic.clear_screen()
    pass

input.on_button_pressed(Button.A, on_button_pressed_a)


# ── Taste B: Stoppsignal senden ──────────────────────────────
def on_button_pressed_b():
    # TODO: Sende "STOP" per Funk
    # radio.send_string("???")

    # TODO: Zeige ein Stopp-Symbol
    # basic.show_icon(IconNames.No)
    # basic.pause(500)
    # basic.clear_screen()
    pass

input.on_button_pressed(Button.B, on_button_pressed_b)


# ── Taste A+B: Countdown, dann starten ──────────────────────
def on_button_pressed_ab():
    # TODO: Countdown von 3 bis 1
    #   Tipp: for i in range(3, 0, -1):
    #             basic.show_number(i)
    #             basic.pause(800)
    #         basic.clear_screen()

    # TODO: Dann "START" senden (wie bei Taste A)
    pass

input.on_button_pressed(Button.AB, on_button_pressed_ab)
