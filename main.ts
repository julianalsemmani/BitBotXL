let randomNumber = randint(0, 1)
bitbot.ledRainbow()
basic.showString("HEI")
music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
bitbot.go(BBDirection.Forward, 50)
basic.forever(function () {
    randomNumber = randint(0, 1)
    bitbot.BBBias(BBRobotDirection.Left, 10)
    basic.showIcon(IconNames.Happy)
    if (bitbot.sonar(BBPingUnit.Centimeters) < 5) {
        bitbot.goms(BBDirection.Reverse, 50, 500)
    } else if (bitbot.sonar(BBPingUnit.Centimeters) < 13) {
        bitbot.stop(BBStopMode.Brake)
        if (randomNumber == 0) {
            bitbot.rotatems(BBRobotDirection.Left, 22, 1200)
        } else if (randomNumber == 1) {
            bitbot.rotatems(BBRobotDirection.Right, 22, 1200)
        }
    } else {
        bitbot.go(BBDirection.Forward, 50)
    }
})
