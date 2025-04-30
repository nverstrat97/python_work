import pygame

class Projectile:
    def __init__(self, x, y, target, damage):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5
        self.damage = damage  # Now configurable based on tower level

    def move(self):
        if not self.target.alive:  # Prevent errors if target is already dead
            return True  # Remove projectile if target is gone
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

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 5)

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.base_cooldown = 30
        self.cooldown = 0
        self.projectiles = []
        self.level = 1
        self.max_level = 3
        self.base_damage = 20
        self.upgrade_cost = 50  # Cost to upgrade to next level
        self.cost = 100  # Initial cost to build tower (for currency system)

    def get_stats(self):
        # Scale stats based on level
        damage = self.base_damage + (self.level - 1) * 10  # +10 damage per level
        cooldown = max(10, self.base_cooldown - (self.level - 1) * 5)  # Reduce cooldown, min 10
        range_val = self.range + (self.level - 1) * 25  # +25 range per level
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
            self.upgrade_cost += 50  # Increase cost for next upgrade
            return True
        return False

    def draw(self, screen):
        damage, cooldown, range_val = self.get_stats()
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), 20)
        pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y), range_val, 1)
        # Display level near tower
        font = pygame.font.SysFont("arial", 16)
        text = font.render(str(self.level), True, (255, 255, 255))
        screen.blit(text, (self.x - 5, self.y - 10))
        for projectile in self.projectiles:
            projectile.draw(screen)