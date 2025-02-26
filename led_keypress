from gpiozero import LED
import keyboard
import time

# LED csatlakoztatva a 17-es GPIO pinre
led = LED(17)

print("Nyomd meg az 'A' billentyűt a LED felkapcsolásához!")

while True:
    try:
        if keyboard.is_pressed("a"):
            print("LED bekapcsolva!")
            led.on()
            time.sleep(5)  # 5 másodpercig világít
            led.off()
            print("LED kikapcsolva!")
    except KeyboardInterrupt:
        print("\nKilépés...")
        break
