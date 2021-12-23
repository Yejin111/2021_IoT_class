from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

RED_LED_PIN = 4
BLUE_LED_PIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)


@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color,op):
    if op == "on" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif op == "off" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        '''
    elif op == "on" and color == "blue":
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
        return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif op == "off" and color == "blue":
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)
        return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''

if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()