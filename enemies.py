import pygame
from entities import Entity
from proyectiles import Projectile, EnemyProjectile
import random

from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(Entity):
    def __init__(self, image, x, y, speed, fire_rate):
        super().__init__(image, x, y)
        self.health = 100
        self.projectiles = pygame.sprite.Group()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.fire_rate = fire_rate  # Tasa de disparo en cuadros por segundo
        self.last_shot = pygame.time.get_ticks()
        self.direction = random.choice(['left', 'right'])

    def update(self, key):
        # Movimiento aleatorio
        if self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        # Cambio de dirección si sale de la pantalla
        if self.rect.left < 0:
            self.direction = 'right'
        elif self.rect.right > SCREEN_WIDTH:
            self.direction = 'left'

        # Disparo
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.fire_rate:
            self.shoot()
            self.last_shot = current_time

    def attack(self, target):
        if self.cooldown == 0:
            target.health -= self.attack_power
            self.cooldown = 60

    def shoot(self):
        if self.direction == 'right':
            projectile = EnemyProjectile(self.rect.right, self.rect.centery, 7)
        elif self.direction == 'left':
            projectile = EnemyProjectile(self.rect.left, self.rect.centery, 7)
        self.projectiles.add(projectile)


class Boss(Entity):
    def __init__(self, image, x, y, health, attack_power, special_ability):
        super().__init__(image, x, y)
        self.health = health
        self.attack_power = attack_power
        self.special_ability = special_ability
        self.cooldown = 0
        self.projectiles = pygame.sprite.Group()

    def shoot(self):
        projectile = EnemyProjectile(self.rect.centerx, self.rect.bottom, 10)
        self.projectiles.add(projectile)

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
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.attack_power = 5
        self.projectiles = pygame.sprite.Group()
        self.health = 10
        self.cooldown = 0

    def attack(self, target):
        if self.cooldown == 0:
            target.health -= self.attack_power
            self.cooldown = 60

    def update(self, *args):
        self.rect.x += 1
        self.rect.y += random.randint(-1, 1) * 2
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.cooldown > 0:
            self.cooldown -= 1
        self.projectiles.update()

