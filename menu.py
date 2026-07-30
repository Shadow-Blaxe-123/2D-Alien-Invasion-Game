import pygame
from pygame import SurfaceType



class Menu:
    def __init__(self, screen: SurfaceType):
        self.screen = screen
        self.screen_center = (screen.get_width()//2, screen.get_height()//2)
        self.text = "Play"


    def display(self):
        # TODO: Add Border to PLay button
        # TODO: Detect mouse click
        # TODO: Clear the screen

        font = pygame.font.SysFont("sans-serif",100)
        text_render = font.render(self.text,True, "green", "blue")

        text_rect = text_render.get_rect()

        # set the center of the rectangular object.
        text_rect.center = self.screen_center

        self.screen.blit(text_render, text_rect)
        pygame.display.flip()

    def remove(self, bg: SurfaceType):
        self.screen.blit(bg, (0,0))
        pygame.display.flip()
        print("h")

