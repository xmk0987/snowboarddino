import pygame
from settings import *
import math

class Background:
    def __init__(self):
        self.bg = pygame.image.load('./images/background/lights.jpg').convert()
        self.flip_bg = pygame.transform.flip(self.bg, True, False)

        bg_width = self.bg.get_width()
        self.tiles = math.ceil(screen_width / bg_width) + 1  

        self.rect1 = self.bg.get_rect(topleft=(0, 0))
        self.rect2 = self.flip_bg.get_rect(topleft=(screen_width, 0))

    def draw(self,screen):
        # Draw the images
        screen.blit(self.bg, self.rect1)
        screen.blit(self.flip_bg, self.rect2)

    def update(self, screen, scroll_speed):
        self.rect1.x -= scroll_speed
        self.rect2.x -= scroll_speed
        if self.rect1.right <= 0:
            self.rect1.x = screen_width
        elif self.rect2.right <= 0:
            self.rect2.x = screen_width

        self.draw(screen)


