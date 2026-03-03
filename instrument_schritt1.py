# ============================================================
# 🎵 INSTRUMENT – Schritt 1  |  MakeCode-Python
# Töne mit Dauer in der for-Schleife abspielen
# ============================================================
#
# Drücke Taste A → die Melodie wird einmal abgespielt.
#
# In diesem Schritt siehst du:
#   - wie die for-Schleife mit Index i funktioniert
#   - wie music.play_tone(freq, ms) einen Ton abspielt
#   - wie Pausen (Frequenz 0) behandelt werden
# ============================================================

# ── Die Noten ────────────────────────────────────────────────
#
# Frequenz = Tonhöhe in Hertz (Hz):
#   261 = C4   294 = D4   329 = E4   349 = F4   392 = G4
#
# Dauer in Millisekunden (ms):
#   400 ms = normaler Schlag  |  800 ms = langer Schlag
#
# Beide Listen gehören zusammen: noten[i] + dauer[i] = eine Note.

noten = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
#  Ton:   E4   E4   F4   G4   G4   F4   E4   D4   C4   C4   D4   E4   E4   D4   D4

dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]


# ── Funktion: Melodie abspielen ──────────────────────────────
#
# Die for-Schleife zählt i von 0 bis 14 (= len(noten)-1).
#
#   range(len(noten)) erzeugt: 0, 1, 2, 3, …, 14
#
#   noten[i]  → die i-te Frequenz (Indexzugriff)
#   dauer[i]  → die i-te Dauer
#
# music.play_tone(freq, ms) – spielt freq Hz für ms Millisekunden.
# music.rest(ms)            – Stille für ms Millisekunden.

def spiele_melodie():
    basic.show_icon(IconNames.Music)

    for i in range(len(noten)):
        freq = noten[i]
        ms = dauer[i]

        if freq == 0:
            # Frequenz 0 bedeutet Pause
            music.rest(ms)
        else:
            music.play_tone(freq, ms)

        # Kurze Lücke zwischen den Noten
        basic.pause(30)

    basic.show_icon(IconNames.Yes)
    basic.pause(800)
    basic.clear_screen()


# ── Taste A: Melodie starten ─────────────────────────────────
def on_button_pressed_a():
    spiele_melodie()

input.on_button_pressed(Button.A, on_button_pressed_a)

# Hinweis beim Start
basic.show_string("S1", 80)
