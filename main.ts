let leftOrRight = ["BBRobotDirection.LEFT", "BBRobotDirection.RIGHT"]
bitbot.ledRainbow()
basic.showString("Hei")
music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
bitbot.go(BBDirection.Forward, 50)
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
    if (bitbot.sonar(BBPingUnit.Centimeters) < 15) {
        bitbot.rotatems(BBRobotDirection.Left, 15, 2200)
    } else {
        if (bitbot.sonar(BBPingUnit.Centimeters) < 5) {
            bitbot.rotatems(BBRobotDirection.Right, 15, 4400)
        }
    }
})
