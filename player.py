import pygame
from entities import Entity
from proyectiles import Projectile

class Player(Entity):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.health = 100
        self.shield = 100
        self.powers = []
        self.projectiles = pygame.sprite.Group()

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        self.projectiles.update()

    def shoot(self):
        projectile = Projectile(self.rect.centerx, self.rect.top, 10)
        self.projectiles.add(projectile)

    def acquire_power(self, boss):
        self.powers.append(boss.special_ability)
        print(f"Acquired power: {boss.special_ability}")

    def use_power(self):
        if self.powers:
            power = self.powers.pop(0)
            print(f"Using power: {power}")

