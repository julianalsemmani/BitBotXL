leftOrRight = ["BBRobotDirection.LEFT", "BBRobotDirection.RIGHT"]
bitbot.led_rainbow()
basic.show_string("Hei")
music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
bitbot.go(BBDirection.FORWARD, 50)

def on_forever():
    basic.show_icon(IconNames.HAPPY)
    if bitbot.sonar(BBPingUnit.CENTIMETERS) < 15:
        bitbot.rotatems(BBRobotDirection.LEFT, 15, 2200)
        if bitbot.sonar(BBPingUnit.CENTIMETERS) < 5:
            bitbot.rotatems(BBRobotDirection.LEFT, 15, 2200)
    else:
        bitbot.go(BBDirection.FORWARD, 50)
basic.forever(on_forever)
