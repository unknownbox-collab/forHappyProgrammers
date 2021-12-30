import pygame,sys

pygame.init()
pygame.display.set_caption("~~그때 그 발명대회~~")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

from assets.setting.factory import *
sceneFac = SceneFactory()
itemFac = ItemFactory()

while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BLACK)
    pygame.display.update()