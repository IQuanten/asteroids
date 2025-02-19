import pygame
import random
from CircleShape import CircleShape
from Constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        randomAngle = random.uniform(20, 50)
        newVector1 = self.velocity.rotate(randomAngle) 
        newVector2 = self.velocity.rotate(-randomAngle) 

        newRadius = old_radius - ASTEROID_MIN_RADIUS
        roid1 = Asteroid(self.position.x, self.position.y, newRadius)
        roid1.velocity = newVector1 * 1.2

        roid2 = Asteroid(self.position.x, self.position.y, newRadius)
        roid2.velocity = newVector2 * 1.2