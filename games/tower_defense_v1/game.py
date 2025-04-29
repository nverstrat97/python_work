# game.py
import pygame
from enemy import Enemy
from towers import Tower
from path import draw_path, path
from settings import WIDTH, HEIGHT, BG_COLOR, FPS

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.enemies = []
        self.towers = []
        self.path = path
        self.state = "start"  # start, playing, win, lose
        self.wave_number = 0
        self.spawn_delay = 60
        self.spawn_timer = 0
        self.max_waves = 3
        self.enemies_per_wave = 5
        self.enemies_spawned = 0
        self.lives = 10

    def start_game(self):
        self.state = "playing"
        self.enemies.clear()
        self.towers.clear()
        self.wave_number = 1
        self.enemies_spawned = 0
        self.lives = 10

    def update(self):
        self.clock.tick(FPS)
        self.screen.fill(BG_COLOR)

        if self.state == "start":
            self.draw_text("Click to Start", (WIDTH//2, HEIGHT//2), 40)
        elif self.state == "playing":
            self.play_game()
        elif self.state == "win":
            self.draw_text("You Win!", (WIDTH//2, HEIGHT//2), 40)
        elif self.state == "lose":
            self.draw_text("Game Over", (WIDTH//2, HEIGHT//2), 40)

        pygame.display.flip()

    def play_game(self):
        draw_path(self.screen, self.path)

        # Spawn enemies over time
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay and self.enemies_spawned < self.enemies_per_wave:
            self.enemies.append(Enemy(self.path))
            self.spawn_timer = 0
            self.enemies_spawned += 1

        # Move/draw enemies
        for enemy in self.enemies:
            if enemy.alive:
                enemy.move()
                enemy.draw(self.screen)
            elif enemy.path_index >= len(enemy.path) - 1:
                self.lives -= 1

        # Clean up dead enemies
        living_enemies = [e for e in self.enemies if e.alive]
        self.enemies = [e for e in self.enemies if e.alive or e.path_index < len(e.path) - 1]

        for tower in self.towers:
            tower.update(living_enemies)
            tower.draw(self.screen)

        # Check win/lose
        if self.lives <= 0:
            self.state = "lose"
        elif self.enemies_spawned >= self.enemies_per_wave and not living_enemies:
            if self.wave_number >= self.max_waves:
                self.state = "win"
            else:
                self.wave_number += 1
                self.enemies_spawned = 0

        self.draw_text(f"Lives: {self.lives}", (80, 20), 24)
        self.draw_text(f"Wave: {self.wave_number}", (WIDTH - 100, 20), 24)

    def handle_click(self, pos):
        if self.state == "start":
            self.start_game()
        elif self.state == "playing":
            self.towers.append(Tower(*pos))
        elif self.state in ["win", "lose"]:
            self.state = "start"

    def draw_text(self, text, pos, size):
        font = pygame.font.SysFont("arial", size)
        surface = font.render(text, True, (255, 255, 255))
        rect = surface.get_rect(center=pos)
        self.screen.blit(surface, rect)
