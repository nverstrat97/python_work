from settings import WIDTH, HEIGHT
import pygame

class UI:
    def __init__(self, game):
        self.game = game
        self.font_small = pygame.font.SysFont("arial", 24)  # Fonts defined here
        self.font_large = pygame.font.SysFont("arial", 40)
        self.window_width = WIDTH
        self.window_height = HEIGHT

    def update_window_size(self, width, height):
        """Update UI dimensions for adaptable positioning."""
        self.window_width = width
        self.window_height = height
        print(f"[DEBUG] UI updated to window size {width}x{height}")

    def draw_text(self, text, pos, size):
        """Helper to draw text on screen."""
        font = self.font_large if size > 30 else self.font_small
        surface = font.render(text, True, (255, 255, 255))
        rect = surface.get_rect(center=pos)
        self.game.screen.blit(surface, rect)

    def draw_start_screen(self):
        self.draw_text("Click to Start", (self.window_width // 2, self.window_height // 2), 40)

    def draw_win_screen(self):
        self.draw_text("You Win!", (self.window_width // 2, self.window_height // 2), 40)

    def draw_lose_screen(self):
        self.draw_text("You Lose", (self.window_width // 2, self.window_height // 2), 40)

    def draw_stats(self):
        """Draw game stats (lives, money, wave) at the top."""
        top_margin = 20
        spacing = max(100, min(self.window_width // 4, 200))
        self.draw_text(f"Lives: {self.game.lives}", (spacing * 1, top_margin), 24)
        self.draw_text(f"Money: {self.game.money}", (spacing * 2, top_margin), 24)
        self.draw_text(f"Wave: {self.game.level.wave_number + 1}", (spacing * 3, top_margin), 24)