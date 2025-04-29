# main.py
import pygame
from settings import WIDTH, HEIGHT, BG_COLOR, FPS
from enemy import Enemy
from towers import Tower
from path import draw_path, path

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense")
    clock = pygame.time.Clock()

    enemies = [Enemy(path)]
    towers = []

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                towers.append(Tower(x, y))

        draw_path(screen, path)

        for enemy in enemies:
            if enemy.alive:
                enemy.move()
                enemy.draw(screen)

        living_enemies = [e for e in enemies if e.alive]

        for tower in towers:
            tower.update(living_enemies)
            tower.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
