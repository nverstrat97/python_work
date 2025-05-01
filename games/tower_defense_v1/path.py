# path.py
import pygame

def draw_path(screen, path):
    if len(path) > 1:
        pygame.draw.lines(screen, (0, 255, 0), False, path, 4)

original_path = [(0, 300), (200, 300), (200, 100), (600, 100), (600, 400), (800, 400)]

# will be scaled dynamically in game.py
path = original_path
