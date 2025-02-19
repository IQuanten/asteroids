import pygame
from Constants import *
from Player import Player 
from Asteroid import Asteroid
from AsteroidField import AsteroidField
from Shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    game_speed = pygame.time.Clock()
    dt = 0
    points = 0 
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group, drawable_group, updatable_group)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable_group.update(dt)

        for asteroid in asteroid_group:
            if player.isColliding(asteroid):
                print(f"Game over! You scored {points} points!")
                return
            for shot in shots_group:
                if asteroid.isColliding(shot):
                    asteroid.split()
                    shot.kill()
                    points +=1

        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = game_speed.tick(60) / 1000
        
            
if __name__ == "__main__":
    main()