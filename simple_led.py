import RPi.GPIO as GPIO
import time

# GPIO pin beállítása, amelyhez a LED csatlakozik
LED_PIN = 18  # A GPIO18-at használjuk példaként

# GPIO mód beállítása
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def led_on():
    """Bekapcsolja a LED-et."""
    GPIO.output(LED_PIN, GPIO.HIGH)

def led_off():
    """Kikapcsolja a LED-et."""
    GPIO.output(LED_PIN, GPIO.LOW)

def main():
    try:
        while True:
            print("LED bekapcsol")
            led_on()
            time.sleep(1)  # LED világít 1 másodpercig

            print("LED kikapcsol")
            led_off()
            time.sleep(1)  # LED kikapcsolva 1 másodpercig
    except KeyboardInterrupt:
        print("Program leállítva.")
    finally:
        GPIO.cleanup()  # GPIO állapot visszaállítása

if __name__ == "__main__":
    main()
