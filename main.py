import sys

import pygame

from settings import Settings

if __name__ == "__main__":
    pygame.init()
    running = True
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("2D Alien Invasion Game")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("white")
        pygame.display.update()
