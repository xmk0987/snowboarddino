import pygame
from settings import *
from support import import_folder

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, moveSpeed, x):
        super().__init__()
        self.width = 30
        self.move_speed = moveSpeed
        self.x = x
        self.type = type

        image_path = './images/enemies/'
        self.air_enemy_image = pygame.image.load(image_path + 'air_enemy.png')
        self.big_ground_enemy_image = pygame.image.load(image_path + 'big_ground_enemy.png')
        self.small_ground_enemy_image = pygame.image.load(image_path + 'small_ground_enemy.png')

        if self.type == 1:
            #self.enemy_rect = pygame.Rect(self.x, ground_level - small_ground_enemy_height, self.width, small_ground_enemy_height)
            self.enemy_rect = self.small_ground_enemy_image.get_rect(topleft = (self.x, ground_level - small_ground_enemy_height))
        elif self.type == 2:
            #self.enemy_rect = pygame.Rect(self.x, ground_level-big_ground_enemy_height, self.width, big_ground_enemy_height)
            self.enemy_rect = self.big_ground_enemy_image.get_rect(topleft = (self.x, ground_level-big_ground_enemy_height))

        elif self.type == 3:
            #self.enemy_rect = pygame.Rect(self.x, body_level, self.width, air_enemy_height)
            self.enemy_rect = self.air_enemy_image.get_rect(topleft = (self.x, body_level))

        elif self.type == 4:
            #self.enemy_rect = pygame.Rect(self.x, crouch_level, self.width, air_enemy_height)
            self.enemy_rect = self.air_enemy_image.get_rect(topleft = (self.x, crouch_level))

    def spawn_enemy(self, screen):
        if self.type == 1:
            screen.blit(self.small_ground_enemy_image, self.enemy_rect)
        elif self.type == 2:
            screen.blit(self.big_ground_enemy_image, self.enemy_rect)
        else: 
            screen.blit(self.air_enemy_image, self.enemy_rect)

    def move_enemy(self):
        self.enemy_rect.x -= self.move_speed

    def update(self, screen):
        self.spawn_enemy(screen)
        self.move_enemy()


