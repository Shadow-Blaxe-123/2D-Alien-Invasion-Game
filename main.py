import sys

import pygame

from settings import Settings
from menu import Menu

if __name__ == "__main__":
    pygame.init()
    running = True
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    menu = Menu(screen)
    pygame.display.set_caption("2D Alien Invasion Game")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        menu.display()
