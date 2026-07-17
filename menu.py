import pygame
from pygame import SurfaceType



class Menu:
    def __init__(self, screen: SurfaceType):
        self.screen = screen
        self.background = pygame.image.load("assets/Background.png")
        self.background = pygame.transform.scale(self.background, self.screen.get_size())

    def display(self):
        self.screen.blit(self.background, (0,0) )
        pygame.display.flip()
