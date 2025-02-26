import pygame
from gpiozero import PWMLED
import time

green_led = PWMLED(20)  # Zöld LED a GPIO 20 pinhez

pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Billentyűzet teszt")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  # Billentyű lenyomása
            print(f"Lenyomott billentyű: {pygame.key.name(event.key)}")
            
            
            if event.key == pygame.K_a:  # 'a' lenyomására Zöld led
                green_led.value = 1  # Zöld LED bekapcsolása
                time.sleep(5)
                green_led.value = 0  # Zöld LED bekapcsolása


            if event.key == pygame.K_q:  # 'Q' lenyomására kilép
                running = False

pygame.quit()
