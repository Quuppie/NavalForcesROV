
#https://stackoverflow.com/questions/52124027/python-evdev-reading-axes-x-and-y-of-a-gamepad-simultaneously
from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0') 

delayvariable = 5

import os
import pigpio #importing GPIO library
import RPi.GPIO as GPIO
import time
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error

#recentvalue = stickvalue
GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)                 #left  
GPIO.setup(19, GPIO.IN)                         #Right sensor connection
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) #middle sensor connection

pwm=GPIO.PWM(03, 50)
pwm.start(0)

# Set sensitivity
deadl = 123
deadr = 132
deadup = 123
deaddn = 132



#Angle




def SetAngle(angle):
    duty = angle #/ 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(.1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)
	
    pwm.stop()

last = {
    "ABS_Z": 128
}
eventcounter = 0
delayconfig = 10
for event in gamepad.read_loop(): 
    if event.type == ecodes.EV_ABS: 
        absevent = categorize(event) 
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z': 
            last["ABS_Z"] = absevent.event.value
	
        if last["ABS_Z"] > deadr: #and eventcounter % 4 == 0: 
            print last["ABS_Z"] 
# set a new angle
        elif last["ABS_Z"] < deadl: #and eventcounter % 5 == 0: 
            print last["ABS_Z"]
# set a new angle
	stickvalue = (int(last["ABS_Z"]))
	SetAngle(int(stickvalue / 2.83))   

GPIO.cleanup()
