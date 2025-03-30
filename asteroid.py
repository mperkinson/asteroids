from circleshape import CircleShape
import pygame
import random
import constants as consts


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= consts.ASTEROID_MIN_RADIUS:
            self.kill()
            return

        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle) * 1.2
        vec2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - consts.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vec1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vec2

        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)

        self.kill()
