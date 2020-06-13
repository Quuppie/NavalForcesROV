import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
p = GPIO.PWM(3, 50)
p.start(7.5)

from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0')

for event in gamepad.read_loop(): 
    if event.type == ecodes.EV_ABS: 
        absevent = categorize(event)

while True:
   dc = int(absevent.event.value) 
   p.ChangeDutyCycle(dc)

p.stop()
GPIO.cleanup()
