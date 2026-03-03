# ============================================================
# 🎵 INSTRUMENT – Schritt 2  |  MakeCode-Python
# Zwischen Stimmen per Taste A wechseln
# ============================================================
#
# Taste A → nächste Stimme wählen  (0 → 1 → 2 → 3 → 0 → …)
# Taste B → aktuelle Stimme abspielen
#
# Stimme 0: Sopran  – Hauptmelodie
# Stimme 1: Alt     – eine Terz tiefer
# Stimme 2: Tenor   – tiefe Harmonie
# Stimme 3: Bass    – Grundtöne mit Pausen
# ============================================================

# ── Die vier Stimmen ─────────────────────────────────────────
sopran = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
alt    = [261, 261, 294, 329, 329, 294, 261, 247, 220, 220, 247, 261, 261, 247, 247]
tenor  = [196, 196, 220, 247, 247, 220, 196, 185, 165, 165, 185, 196, 196, 185, 185]
bass   = [131,   0, 131,   0, 147,   0, 165,   0, 131,   0, 131,   0, 147,   0, 131]

# Liste von Listen – alle_stimmen[0] = sopran usw.
alle_stimmen = [sopran, alt, tenor, bass]

# Dauern – für alle Stimmen gleich
dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]

# Aktuell gewählte Stimme
aktuelle_stimme = 0


# ── Stimmnummer anzeigen ─────────────────────────────────────
def zeige_stimme():
    basic.show_number(aktuelle_stimme)
    basic.pause(600)
    basic.clear_screen()


# ── Melodie der gewählten Stimme abspielen ───────────────────
#
# alle_stimmen[aktuelle_stimme] liefert die jeweilige Notenliste.
# Die Schleife läuft genauso wie in Schritt 1.

def spiele_melodie():
    noten = alle_stimmen[aktuelle_stimme]
    basic.show_icon(IconNames.Music)

    for i in range(len(noten)):
        freq = noten[i]
        ms = dauer[i]
        if freq == 0:
            music.rest(ms)
        else:
            music.play_tone(freq, ms)
        basic.pause(30)

    basic.show_icon(IconNames.Yes)
    basic.pause(600)
    basic.clear_screen()
    zeige_stimme()


# ── Taste A: Stimme wechseln (Ringzähler mit %) ──────────────
#
# (aktuelle_stimme + 1) % 4 springt nach 3 wieder auf 0:
#   0 → 1 → 2 → 3 → 0 → 1 → …
#
# "global" wird gebraucht, weil aktuelle_stimme hier verändert
# wird (sie ist außerhalb der Funktion definiert).

def on_button_pressed_a():
    global aktuelle_stimme
    aktuelle_stimme = (aktuelle_stimme + 1) % len(alle_stimmen)
    zeige_stimme()

input.on_button_pressed(Button.A, on_button_pressed_a)


# ── Taste B: Aktuelle Stimme abspielen ───────────────────────
def on_button_pressed_b():
    spiele_melodie()

input.on_button_pressed(Button.B, on_button_pressed_b)


# Beim Start
basic.show_string("S2", 80)
zeige_stimme()
