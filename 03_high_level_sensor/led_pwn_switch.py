import RPi.GPIO as GPIO
import time

LED_PIN = [16, 20, 21]
SWITCH_PIN = 18

GPIO.setmode(GPIO.BCM)

for i in range(3):
    GPIO.setup(LED_PIN[i], GPIO.OUT)

GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(SWITCH_PIN) == 1:
            for i in LED_PIN:
                GPIO.output(i, GPIO.HIGH) 
        else:
            for i in LED_PIN:
                GPIO.output(i, GPIO.LOW)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')