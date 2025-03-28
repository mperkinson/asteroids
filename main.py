import pygame
from player import Player
import constants as consts


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {consts.SCREEN_WIDTH}")
    print(f"Screen height: {consts.SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    dt = 0

    p_x = consts.SCREEN_WIDTH / 2
    p_y = consts.SCREEN_HEIGHT / 2
    p = Player(p_x, p_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
