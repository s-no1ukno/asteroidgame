import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # initialization of game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        delta = clock.tick(60)  # clock.tick() returns ms since last tick
        dt = delta / 1000  # sets the delta time to seconds since last tick


if __name__ == "__main__":
    main()
