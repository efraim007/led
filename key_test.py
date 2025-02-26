import pygame

pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Billentyűzet teszt")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  # Billentyű lenyomása
            print(f"Lenyomott billentyű: {pygame.key.name(event.key)}")
            if event.key == pygame.K_q:  # 'Q' lenyomására kilép
                running = False

pygame.quit()
