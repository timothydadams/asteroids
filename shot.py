from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, radius=self.radius, color="blue", width=2)