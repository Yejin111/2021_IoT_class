import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 (262Hz)
pwm =  GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0~100)

# 도레미파솔라시도 주파수
melody = [392, 392, 440, 440, 392, 392, 330]
melody2 = [392, 392, 330, 330, 294]
melody3 = [392, 330, 294, 330, 262]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody2:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    time.sleep(0.7)
    for i in melody3:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)


finally:
    pwm.stop()
    GPIO.cleanup()