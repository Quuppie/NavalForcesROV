import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
p = GPIO.PWM(3, 50)
p.start(7.5)

a = range(2,13,1)
for dc in a: 
  print dc
  p.ChangeDutyCycle(dc)
  time.sleep(1) # sleep 1 second 
p.stop()
GPIO.cleanup()
