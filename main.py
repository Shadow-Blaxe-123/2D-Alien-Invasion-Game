import sys

import pygame

from settings import Settings
from menu import Menu

if __name__ == "__main__":
    pygame.init()
    running = True
    show_menu = True
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    background = pygame.image.load("assets/Background.png")
    background = pygame.transform.scale(background, settings.screen_size)
    screen.blit(background, (0,0) )
    pygame.display.flip()
    menu = Menu(screen)
    pygame.display.set_caption("2D Alien Invasion Game")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # TODO: fix the mouse event to check collide point so that only once clicking on the button itself does it clear.
                if event.button ==1:
                    menu.remove(background)
                    show_menu = False

        if show_menu:
            menu.display()
