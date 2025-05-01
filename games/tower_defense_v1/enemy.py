import pygame

class Enemy:
    def __init__(self, path, enemy_type="basic", health=100, speed=1.2):
        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[self.path_index]
        self.speed = speed
        self.alive = True
        self.health = health
        self.max_health = health
        self.enemy_type = enemy_type
        # Reward when defeated by tower, can vary by type
        self.reward = 10 if enemy_type == "basic" else 20 if enemy_type == "fast" else 15

    def move(self):
        if self.alive and self.path_index + 1 < len(self.path):
            target_x, target_y = self.path[self.path_index + 1]
            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < self.speed:
                self.x, self.y = target_x, target_y
                self.path_index += 1
            else:
                self.x += self.speed * dx / distance
                self.y += self.speed * dy / distance

    def draw(self, screen):
        # Color based on enemy type
        color = (255, 0, 0) if self.enemy_type == "basic" else (255, 165, 0) if self.enemy_type == "fast" else (255, 0, 255)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 15)
        health_bar_width = 30
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 15, self.y - 25, health_bar_width, 5))
        pygame.draw.rect(screen, (0, 255, 0), (self.x - 15, self.y - 25, health_bar_width * health_ratio, 5))

    def reached_end(self):
        return self.path_index >= len(self.path) - 1

    def update_path(self, new_path):
        """Update the enemy's path to follow a new scaled path after window resize."""
        if self.path_index < len(new_path):
            self.path = new_path
            # Adjust current position to match the new scaled path's corresponding point if possible
            if self.path_index < len(self.path):
                self.x, self.y = self.path[self.path_index]
            print(f"[DEBUG] Enemy path updated, position reset to {self.x}, {self.y} at index {self.path_index}")
        else:
            print(f"[DEBUG] Enemy path not updated, beyond path length at index {self.path_index}")