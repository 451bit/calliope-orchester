# ============================================================
# 🎵 INSTRUMENT – Schritt 3  |  MakeCode-Python
# Auf den Dirigenten reagieren (Funk)
# ============================================================
#
# Taste A      → Stimme wechseln (solange nicht gespielt wird)
# Funk "START" → Melodie abspielen
# Funk "STOP"  → sofort aufhören
#
# WICHTIG: Alle Geräte müssen Gruppe 42 verwenden!
# ============================================================

# ── Funk einrichten ──────────────────────────────────────────
radio.set_group(42)
radio.set_transmit_power(7)

# ── Die vier Stimmen ─────────────────────────────────────────
sopran = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
alt    = [261, 261, 294, 329, 329, 294, 261, 247, 220, 220, 247, 261, 261, 247, 247]
tenor  = [196, 196, 220, 247, 247, 220, 196, 185, 165, 165, 185, 196, 196, 185, 185]
bass   = [131,   0, 131,   0, 147,   0, 165,   0, 131,   0, 131,   0, 147,   0, 131]
alle_stimmen = [sopran, alt, tenor, bass]
dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]

aktuelle_stimme = 0
stop_signal = False   # wird True wenn "STOP" empfangen wird


# ── Stimmnummer anzeigen ─────────────────────────────────────
def zeige_stimme():
    basic.show_number(aktuelle_stimme)
    basic.pause(600)
    basic.clear_screen()


# ── Melodie abspielen ────────────────────────────────────────
#
# stop_signal wird bei jeder Note geprüft.
# Kommt "STOP" per Funk, setzt on_received_string es auf True.
# break verlässt die Schleife sofort.

def spiele_melodie():
    global stop_signal
    stop_signal = False
    noten = alle_stimmen[aktuelle_stimme]
    basic.show_icon(IconNames.Music)

    for i in range(len(noten)):
        if stop_signal:
            break   # Schleife sofort verlassen

        freq = noten[i]
        ms = dauer[i]
        if freq == 0:
            music.rest(ms)
        else:
            music.play_tone(freq, ms)
        basic.pause(30)

    music.rest(1)
    basic.clear_screen()
    zeige_stimme()


# ── Taste A: Stimme wechseln ─────────────────────────────────
def on_button_pressed_a():
    global aktuelle_stimme
    aktuelle_stimme = (aktuelle_stimme + 1) % len(alle_stimmen)
    zeige_stimme()

input.on_button_pressed(Button.A, on_button_pressed_a)


# ── Funk: Nachrichten empfangen ──────────────────────────────
#
# radio.on_received_string() wird automatisch aufgerufen,
# sobald eine Funknachricht eingeht.
#
# "START" → Melodie starten
# "STOP"  → stop_signal auf True setzen → Schleife bricht ab

def on_received_string(receivedString: str):
    global stop_signal
    if receivedString == "START":
        stop_signal = False
        spiele_melodie()
    elif receivedString == "STOP":
        stop_signal = True

radio.on_received_string(on_received_string)


# ── Beim Start ───────────────────────────────────────────────
basic.show_string("S3", 80)
zeige_stimme()
