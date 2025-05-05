import pygame
from src.settings import WIDTH, HEIGHT, BG_COLOR, GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT
from src.ui.ui import UI
from src.core.level import Level
from src.entities.towers import Tower

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = "start"  # Options: start, playing, win, lose
        self.lives = 10
        self.money = 100
        self.window_width = WIDTH
        self.window_height = HEIGHT
        self.towers = []
        # Initialize sub-modules
        self.ui = UI(self)
        self.level = Level(self)
        # Calculate viewport offset to center game board if window is larger
        self.viewport_x = max(0, (self.window_width - GAME_BOARD_WIDTH) // 2)
        self.viewport_y = max(0, (self.window_height - GAME_BOARD_HEIGHT) // 2)

    def update_window_size(self, width, height):
        """Update window dimensions and adjust viewport, not game elements."""
        self.window_width = width
        self.window_height = height
        self.ui.update_window_size(width, height)
        # Center the game board in the window if window is larger than game board
        self.viewport_x = max(0, (self.window_width - GAME_BOARD_WIDTH) // 2)
        self.viewport_y = max(0, (self.window_height - GAME_BOARD_HEIGHT) // 2)
        print(f"[DEBUG] Game updated to window size {width}x{height}, viewport offset ({self.viewport_x}, {self.viewport_y})")

    def update(self):
        self.screen.fill(BG_COLOR)

        if self.state == "start":
            self.ui.draw_start_screen()
        elif self.state == "playing":
            self.play_game()
        elif self.state == "win":
            self.ui.draw_win_screen()
        elif self.state == "lose":
            self.ui.draw_lose_screen()

        pygame.display.flip()

    def play_game(self):
        # Draw level elements (path, enemies) with viewport offset
        self.level.draw()
        self.level.update()
        
        # Update and draw towers with viewport offset
        living_enemies = [e for e in self.level.enemies if e.alive]
        for tower in self.towers:
            tower.update(living_enemies)
            tower.draw(self.screen, offset_x=self.viewport_x, offset_y=self.viewport_y)

        # Handle lives and money updates from level
        if self.level.enemies_reached_end:
            self.lives -= self.level.enemies_reached_end
            self.level.enemies_reached_end = 0
        
        for enemy in self.level.enemies[:]:
            if not enemy.alive and enemy.health <= 0:
                self.money += enemy.reward
                self.level.enemies.remove(enemy)

        # Check win/lose conditions
        if self.lives <= 0:
            self.state = "lose"
        elif self.level.is_level_complete():
            if self.level.current_level >= self.level.max_levels - 1:
                self.state = "win"
            else:
                self.level.advance_to_next_level()
                print(f"[DEBUG] Advancing to level {self.level.current_level + 1}")

        # Draw UI stats (adapts to window size via UI class)
        self.ui.draw_stats()
        # Draw game border
        self.draw_border()

    def draw_border(self):
        """Draw a border around the fixed game board area."""
        from settings import BORDER_COLOR, BORDER_THICKNESS, GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT
        border_rect = pygame.Rect(self.viewport_x, self.viewport_y, GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)
        pygame.draw.rect(self.screen, BORDER_COLOR, border_rect, BORDER_THICKNESS)

    def start_game(self):
        self.state = "playing"
        self.level.enemies = []
        self.towers = []
        self.level.reset()
        self.lives = 10
        self.money = 100

    def handle_click(self, pos):
        if self.state == "start":
            self.start_game()
        elif self.state == "playing":
            # Adjust click position to account for viewport offset (convert window coords to game board coords)
            adjusted_pos = (pos[0] - self.viewport_x, pos[1] - self.viewport_y)
            # Only allow clicks within game board boundaries
            if (0 <= adjusted_pos[0] <= GAME_BOARD_WIDTH and 
                0 <= adjusted_pos[1] <= GAME_BOARD_HEIGHT):
                upgrade_attempted = False
                for tower in self.towers:
                    dx = tower.x - adjusted_pos[0]
                    dy = tower.y - adjusted_pos[1]
                    dist = (dx**2 + dy**2) ** 0.5
                    if dist < 25:
                        upgrade_attempted = True
                        if self.money >= tower.upgrade_cost:
                            if tower.upgrade():
                                self.money -= tower.upgrade_cost
                                print(f"[DEBUG] Tower upgraded to level {tower.level}")
                        else:
                            print(f"[DEBUG] Not enough money to upgrade tower. Need {tower.upgrade_cost}, have {self.money}")
                        break
                if not upgrade_attempted and self.money >= 100:
                    self.towers.append(Tower(*adjusted_pos))
                    self.money -= 100
                    print(f"[DEBUG] Tower placed at {adjusted_pos}. Money left: {self.money}")
                elif not upgrade_attempted and self.money < 100:
                    print(f"[DEBUG] Not enough money to place tower. Need 100, have {self.money}")
            else:
                print(f"[DEBUG] Click outside game board boundaries at {adjusted_pos}")
        elif self.state in ["win", "lose"]:
            self.state = "start"