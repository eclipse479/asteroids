import pygame
from circleshape import *
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    
    def __init__(self, x,y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0


    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius/1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius + right
        c = self.position - forward * self.radius - right

        return [a,b,c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        forward *= PLAYER_SPEED * dt
        self.position += forward
        
    def update(self, dt):

        self.cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot()
            self.cooldown = PLAYER_SHOOT_COOLDOWN

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


class Shot(CircleShape):

    
    def __init__(self, x,y, radius):
        super().__init__(x,y,radius)
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt 

