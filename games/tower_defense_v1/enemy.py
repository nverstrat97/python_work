# enemy.py
import pygame

class Enemy:
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[self.path_index]
        self.speed = 1.2
        self.max_health = 100
        self.health = self.max_health
        self.alive = True

    def move(self):
        if self.path_index + 1 < len(self.path):
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
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 15)
        health_bar_width = 30
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 15, self.y - 25, health_bar_width, 5))
        pygame.draw.rect(screen, (0, 255, 0), (self.x - 15, self.y - 25, health_bar_width * health_ratio, 5))
