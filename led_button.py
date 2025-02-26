import RPi.GPIO as GPIO
import time

led_pin = 17  # A LED a 17-es GPIO lábon van
vcc_pin = 17 # VCC pin
gnd_pin = 9 # GND pin
scl_pin = 3  # GPIO3
sda_pin = 2  # GPIO2

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(scl_pin, GPIO.IN)
GPIO.setup(sda_pin, GPIO.IN)

try:
    while True:
        # SCL ellenőrzése
        if GPIO.input(scl_pin) == GPIO.HIGH:
            GPIO.output(led_pin, GPIO.HIGH)
            print("SCL HIGH")
            time.sleep(0.5)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.5)
        else:
            print("SCL LOW")
            time.sleep(1)

        # SDA ellenőrzése
        if GPIO.input(sda_pin) == GPIO.HIGH:
            GPIO.output(led_pin, GPIO.HIGH)
            print("SDA HIGH")
            time.sleep(0.5)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.5)
        else:
            print("SDA LOW")
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
