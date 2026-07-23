import pygame
from pygame import SurfaceType



class Menu:
    def __init__(self, screen: SurfaceType):
        self.screen = screen
        self.screen_center = (screen.get_width()//2, screen.get_height()//2)


    def display(self):
        # TODO: ADD Content
        pygame.display.flip()
        pygame.draw.rect(self.screen, (255,255,255), (640,360,25,25),5)

        pygame.display.flip()
