from settings import WIDTH, HEIGHT, GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT
from path import original_path, draw_path
from enemy import Enemy

class Level:
    def __init__(self, game):
        self.game = game
        self.path = original_path  # Use fixed path for game board (no scaling)
        self.enemies = []
        self.wave_number = 0
        self.spawn_delay = 60
        self.spawn_timer = 0
        self.enemies_per_wave = 5
        self.enemies_spawned = 0
        self.enemies_reached_end = 0  # Track enemies that reached end for lives deduction
        self.max_waves = 3
        self.current_level = 0
        self.max_levels = 1

    def update_window_size(self, width, height):
        """Update dimensions but do not rescale path (fixed game board)."""
        print(f"[DEBUG] Level received window size update {width}x{height}, but path remains fixed")

    def reset(self):
        """Reset level state for new game."""
        self.enemies.clear()
        self.wave_number = 0
        self.enemies_spawned = 0

    def draw(self):
        """Draw level elements like the path with viewport offset."""
        draw_path(self.game.screen, [(x + self.game.viewport_x, y + self.game.viewport_y) for x, y in self.path])

    def update(self):
        """Update level logic like enemy spawning and movement."""
        # Spawn enemies over time using fixed path
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
                    self.enemies_reached_end += 1
                    print(f"[DEBUG] Enemy reached end. Lives to deduct: {self.enemies_reached_end}")

            if enemy.alive:
                enemy.draw(self.game.screen, offset_x=self.game.viewport_x, offset_y=self.game.viewport_y)

    def is_wave_complete(self):
        """Check if current wave is done."""
        living_enemies = [e for e in self.enemies if e.alive]
        return self.enemies_spawned >= self.enemies_per_wave and not living_enemies

    def is_level_complete(self):
        """Check if all waves in level are done."""
        if self.is_wave_complete():
            if self.wave_number >= self.max_waves - 1:
                return True
            else:
                self.wave_number += 1
                self.enemies_spawned = 0
                print(f"[DEBUG] Moving to Wave {self.wave_number + 1}")
        return False

    def advance_to_next_level(self):
        """Move to next level if available."""
        self.current_level += 1
        self.wave_number = 0
        self.enemies_spawned = 0
        # Optionally update path or wave data for new level in future