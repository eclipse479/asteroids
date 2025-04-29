import pygame
from circleshape import *


class Asteroids(CircleShape):

   

    def __init__(sefl, x,y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt 
