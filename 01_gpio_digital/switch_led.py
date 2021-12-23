#스위치로 LED 제어하기
import RPi.GPIO as GPIO

LED_PIN = 4
SWITCH_PIN = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
# 내부풀다운저항 사용
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True: 
        val = GPIO.input(SWITCH_PIN) #누르지 않았을 때 0, 눌렀을 떄 1
        print(val)
        GPIO.output(LED_PIN, val) # GPIO.HIGH = 1
finally:
    GPIO.cleanup()
    print('cleanup and exit')