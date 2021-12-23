import RPi.GPIO as GPIO
import time

BUZZER_PIN = 25
SWITCH_PIN = 18
LED_PIN = [16, 20, 21]


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
for i in range(3):
    GPIO.setup(LED_PIN[i], GPIO.OUT)
for i in LED_PIN:
    GPIO.output(i, GPIO.LOW) 

pwm = GPIO.PWM(BUZZER_PIN, 523)


try:
  while True:
      print(GPIO.input(SWITCH_PIN)) 
      if GPIO.input(SWITCH_PIN) == 1: 
        for i in LED_PIN:
            GPIO.output(i, GPIO.HIGH) 
        pwm.start(50)
        time.sleep(4)
        pwm.ChangeDutyCycle(0)
        for i in LED_PIN:
            GPIO.output(i, GPIO.LOW) 
finally: 
    pwm.stop()
    GPIO.cleanup()