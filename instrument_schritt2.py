# ============================================================
# 🎵 INSTRUMENT – Schritt 2
# Zwischen Instrumenten (Stimmen) per Knopfdruck wechseln
# ============================================================
#
# In diesem Schritt lernst du:
#   - Wie man mehrere Melodien (Stimmen) speichert
#   - Wie man per Taste A zwischen den Stimmen wechselt
#   - Wie man die aktuelle Stimmnummer auf dem Display zeigt
#
# Es gibt 4 Stimmen der Ode an die Freude:
#   Stimme 0 (Sopran)  – die Hauptmelodie, die jeder kennt
#   Stimme 1 (Alt)     – eine Terz tiefer als die Melodie
#   Stimme 2 (Tenor)   – tiefere Begleitung
#   Stimme 3 (Bass)    – Grundtöne, lange Schläge mit Pausen
# ============================================================

from microbit import *
import music

# ── Die vier Stimmen ─────────────────────────────────────────
#
# Jede Stimme ist eine eigene Liste von Frequenzen.
# Alle Stimmen haben dieselbe Anzahl von Noten und
# dieselben Dauern – so spielen sie später synchron.

# Stimme 0: Sopran – Hauptmelodie (Ode an die Freude)
sopran_noten = [329, 329, 349, 392, 392, 349, 329, 294, 261, 261, 294, 329, 329, 294, 294]
#               E4   E4   F4   G4   G4   F4   E4   D4   C4   C4   D4   E4   E4   D4   D4

# Stimme 1: Alt – eine Terz tiefer als die Sopranmelodie
alt_noten    = [261, 261, 294, 329, 329, 294, 261, 247, 220, 220, 247, 261, 261, 247, 247]
#               C4   C4   D4   E4   E4   D4   C4   H3   A3   A3   H3   C4   C4   H3   H3

# Stimme 2: Tenor – Harmonie-Begleitung eine Oktave tiefer
tenor_noten  = [196, 196, 220, 247, 247, 220, 196, 185, 165, 165, 185, 196, 196, 185, 185]
#               G3   G3   A3   H3   H3   A3   G3   F#3  E3   E3   F#3  G3   G3   F#3  F#3

# Stimme 3: Bass – tiefe Grundtöne mit Pausen (0 = Pause)
bass_noten   = [131,   0, 131,   0, 147,   0, 165,   0, 131,   0, 131,   0, 147,   0, 131]
#               C3  Pause  C3  Pause  D3  Pause  E3  Pause  C3  Pause  C3  Pause  D3  Pause  C3

# Dauern – gelten für alle Stimmen gleich
dauer = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 600, 200, 800]

# Alle vier Stimmen in einer Liste speichern
# → so können wir mit stimme[aktuelle_stimme] darauf zugreifen
alle_stimmen = [sopran_noten, alt_noten, tenor_noten, bass_noten]
stimmen_namen = ["S0", "S1", "S2", "S3"]  # Kurz-Bezeichnungen für das Display

# ── Aktuell gewählte Stimme ──────────────────────────────────
#
# Diese Variable merkt sich, welche Stimme gerade aktiv ist.
# Sie startet bei 0 (Sopran) und kann per Taste A geändert werden.

aktuelle_stimme = 0


# ── Funktion: Stimmnummer anzeigen ───────────────────────────

def zeige_stimme():
    """Zeigt die aktuelle Stimmnummer kurz auf dem Display."""
    display.scroll(stimmen_namen[aktuelle_stimme], delay=80)


# ── Funktion: Melodie spielen ────────────────────────────────

def spiele_melodie(stimmen_nr):
    """
    Spielt die Melodie der angegebenen Stimme ab.
    stimmen_nr: 0=Sopran, 1=Alt, 2=Tenor, 3=Bass
    """
    # Hole die passende Notenliste
    noten = alle_stimmen[stimmen_nr]

    display.show(Image.MUSIC_QUAVERS)

    for i in range(len(noten)):
        freq = noten[i]
        ms   = dauer[i]

        if freq == 0:
            music.stop()
            sleep(ms)
        else:
            music.pitch(freq, ms)

        sleep(30)

    display.show(Image.YES)
    sleep(600)
    display.clear()


# ── Hauptprogramm ────────────────────────────────────────────
#
# Taste A:  Stimme wechseln (0 → 1 → 2 → 3 → 0 → ...)
# Taste B:  Aktuelle Melodie einmal abspielen

display.scroll("S2", delay=80)  # "S2" = Schritt 2
zeige_stimme()

while True:

    # ── Taste A: Nächste Stimme wählen ──────────────────────
    #
    # Wir zählen aktuelle_stimme hoch.
    # Mit % 4 (Modulo 4) springen wir nach Stimme 3 wieder auf 0.
    #
    # Beispiel:
    #   0 → 1 → 2 → 3 → 0 → 1 → ...
    #   Das nennt man einen "Ringzähler".

    if button_a.was_pressed():
        aktuelle_stimme = (aktuelle_stimme + 1) % len(alle_stimmen)
        zeige_stimme()

    # ── Taste B: Aktuelle Melodie spielen ───────────────────
    if button_b.was_pressed():
        spiele_melodie(aktuelle_stimme)

    sleep(100)
