# ============================================================
# 🎵 INSTRUMENT – Vorlage  |  MakeCode-Python
# Melodie: Ode an die Freude (Sopranstimme)
# ============================================================
#
# Das hier ist dein Startpunkt.
# Die Noten sind schon bereit – als zwei Listen.
#
# DEINE AUFGABE (Schritt 1 in der Anleitung):
#   Schreibe eine for-Schleife, die alle Noten abspielt.
#   Schaue in der Anleitung nach, wie das geht.
#
# Wenn du fertig bist, schau dir instrument_schritt2 an:
#   → Stimme per Taste A wechseln
# ============================================================

# ── Noten der Sopranstimme (Ode an die Freude) ───────────────
#
#   noten[i] → Frequenz in Hz (Tonhöhe).  0 = Pause.
#   dauer[i] → Länge des Tons in ms.
#
# Beide Listen gehören zusammen: noten[i] und dauer[i].

noten = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
#  Ton:   E4   E4   F4   G4   G4   F4   E4   D4   C4   C4   D4   E4   E4   D4   D4

dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]


# ── TODO: Taste A → Melodie abspielen ────────────────────────
#
# Schreibe innerhalb der Funktion eine for-Schleife:
#
#   for i in range(len(noten)):
#       music.play_tone(noten[i], dauer[i])
#
def on_button_pressed_a():
    # Deine Schleife kommt hier rein!
    pass

input.on_button_pressed(Button.A, on_button_pressed_a)
