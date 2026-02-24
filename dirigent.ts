// ============================================================
// 🎼 DIRIGENT – Calliope Mini Orchester
// Melodie: Ode an die Freude (4 Stimmen)
// Funkgruppe: 42
// ============================================================
//
// BEDIENUNG:
//   Taste A:   Startsignal sofort an alle Instrumente senden
//   Taste B:   Stoppsignal senden
//   Taste A+B: Countdown 3-2-1, dann starten
// ============================================================

let laeuft = false

// ----- Beim Start -----
radio.setGroup(42)
radio.setTransmitPower(7)

basic.showIcon(IconNames.Diamond)
basic.pause(1000)
basic.clearScreen()
basic.showString("DIR")
basic.pause(500)
basic.clearScreen()

// ----- Taste A: Sofort starten -----
input.onButtonPressed(Button.A, function () {
    if (!laeuft) {
        laeuft = true
        basic.showIcon(IconNames.ArrowNorth)
        radio.sendString("START")
        basic.pause(200)
        basic.clearScreen()
        basic.showIcon(IconNames.Music)
        // Warte grob so lange wie die Melodie dauert (~10 Sekunden)
        basic.pause(10000)
        basic.clearScreen()
        basic.showIcon(IconNames.Yes)
        basic.pause(1000)
        basic.clearScreen()
        laeuft = false
    }
})

// ----- Taste B: Stopp senden -----
input.onButtonPressed(Button.B, function () {
    radio.sendString("STOP")
    laeuft = false
    basic.showIcon(IconNames.No)
    basic.pause(500)
    basic.clearScreen()
})

// ----- Taste A+B: Countdown, dann starten -----
input.onButtonPressed(Button.AB, function () {
    if (!laeuft) {
        // Countdown 3-2-1
        for (let i = 3; i >= 1; i--) {
            basic.showNumber(i)
            basic.pause(800)
        }
        basic.clearScreen()
        laeuft = true
        basic.showIcon(IconNames.ArrowNorth)
        radio.sendString("START")
        basic.pause(200)
        basic.clearScreen()
        basic.showIcon(IconNames.Music)
        basic.pause(10000)
        basic.clearScreen()
        basic.showIcon(IconNames.Yes)
        basic.pause(1000)
        basic.clearScreen()
        laeuft = false
    }
})

// ----- Funk: Empfang (Statusmeldungen von Instrumenten) -----
radio.onReceivedString(function (receivedString) {
    // Dirigent empfaengt keine relevanten Nachrichten im Grundbetrieb
    // Hier koennte man z.B. Rueckmeldungen der Instrumente verarbeiten
})
