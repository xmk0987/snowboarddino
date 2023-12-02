from enemy import Enemy
import random
from player import Player
from settings import *

class Spawn:
    def __init__(self):
        self.enemyCount = 1
        self.level = 1
        self.player = Player(200, screen_height - 90)  
        
        self.enemy_speed = 6
        self.enemy_x = 1500

    def check_if_passed(self, enemy):
        if enemy.enemy_rect.x < 0:
            return True

    def spawn_enemy(self, level):
        # Spawning enemies
        self.enemy_speed = level + 5

        if level >= 4:
            random_number = random.randint(1, 4)
            random_number2 = random.randint(1, 4)
            if level < 12:
                random_distance = random.randint(35, 60)
            if level >= 12:
                random_distance = random.randint(45, 60)


            if self.enemyCount == 2:
                self.enemy = Enemy(random_number, self.enemy_speed, self.enemy_x)
                self.enemy2 = Enemy(random_number2, self.enemy_speed, self.enemy_x + (10*random_distance))
                self.enemyCount += 2
            if self.check_if_passed(self.enemy) and self.check_if_passed(self.enemy2):
                self.enemyCount = 2
            
        else:
            if self.enemyCount == 1:
                random_number = random.randint(1, 4)
                self.enemy = Enemy(random_number, self.enemy_speed, self.enemy_x)
                self.enemyCount += 1

            if self.check_if_passed(self.enemy):
                self.enemyCount = 1
            
            if level >= 2:
                self.enemy_x = 1000


    def update(self, screen, level, ground_rect):
        self.spawn_enemy(level)
        self.player.update(screen, ground_rect, self.enemy)
        if self.player.check_enemy_collision(self.enemy):
            return True
        self.enemy.update(screen)
        if hasattr(self, 'enemy2'):
            self.enemy2.update(screen)
            if self.player.check_enemy_collision(self.enemy2):
                return True







