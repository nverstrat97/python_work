import pygame
from settings import WIDTH, HEIGHT
from game import Game

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tower Defense")
        clock = pygame.time.Clock()  # Frame rate control
        game = Game(screen)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    game.handle_click(pygame.mouse.get_pos())

            game.update()
            clock.tick(60)  # Cap at 60 FPS

        pygame.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()

if __name__ == "__main__":
    main()