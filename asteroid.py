import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(angle)
        vect2 = self.velocity.rotate(-angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        aster1 = Asteroid(self.position.x, self.position.y, radius)
        aster1.velocity = vect1 * 1.2
        aster2 = Asteroid(self.position.x, self.position.y, radius)
        aster2.velocity = vect2 * 1.2
    