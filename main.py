import pygame
import constants as consts


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {consts.SCREEN_WIDTH}")
    print(f"Screen height: {consts.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
