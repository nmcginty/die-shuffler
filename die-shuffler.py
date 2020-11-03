import RPi.GPIO as GPIO                     
import time
import os
import sys
import subprocess

dice_kind = sys.argv[1]


def captureImage():
    face = int(input("Enter dice roll:"))
    print(f"{dice_kind}_{face}")                
    os.system(f"sudo ./camera.sh {dice_kind} {face}")

servoPIN = 17                               
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)              
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(10) # Initialization
time.sleep(1)

try:
  while True:
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(6.75)
    time.sleep(0.5)
    p.ChangeDutyCycle(6)
    time.sleep(0.5)
    p.ChangeDutyCycle(6.5)
    #p.ChangeDutyCycle(6.75)
    time.sleep(0.5)
    captureImage()
    p.ChangeDutyCycle(10)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
