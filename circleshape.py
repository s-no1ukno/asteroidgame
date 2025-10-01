import pygame

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        # will use this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

        # distance = self.position.distance_to(other.position)
        #
        # print(f"debug ====> self.pos {self.position} || other pos {other.position}")
        # print(f"debug ====> distance {distance}")
        # print(f"debug ====> self.radius {self.radius} || other radius {other.radius}")
        #
        # if distance <= self.radius + other.radius:
        #     print("true")
        #     return True
        # else:
        #     print("false")
        #     return False
