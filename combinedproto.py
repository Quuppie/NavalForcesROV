#https://stackoverflow.com/questions/52124027/python-evdev-reading-axes-x-and-y-of-a-gamepad-simultaneously
from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0') 


import os
import pigpio #importing GPIO library
import RPi.GPIO as GPIO
import time
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error

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



Joystick




def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

while True:
    i=GPIO.input(15)                         #Reading output of right IR sensor
    j=GPIO.input(37)  
    y=GPIO.input(19)
    if i==1:                                #Left IR sensor detects an object
        print("Obstacle detected on Left"),i
        SetAngle(10)
        time.sleep(0.1)
    if j==1:                                #Right IR sensor detects an object
                print("Obstacle detected on Right"),j
                SetAngle(90)
        time.sleep(0.1)

    if y==1:                                #Middle IR sensor detects an object
                print("Maintain heading"),y
                SetAngle(50)
        time.sleep(0.1)

#while True:
    print "type a number - 0, 30 ,38, 60,76, 90"
    inp = raw_input()
#    SetAngle(int(inp))
    SetAngle(int(last["ABS_Z"]))

pwm.stop()

GPIO.cleanup()


last = {
    "ABS_RZ": 128,
    "ABS_Z": 128,
    "ABS_HAT0Y": 128,
    "ABS_HAT0X": 128,
    "ABS_Y": 128,
    "ABS_X": 128
}
for event in gamepad.read_loop(): 
    if event.type == ecodes.EV_ABS: 
        absevent = categorize(event) 


        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z': 
            last["ABS_Z"] = absevent.event.value
  

        if last["ABS_Z"] > deadr : 
            print 'r_right' 
            print last["ABS_Z"] 
        elif last["ABS_Z"] < deadl: 
            print 'r_left' 
            print last["ABS_Z"]
