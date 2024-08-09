import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        super().__init__()
        self.direction = direction
        self.image = pygame.image.load('recursos/images/proyectil_user.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed

        # Elimina el proyectil si sale de la pantalla
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
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
