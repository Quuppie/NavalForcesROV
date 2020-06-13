from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0')  
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
p = GPIO.PWM(3, 50)
p.start(7.5)
deadl = 123
deadr = 132

last = {
    "ABS_Z": 128
}
eventcounter = 0
for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z':
            last["ABS_Z"] = absevent.event.value
        if last["ABS_Z"] > deadr: #and eventcounter % 5 == 0:
            print last["ABS_Z"]
            p.ChangeDutyCycle(int(last["ABS_Z"]*0.04705))
        elif last["ABS_Z"] < deadl: #and eventcounter % 5 == 0:
            print last["ABS_Z"]
            p.ChangeDutyCycle(int(last["ABS_Z"]*0.04705))

#while True:
#   dc = input("value from 1 to 12 ")
#   p.ChangeDutyCycle(dc)
#
p.stop()
GPIO.cleanup()
