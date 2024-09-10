import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, keys):
        pass

from CrazySpace.main.settings import PLAYER_SPEED
from entities import Entity

class Player(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.speed = PLAYER_SPEED

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

import pygame

class Boss(Entity):
    def __init__(self, image, x, y, health, attack_power, special_ability):
        super().__init__(image, x, y)
        self.health = health
        self.attack_power = attack_power
        self.special_ability = special_ability

    def attack(self, player):
        player.health -= self.attack_power
