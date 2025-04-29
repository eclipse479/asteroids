# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updateable, drawable)
Asteroids.containers = (updateable, drawable, asteroids)
AsteroidField.containers = (updateable)

def main():
    pygame.init()
    delta = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        dt = delta.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for thing in updateable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for thing in asteroids:
            pass
        #print("Starting Asteroids!")
        #print(f"Screen width: {SCREEN_WIDTH}")
        #print(f"Screen height: {SCREEN_HEIGHT}")


        pygame.display.flip()



if __name__ == "__main__":
    main()