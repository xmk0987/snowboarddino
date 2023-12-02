import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y): 
        super().__init__()
        self.import_character_assets()
        self.import_particle_assets()
        self.frame_index = 0
        self.animations_speed = 0.15
        
        self.direction = pygame.Vector2(x,y)
        self.image = self.animations['idle'][self.frame_index]
        self.jump_image = self.animations['jump'][self.frame_index]
        self.crouch_image = self.animations['crouch'][self.frame_index]

        self.player_rect = self.image.get_rect(topleft = (x,y))
        self.crouch_rect = self.crouch_image.get_rect(topleft = (x,y + 18))

        self.jumping = False
        self.crouching = False

        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 16
        self.Y_VELOCITY = self.JUMP_HEIGHT

        self.count = 0


    # ANIMATIONS
    def animate(self, screen):
        if self.jumping:
            screen.blit(self.jump_image, self.player_rect)
        elif self.crouching:
            screen.blit(self.crouch_image, self.crouch_rect)
        else:
            screen.blit(self.image, self.player_rect)

    # Import character animaton surfaces
    def import_character_assets(self):
        character_path = './images/character/'
        self.animations = {'crouch' : [], 'idle' : [], 'fall':[],'jump':[],'run':[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def import_particle_assets(self):
        particle_path = './images/particles'
        self.particles = import_folder(particle_path)

    def animate_snow_particle(self, screen):
        animation = self.particles
        self.frame_index += self.animations_speed
        if self.frame_index >= len(animation): 
            self.frame_index = 0
        
        particle = animation[int(self.frame_index)]
        self.particle_rect = particle.get_rect(bottomleft = (self.player_rect.x - 10, screen_height - 25))
        if not self.jumping:
            screen.blit(particle, self.particle_rect)
 
    # MOVEMENT
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.jumping = True
        elif keys[pygame.K_s]:
            self.crouching = True
        else:
            self.crouching = False

    def jump(self):
        if self.crouching:
            self.player_rect.y = 400
            self.jumping = False
            self.Y_VELOCITY = self.JUMP_HEIGHT
        else:
            if self.jumping:
                self.player_rect.y -= self.Y_VELOCITY
                self.Y_VELOCITY -= self.Y_GRAVITY

                if self.Y_VELOCITY < -self.JUMP_HEIGHT:
                    self.jumping = False
                    self.Y_VELOCITY = self.JUMP_HEIGHT

                self.player_rect = self.image.get_rect(topleft=(self.player_rect.x, self.player_rect.y))

    # COLLISIONS
    def check_vertical_collision(self, ground_rect):
        if self.player_rect.colliderect(ground_rect):
            if self.direction.y > 0:
                self.player_rect.bottom = ground_rect.top
                self.direction.y = 0
                self.jumping = False


    def check_enemy_collision(self, enemy):
        if self.crouching:
            if self.crouch_rect.colliderect(enemy.enemy_rect):
                return True
        else:
            if self.player_rect.colliderect(enemy.enemy_rect):
                return True




    def update(self, screen, ground_rect, enemy):
        self.check_vertical_collision(ground_rect)
        self.check_enemy_collision(enemy)
        self.get_input()
        self.jump()
        self.animate(screen)
        self.animate_snow_particle(screen)



