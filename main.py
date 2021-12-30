import pygame,sys
from factory import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("ITEM GAME")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    while True:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(BLACK)
        pygame.display.update()