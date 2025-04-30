import pygame
from enemy import Enemy
from towers import Tower
from path import draw_path, path
from settings import WIDTH, HEIGHT, BG_COLOR, FPS

class Game:
    def __init__(self, screen):
        self.screen = screen
        # Removed self.clock since frame rate is handled in main.py
        self.enemies = []
        self.towers = []
        self.path = path
        self.state = "start"  # Options: start, playing, win, lose
        self.wave_number = 0
        self.spawn_delay = 60
        self.spawn_timer = 0
        self.max_waves = 3
        self.enemies_per_wave = 5
        self.enemies_spawned = 0
        self.lives = 10
        # Cached fonts for performance
        self.font_small = pygame.font.SysFont("arial", 24)
        self.font_large = pygame.font.SysFont("arial", 40)

    def start_game(self):
        self.state = "playing"
        self.enemies.clear()
        self.towers.clear()
        self.wave_number = 1
        self.enemies_spawned = 0
        self.lives = 10

    def update(self):
        self.screen.fill(BG_COLOR)

        if self.state == "start":
            self.draw_text("Click to Start", (WIDTH // 2, HEIGHT // 2), 40)
        elif self.state == "playing":
            self.play_game()
        elif self.state == "win":
            self.draw_text("You Win!", (WIDTH // 2, HEIGHT // 2), 40)
        elif self.state == "lose":
            self.draw_text("You Lose", (WIDTH // 2, HEIGHT // 2), 40)

        pygame.display.flip()

    def play_game(self):
        draw_path(self.screen, self.path)

        # Spawn enemies over time
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay and self.enemies_spawned < self.enemies_per_wave:
            self.enemies.append(Enemy(self.path))
            self.spawn_timer = 0
            self.enemies_spawned += 1

        # Move enemies and check if they reach the end
        for enemy in self.enemies:
            if enemy.alive:
                enemy.move()
                if enemy.reached_end():
                    enemy.alive = False
                    self.lives -= 1
            if enemy.alive:
                enemy.draw(self.screen)

        # Clean up fully processed enemies (simplified)
        self.enemies = [e for e in self.enemies if e.alive]

        # Update and draw towers
        living_enemies = [e for e in self.enemies if e.alive]
        for tower in self.towers:
            tower.update(living_enemies)
            tower.draw(self.screen)

        # Check for loss condition
        if self.lives <= 0:
            self.state = "lose"

        # Check for win or next wave
        elif self.enemies_spawned >= self.enemies_per_wave and not living_enemies:
            if self.wave_number >= self.max_waves:
                self.state = "win"
            else:
                self.wave_number += 1
                self.enemies_spawned = 0

        # Display lives and wave
        self.draw_text(f"Lives: {self.lives}", (80, 20), 24)
        self.draw_text(f"Wave: {self.wave_number}", (WIDTH - 100, 20), 24)

    def handle_click(self, pos):
        if self.state == "start":
            self.start_game()
        elif self.state == "playing":
            # Add tower at clicked position (consider adding validation later)
            self.towers.append(Tower(*pos))
        elif self.state in ["win", "lose"]:
            self.state = "start"

    def draw_text(self, text, pos, size):
        # Use cached font based on size
        font = self.font_large if size > 30 else self.font_small
        surface = font.render(text, True, (255, 255, 255))
        rect = surface.get_rect(center=pos)
        self.screen.blit(surface, rect)