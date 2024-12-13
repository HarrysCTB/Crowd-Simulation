import pygame
import random


class Birds:
    def __init__(self, x, y, screen, width=10, height=10, speed=None, speed_factor=1):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        base_speed = speed or [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.speed = [s * speed_factor for s in base_speed]

    def update(self, screen_width, screen_height):
        """Met à jour la position de l'agent et gère les collisions."""
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # Gestion des collisions avec les bords
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed[1] *= -1


    def draw(self, screen):
        """Dessine l'agent et un cercle autour."""
        pygame.draw.rect(screen, self.color, self.rect)

        # Dessiner un cercle englobant autour du Bird
        center = self.rect.center  # Centre du rectangle
        radius = 100
        pygame.draw.circle(screen, (255, 0, 0), center, radius, 2)