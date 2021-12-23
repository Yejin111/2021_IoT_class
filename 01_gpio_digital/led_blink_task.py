import RPi.GPIO as GPIO
import time

LED_PIN_1 = 4
LED_PIN_2 = 17
LED_PIN_3 = 22



GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)


GPIO.output(LED_PIN_1, GPIO.HIGH)
print("led_RED on")
time.sleep(2) 
GPIO.output(LED_PIN_1, GPIO.LOW)
print("led_RED off")

GPIO.output(LED_PIN_2, GPIO.HIGH)
print("led_YELLOW on")
time.sleep(2) 
GPIO.output(LED_PIN_2, GPIO.LOW)
print("led_YELLOw off")

GPIO.output(LED_PIN_3, GPIO.HIGH)
print("led_GREEN on")
time.sleep(2) 
GPIO.output(LED_PIN_3, GPIO.LOW)
print("led_GREEN off")


GPIO.cleanup()