import pygame
from entities import Entity
from proyectiles import Projectile, EnemyProjectile
import random

from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(Entity):
    def __init__(self, image, x, y, speed, attack_power):
        super().__init__(image, x, y)
        self.speed = speed
        self.attack_power = attack_power
        self.projectiles = pygame.sprite.Group()
        self.shoot_timer = random.randint(20, 60)

    def update(self, *args):
        self.rect.x += random.randint(-1, 1) * self.speed
        self.rect.y += random.randint(-1, 1) * self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        self.shoot_timer -= 1
        if self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = random.randint(20, 60)
        self.projectiles.update()

    def shoot(self):
        projectile = EnemyProjectile(self.rect.centerx, self.rect.bottom, 5)
        self.projectiles.add(projectile)

class Boss(Entity):
    def __init__(self, image, x, y, health, attack_power, special_ability):
        super().__init__(image, x, y)
        self.health = health
        self.attack_power = attack_power
        self.special_ability = special_ability
        self.cooldown = 0
        self.projectiles = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += 1
        self.rect.y += random.randint(-1, 1) * 2
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.cooldown > 0:
            self.cooldown -= 1
        self.projectiles.update()

    def attack(self, target):
        if self.cooldown == 0:
            target.health -= self.attack_power
            self.cooldown = 60

    def use_special_ability(self):
        if self.special_ability == "Freeze Ability":
            pass
        elif self.special_ability == "Poison Ability":
            pass
        elif self.special_ability == "Instakill Ray":
            pass

class NPC(Entity):
    def __init__(self, image, x, y, dialogue):
        super().__init__(image, x, y)
        self.dialogue = dialogue

    def update(self, *args):
        pass

    def interact(self):
        print(self.dialogue)

