randomNumber = randint(0, 1)
bitbot.led_rainbow()
basic.show_string("HEI")
music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
bitbot.go(BBDirection.FORWARD, 50)

def on_forever():
    global randomNumber
    randomNumber = randint(0, 1)
    bitbot.bb_bias(BBRobotDirection.LEFT, 10)
    basic.show_icon(IconNames.HAPPY)
    if bitbot.sonar(BBPingUnit.CENTIMETERS) < 5:
        bitbot.goms(BBDirection.REVERSE, 50, 500)
    elif bitbot.sonar(BBPingUnit.CENTIMETERS) < 13:
        bitbot.stop(BBStopMode.BRAKE)
        if randomNumber == 0:
            bitbot.rotatems(BBRobotDirection.LEFT, 22, 1200)
        elif randomNumber == 1:
            bitbot.rotatems(BBRobotDirection.RIGHT, 22, 1200)
    else:
        bitbot.go(BBDirection.FORWARD, 50)
basic.forever(on_forever)
