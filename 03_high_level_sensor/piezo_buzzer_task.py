# pir.py
import RPi.GPIO


PIR_PIN = 

GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(5)
print('PIR Ready...')

try:
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:
            print('움직임 감지')
        else:
            print('움직임 없음')
        time
