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
	SetAngle(int(inp))
#        if inp == "0":
#		SetAngle(0)
#        elif inp == "30":
#		SetAngle(30)
#        elif inp == "38":
#		SetAngle(38)
#        elif inp == "76":
#		SetAngle(76)
#        elif inp == "60":
#		SetAngle(60)
#        elif inp == "90":
#		SetAngle(90)

pwm.stop()

GPIO.cleanup()


