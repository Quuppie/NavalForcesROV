from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0')  
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
p = GPIO.PWM(3, 50)
p.start(7.5)

while True:
   dc = input("value from 1 to 12 ")
   p.ChangeDutyCycle(dc)

p.stop()
GPIO.cleanup()
