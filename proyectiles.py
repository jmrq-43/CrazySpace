import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('recursos/images/proyectil_user.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self, *args):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('recursos/images/enemy_projectile.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
