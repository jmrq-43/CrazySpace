import random

import pygame

from CrazySpace.npc.enemies import Boss, Enemy, NPC
from CrazySpace.player.player import Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.paused = False
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.player = Player(pygame.image.load('../npc/recursos/images/player.png'), 100, 100)
        self.all_sprites.add(self.player)
        self.projectiles = pygame.sprite.Group()
        self.enemy_projectiles = pygame.sprite.Group()
        self.boss = Boss(pygame.image.load('../npc/recursos/images/boss.png'), 400, 300, 100, 10, "Freeze Ability")
        self.enemy_count = 0
        self.spawn_npcs()

    def spawn_npcs(self):
        for _ in range(random.randint(10, 20)):
            npc = NPC(pygame.image.load('../npc/recursos/images/npc.png'), random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            self.npcs.add(npc)
            self.all_sprites.add(npc)
        self.enemy_count = len(self.npcs)

    def check_npc_kills(self):
        if len(self.npcs) == 0 and self.enemy_count == 0:
            self.spawn_enemies()

    def spawn_enemies(self):
        for _ in range(3):
            enemy = Enemy(pygame.image.load('../npc/recursos/images/enemy.png'), random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), 3, 1000)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
        self.enemy_count = len(self.enemies)

    def check_enemy_kills(self):
        if len(self.enemies) == 0 and self.enemy_count > 0:
            self.spawn_boss()

    def spawn_boss(self):
        self.all_sprites.add(self.boss)

    def run(self):
        while self.running:
            if self.playing:
                if not self.paused:
                    self.game_loop()
                else:
                    self.pause_menu()
            else:
                self.main_menu()

    def game_loop(self):
        while self.playing and not self.paused:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.toggle_pause()
                if event.key == pygame.K_e:
                    self.interact_with_npc()
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                self.handle_menu_click(mouse_pos)

    def update(self):
        keys = pygame.key.get_pressed()
        self.all_sprites.update(keys)
        self.projectiles.update()
        self.enemy_projectiles.update()
        self.player.projectiles.update()

        # Verificar si los NPCs han sido eliminados
        self.check_npc_kills()

        # Verificar si los enemigos han sido eliminados
        self.check_enemy_kills()
        #colision con npc
        #
        # for projectile in self.player.projectiles:
        #     hits = pygame.sprite.spritecollide(projectile, self.npcs, True)  # True para eliminar el NPC
        # for npc in hits:
        #     projectile.kill()
        #     self.enemy_count -= 1
        #

        # Colisiones de proyectiles con enemigos
        for projectile in self.player.projectiles:
            hits = pygame.sprite.spritecollide(projectile, self.all_sprites, False)
            for hit in hits:
                if isinstance(hit, Enemy) or isinstance(hit, Boss) or isinstance(hit,NPC):
                    hit.health -= 10
                    projectile.kill()
                    self.enemy_count -= 1
                if hit.health <= 0:
                        self.all_sprites.remove(hit)

        # Colisiones de proyectiles con el jugador
        for projectile in self.enemy_projectiles:
            if pygame.sprite.collide_rect(projectile, self.player):
                self.player.health -= 10
                projectile.kill()


        # Colisiones
        collisions = pygame.sprite.spritecollide(self.player, self.all_sprites, False)
        for sprite in collisions:
            if isinstance(sprite, Boss):
                self.player.acquire_power(sprite)
                self.boss.attack(self.player)
                self.boss.use_special_ability()
                self.all_sprites.remove(sprite)


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.projectiles.draw(self.screen)
        self.enemy_projectiles.draw(self.screen)
        self.player.projectiles.draw(self.screen)
        pygame.display.flip()

    def main_menu(self):
        title = self.font.render("Space Game", True, (255, 255, 255))
        start_button = self.small_font.render("Start", True, (255, 255, 255))
        quit_button = self.small_font.render("Quit", True, (255, 255, 255))
        start_button_rect = start_button.get_rect(center=(SCREEN_WIDTH // 2, 300))
        quit_button_rect = quit_button.get_rect(center=(SCREEN_WIDTH // 2, 400))

        while not self.playing:
            self.screen.fill((0, 0, 0))
            self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
            self.screen.blit(start_button, start_button_rect)
            self.screen.blit(quit_button, quit_button_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if start_button_rect.collidepoint(mouse_pos):
                        self.playing = True
                    if quit_button_rect.collidepoint(mouse_pos):
                        self.running = False
                        self.playing = False

    def toggle_pause(self):
        self.paused = not self.paused

    def pause_menu(self):
        resume_text = self.small_font.render("Resume", True, (255, 255, 255))
        main_menu_text = self.small_font.render("Main Menu", True, (255, 255, 255))
        resume_button_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        main_menu_button_rect = main_menu_text.get_rect(center=(SCREEN_WIDTH // 2, 400))

        while self.paused:
            self.screen.fill((0, 0, 0))
            self.screen.blit(resume_text, resume_button_rect)
            self.screen.blit(main_menu_text, main_menu_button_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.paused = False
                    self.playing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if resume_button_rect.collidepoint(mouse_pos):
                        self.toggle_pause()
                    if main_menu_button_rect.collidepoint(mouse_pos):
                        self.paused = False
                        self.playing = False

    def handle_menu_click(self, mouse_pos):
        pass

    def interact_with_npc(self):
        collisions = pygame.sprite.spritecollide(self.player, self.all_sprites, False)
        for sprite in collisions:
            if isinstance(sprite, NPC):
                sprite.interact()


if __name__ == "__main__":
    game = Game()
    game.run()
