# servo_motor.py
import RPi.GPIO as GPIO
import time

SEVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SEVO_PIN, GPIO.OUT)

# 주파수 : 50Hz
pwm = GPIO.PWM(SEVO_PIN, 50)
pwm.start(7.5) # 0도

try:
    while True:
        val = input('1: 0eh, 2: -90eh, 3: +90eh, 9: Exit >')
        if val == '1': 
            pwm.ChangeCUtyCycle(7.5) # 0도
        elif val == '2': 
            #pwm.ChangeCUtyCycle(5) # -45도
            pwm.ChangeCUtyCycle(2.5) # -90도
        elif val == '3': 
            #pwm.ChangeCUtyCycle(10) # +45도
            pwm.ChangeCUtyCycle(12.5) # +90도
        elif val == '9': 
            break
finally:
    pwm.stop()
    GPIO.cleanup()
