import pygame
from src.settings import WIDTH, HEIGHT
from src.core.game import Game

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Tower Defense")
        clock = pygame.time.Clock()
        game = Game(screen)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    game.handle_click(pygame.mouse.get_pos())
                elif event.type == pygame.VIDEORESIZE:
                    # Handle window resizing
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    game.update_window_size(event.w, event.h)

            game.update()
            clock.tick(60)  # Cap at 60 FPS

        pygame.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()

if __name__ == "__main__":
    main()