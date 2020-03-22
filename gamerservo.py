# trying to control stuff via keyboard
import os #importing os library so as to communicate with the system 
import time 
from time import sleep #importing time library to make Rpi wait because its too impatient import RPi.GPIO as GPIO os.system 

os.system ("sudo pigpiod")

time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error 
import pigpio #importing GPIO library import RPi.GPIO as GPIO import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)                 #left  
GPIO.setup(19, GPIO.IN)                         #Right sensor connection
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP) #middle sensor connection

pwm=GPIO.PWM(03, 50) 
pwm.start(0)

def SetAngle(angle):

	duty = angle / 18 + 2

	GPIO.output(03, True)

	pwm.ChangeDutyCycle(duty)

	time.sleep(1)

	GPIO.output(03, False)

	pwm.ChangeDutyCycle(0)



SetAngle(60)

pwm.stop()

GPIO.cleanup()
