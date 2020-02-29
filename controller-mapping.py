#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event3')

#button code variables (change to suit your device)
#if codes are improper, reference the "button mapping" spreadsheet in muh google drive
button1 = 288
button2 = 289
button3 = 290
button4 = 291

button5 = 292
button7 = 294
button6 = 293
button8 = 295

top_l = 296
top_r = ?


#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == button1:
                print("1")
            elif event.code == button2:
                print("2")
            elif event.code == button3:
                print("3")
            elif event.code == button4:
                print("4")

            elif event.code == button5:
                print("lbmp")
            elif event.code == button6:
                print("rbmp")
            elif event.code == button7:
                print("ltrig")
            elif event.code == button8:
                print("rtrig")

            elif event.code == start:
                print("start")
            elif event.code == select:
                print("select")

            elif event.code == lTrig:
                print("left bumper")
            elif event.code == rTrig:
                print("right bumper")
