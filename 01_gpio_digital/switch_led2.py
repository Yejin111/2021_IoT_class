#스위치로 LED 제어하기
import RPi.GPIO as GPIO
import time

LED_PIN = [16, 20, 21]
SWITCH_PIN = [18]
val = [0, 0, 0]

GPIO.setmode(GPIO.BCM)

for i in range(3):
    GPIO.setup(LED_PIN[i], GPIO.OUT)
    GPIO.setup(SWITCH_PIN[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
    while True: 
        for i in range(3):
            val[i] = GPIO.input(SWITCH_PIN[i]) #누르지 않았을 때 0, 눌렀을 떄 1
            print(val)
            GPIO.output(LED_PIN[i], val[i]) # GPIO.HIGH = 1
            time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
