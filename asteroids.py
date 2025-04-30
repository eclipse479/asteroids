import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS


class Asteroids(CircleShape):

   

    def __init__(sefl, x,y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        forward = pygame.Vector2(self.velocity).rotate(angle)
        asteroid1 = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = forward * 1.2

        forward = pygame.Vector2(self.velocity).rotate(-angle)
        asteroid2 = Asteroids(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = forward * 1.2