# tower.py
import pygame

class Projectile:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5

    def move(self):
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = (dx**2 + dy**2) ** 0.5
        if dist < self.speed or dist == 0:
            self.target.health -= 20
            if self.target.health <= 0:
                self.target.alive = False
            return True
        self.x += self.speed * dx / dist
        self.y += self.speed * dy / dist
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 5)

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.cooldown = 0
        self.projectiles = []

    def update(self, enemy_list):
        if self.cooldown > 0:
            self.cooldown -= 1

        for enemy in enemy_list:
            if not enemy.alive:
                continue
            dx = enemy.x - self.x
            dy = enemy.y - self.y
            dist = (dx**2 + dy**2) ** 0.5
            if dist <= self.range and self.cooldown == 0:
                self.shoot(enemy)
                self.cooldown = 30
                break

        for projectile in self.projectiles[:]:
            if projectile.move():
                self.projectiles.remove(projectile)

    def shoot(self, enemy):
        self.projectiles.append(Projectile(self.x, self.y, enemy))

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), 20)
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), self.range, 1)
        for projectile in self.projectiles:
            projectile.draw(screen)
