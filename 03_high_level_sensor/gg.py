import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 25
sw = 18
scale = 523

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(sw, GPIO.IN) 
p = GPIO.PWM(buzzer, 100)

list = 8
try:
while 1: 
    if GPIO.input(sw) == 1:
        p.start(100)
time.sleep(0.5)
p.stop() #pwm 종료
except KeyboardInterrupt: #ctrl+c->종료
GPIO.cleanup()