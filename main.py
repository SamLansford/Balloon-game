import pygame


pygame.init()

WIDTH = 400
HEIGHT = 450

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ballon Game")

FPS = 60

clock = pygame.time.Clock()

Start = True

while Start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

window.fill(255, 0 ,0)

pygame.display.update()

clock.tick(FPS)