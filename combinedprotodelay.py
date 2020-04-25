
#https://stackoverflow.com/questions/52124027/python-evdev-reading-axes-x-and-y-of-a-gamepad-simultaneously
from evdev import InputDevice, categorize, ecodes, KeyEvent 
gamepad = InputDevice('/dev/input/event0') 


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
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(.1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)
	
    pwm.stop()
#for a in [10,20,30,40,50,60]:
#	SetAngle(a)
#a = ""
#while a != "exit":
#	a = input("type an angle")
#	SetAngle(a)

#while True:
print "let's hope this thing works"
#    print last["ABS_Z"]
    #print (ins)
#    inp = raw_input()
#    SetAngle(int(inp)) 
#    SetAngle(int(last["ABS_Z"]))  #It looks like we can't have parentheses and brackets enclosing each other, because it does some sort of super function
#    SetAngle("ins")



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
  

        if last["ABS_Z"] > deadr: #and eventcounter % 5 == 0: 
            print 'r_right' 
            print last["ABS_Z"] 
            eventcounter = 0
        elif last["ABS_Z"] < deadl: #and eventcounter % 5 == 0: 
            print 'r_left' 
            print last["ABS_Z"]
            eventcounter = 0
        #eventcounter = eventcounter + 1 
	#print ("eventcounter: " + str(eventcounter))
        #print ("Angle: " + str(eventcounter))
	#making a variable holding the value thingy
	stickvalue = (int(last["ABS_Z"]))
	#so, here I'm trying to make a delay variable thing

	delayvariable = 0 
	time.sleep(0.2)
	delayvariable = 1
	time.sleep(0.2)


#	if abs(int(stickvalue) - recentvalue) < 10:
#		SetAngle(recentvalue)
	if delayvariable==1:
		SetAngle(int(stickvalue / 2.83))   


#SetAngle(int(last["ABS_Z"]))
 #   print("My angle is " + str(int(last["ABS_Z"])))

#	print "code is no more"

GPIO.cleanup()
