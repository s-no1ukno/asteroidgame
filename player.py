import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        triangle = self.triangle()
        print(f"DEBUG ---> : {triangle}")
        pygame.draw.polygon(screen, "white", triangle, 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right # pyright: ignore
        c = self.position - forward * self.radius + right # pyright: ignore

        return [a, b, c]
