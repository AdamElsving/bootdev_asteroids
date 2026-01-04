import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE, ASTEROID_SPLIT_VELOCITY_MULTIPLIER
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        
        angle = random.randint(ASTEROID_MIN_SPLIT_ANGLE, ASTEROID_MAX_SPLIT_ANGLE)
        fst_asteroid_dir = self.velocity.rotate(angle)
        snd_asteroid_dir = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        fst_asteroid = Asteroid(*self.position, new_radius)
        snd_asteroid = Asteroid(*self.position, new_radius)
        
        fst_asteroid.velocity = fst_asteroid_dir * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        snd_asteroid.velocity = snd_asteroid_dir * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        

