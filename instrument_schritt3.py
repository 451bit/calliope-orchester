# ============================================================
# 🎵 INSTRUMENT – Schritt 3
# Auf den Dirigenten reagieren (Funk-Empfang)
# ============================================================
#
# In diesem Schritt lernst du:
#   - Wie man per Funk Nachrichten empfängt
#   - Wie man auf "START" und "STOP" reagiert
#   - Wie man Taste A zum Stimme-Wechseln beibehält
#   - Wie das fertige Orchester-Programm aussieht
#
# ABLAUF IM ORCHESTER:
#   1. Alle Instrumente starten → jeder wählt seine Stimme
#   2. Solange: Taste A → Stimme wechseln, Display zeigt Nummer
#   3. Dirigent drückt Taste A → sendet "START"
#   4. Alle Instrumente spielen ihre Melodie
#   5. Dirigent drückt Taste B → sendet "STOP"
#   6. Alle Instrumente hören auf
#
# FUNKGRUPPE:
#   Alle Geräte (Dirigent + Instrumente) müssen dieselbe
#   Gruppe haben: Gruppe 42
# ============================================================

from microbit import *
import radio
import music

# ── Funk einschalten ─────────────────────────────────────────
radio.on()
radio.config(group=42, power=7)
# group=42  → alle im Orchester nutzen diese Gruppe
# power=7   → maximale Sendeleistung (Reichweite)


# ── Die vier Stimmen ─────────────────────────────────────────

sopran_noten = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
alt_noten    = [261, 261, 294, 329, 329, 294, 261, 247, 220, 220, 247, 261, 261, 247, 247]
tenor_noten  = [196, 196, 220, 247, 247, 220, 196, 185, 165, 165, 185, 196, 196, 185, 185]
bass_noten   = [131,   0, 131,   0, 147,   0, 165,   0, 131,   0, 131,   0, 147,   0, 131]

dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]

alle_stimmen  = [sopran_noten, alt_noten, tenor_noten, bass_noten]
stimmen_namen = ["S0", "S1", "S2", "S3"]


# ── Zustandsvariablen ────────────────────────────────────────
#
# aktuelle_stimme: welche Stimme gerade aktiv ist (0–3)
# spielt:          True → Melodie wird gerade gespielt
#                  False → wir warten auf "START"

aktuelle_stimme = 0
spielt          = False


# ── Funktion: Stimmnummer anzeigen ───────────────────────────

def zeige_stimme():
    display.scroll(stimmen_namen[aktuelle_stimme], delay=80)


# ── Funktion: Melodie spielen ────────────────────────────────
#
# Diese Funktion prüft in der inneren Schleife regelmäßig,
# ob eine "STOP"-Nachricht empfangen wurde.
# Falls ja, bricht sie die Melodie sofort ab.

def spiele_melodie(stimmen_nr):
    """
    Spielt die Melodie der gewählten Stimme.
    Bricht ab, wenn "STOP" empfangen wird.
    """
    global spielt

    noten = alle_stimmen[stimmen_nr]
    display.show(Image.MUSIC_QUAVERS)

    for i in range(len(noten)):

        # ── Zwischendurch auf STOP prüfen ───────────────────
        # radio.receive() gibt None zurück, wenn nichts empfangen,
        # oder den empfangenen Text als String.
        nachricht = radio.receive()
        if nachricht == "STOP":
            spielt = False
            break   # Schleife sofort verlassen

        freq = noten[i]
        ms   = dauer[i]

        if freq == 0:
            music.stop()
            sleep(ms)
        else:
            music.pitch(freq, ms)

        sleep(30)

    music.stop()
    display.clear()
    zeige_stimme()


# ── Startsequenz ─────────────────────────────────────────────

display.scroll("S3", delay=80)   # "S3" = Schritt 3
zeige_stimme()


# ── Hauptschleife ────────────────────────────────────────────
#
# Wenn nicht gespielt wird:
#   → Taste A: Stimme wechseln
#   → Funk:    auf "START" warten
#
# Wenn gespielt wird:
#   → spiele_melodie() läuft und prüft selbst auf "STOP"

while True:

    if not spielt:
        # ── Stimme wechseln per Taste A ─────────────────────
        if button_a.was_pressed():
            aktuelle_stimme = (aktuelle_stimme + 1) % len(alle_stimmen)
            zeige_stimme()

        # ── Funk-Empfang: auf "START" warten ────────────────
        #
        # radio.receive() gibt None zurück, wenn nichts da ist.
        # Wir prüfen nur, wenn tatsächlich etwas empfangen wurde.

        nachricht = radio.receive()

        if nachricht == "START":
            # Der Dirigent hat das Startzeichen gegeben!
            spielt = True
            display.show(Image.ARROW_N)
            sleep(200)
            display.clear()
            spiele_melodie(aktuelle_stimme)
            # Nach dem Spielen: bereit für den nächsten START
            spielt = False

    sleep(50)   # kurze Pause, um Strom zu sparen
