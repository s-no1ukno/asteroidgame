import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            # else spawn 2 new asteroids
            angle = random.uniform(20, 50)
            new_vec_1 = self.velocity.rotate(angle)
            new_vec_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_1.velocity = new_vec_1 * 1.2
            new_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_2.velocity = new_vec_2 * 1.2
            self.kill()


