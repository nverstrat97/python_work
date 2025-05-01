import pygame
from settings import TOWER_BASE_RANGE, TOWER_BASE_COOLDOWN, TOWER_BASE_DAMAGE, TOWER_MAX_LEVEL, TOWER_UPGRADE_COST_BASE, TOWER_COST, TOWER_DAMAGE_INCREASE, TOWER_COOLDOWN_DECREASE, TOWER_RANGE_INCREASE, TOWER_UPGRADE_COST_INCREASE

class Projectile:
    def __init__(self, x, y, target, damage):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5
        self.damage = damage

    def move(self):
        if not self.target.alive:
            return True
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = (dx**2 + dy**2) ** 0.5
        if dist < self.speed or dist == 0:
            self.target.health -= self.damage
            if self.target.health <= 0:
                self.target.alive = False
            return True
        self.x += self.speed * dx / dist
        self.y += self.speed * dy / dist
        return False

    def draw(self, screen, offset_x=0, offset_y=0):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x + offset_x), int(self.y + offset_y)), 5)

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = TOWER_BASE_RANGE
        self.base_cooldown = TOWER_BASE_COOLDOWN
        self.cooldown = 0
        self.projectiles = []
        self.level = 1
        self.max_level = TOWER_MAX_LEVEL
        self.base_damage = TOWER_BASE_DAMAGE
        self.upgrade_cost = TOWER_UPGRADE_COST_BASE
        self.cost = TOWER_COST

    def get_stats(self):
        damage = self.base_damage + (self.level - 1) * TOWER_DAMAGE_INCREASE
        cooldown = max(10, self.base_cooldown - (self.level - 1) * TOWER_COOLDOWN_DECREASE)
        range_val = self.range + (self.level - 1) * TOWER_RANGE_INCREASE
        return damage, cooldown, range_val

    def update(self, enemy_list):
        damage, cooldown, range_val = self.get_stats()
        if self.cooldown > 0:
            self.cooldown -= 1

        for enemy in enemy_list:
            if not enemy.alive:
                continue
            dx = enemy.x - self.x
            dy = enemy.y - self.y
            dist = (dx**2 + dy**2) ** 0.5
            if dist <= range_val and self.cooldown == 0:
                self.shoot(enemy, damage)
                self.cooldown = cooldown
                break

        for projectile in self.projectiles[:]:
            if projectile.move():
                self.projectiles.remove(projectile)

    def shoot(self, enemy, damage):
        self.projectiles.append(Projectile(self.x, self.y, enemy, damage))

    def upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            self.upgrade_cost += TOWER_UPGRADE_COST_INCREASE
            return True
        return False

    def draw(self, screen, offset_x=0, offset_y=0):
        damage, cooldown, range_val = self.get_stats()
        draw_x = int(self.x + offset_x)
        draw_y = int(self.y + offset_y)
        pygame.draw.circle(screen, (0, 255, 255), (draw_x, draw_y), 20)
        pygame.draw.circle(screen, (0, 255, 255), (draw_x, draw_y), range_val, 1)
        font = pygame.font.SysFont("arial", 16)
        text = font.render(str(self.level), True, (255, 255, 255))
        screen.blit(text, (draw_x - 5, draw_y - 10))
        for projectile in self.projectiles:
            projectile.draw(screen, offset_x, offset_y)

    def update_position(self, new_x, new_y):
        """Update the tower's position if needed (not used with fixed board, kept for compatibility)."""
        self.x = new_x
        self.y = new_y
        print(f"[DEBUG] Tower position updated to ({self.x}, {self.y})")