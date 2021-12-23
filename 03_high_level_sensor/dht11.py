import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN=17

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            print(f"Temperature={temperature:.1f}C, humidity:{humidity:.1f}%")
        else:
            print('Read error')
        time.sleep(1)

finally:
    print("End of Program")