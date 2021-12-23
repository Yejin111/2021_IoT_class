import RPi.GPIO as GPIO
import time

SEGMENT_PIN = [7, 17, 22, 6, 26, 11, 27]
DIGIT_PIN = [12, 9, 4, 10]
SWITCH_PIN = 18
LED_PIN = [16, 20, 21]
BUZZER_PIN = 25

GPIO.setmode(GPIO.BCM)
for i in range(3):
    GPIO.setup(LED_PIN[i], GPIO.OUT)
for i in LED_PIN:
    GPIO.output(i, GPIO.LOW) 
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
for segment in SEGMENT_PIN :
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

for digit in DIGIT_PIN :
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)
pwm = GPIO.PWM(BUZZER_PIN, 523)

data = [[1, 1, 1, 1, 1, 1, 0], #0
        [0, 1, 1, 0, 0, 0, 0], #1
        [1, 1, 0, 1, 1, 0, 1], #2
        [1, 1, 1, 1, 0, 0, 1], #3
        [0, 1, 1, 0, 0, 1, 1], #4
        [1, 0, 1, 1, 0, 1, 1], #5
        [1, 0, 1, 1, 1, 1, 1], #6
        [1, 1, 1, 0, 0, 0, 0], #7
        [1, 1, 1, 1, 1, 1, 1], #8
        [1, 1, 1, 0, 0, 1, 1]] #9

def display(digit, number):
    for i in range(len(DIGIT_PIN)): 
        if i + 1 == digit:
            GPIO.output(DIGIT_PIN[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PIN[i], GPIO.HIGH)


    for i in range(len(SEGMENT_PIN)): 
        GPIO.output(SEGMENT_PIN[i], data[number][i])
    time.sleep(0.001)

try:
    while True:
        if GPIO.input(SWITCH_PIN) == 1:
            for i in LED_PIN:
                GPIO.output(i, GPIO.HIGH) 
            pwm.start(50)
            for i in range(1000):
                display(1, 1)
                display(2, 1)
                display(3, 9)
            pwm.ChangeDutyCycle(0)
            for i in LED_PIN:
                GPIO.output(i, GPIO.LOW)  
            
        GPIO.output(DIGIT_PIN[2], GPIO.LOW)
        for i in range(len(SEGMENT_PIN)): 
            GPIO.output(SEGMENT_PIN[i], GPIO.LOW)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 