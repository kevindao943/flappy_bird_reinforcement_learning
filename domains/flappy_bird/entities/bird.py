import pygame
from flappy_bird.constants.constants import *

class Bird:
    def __init__(self):
        self.image = pygame.Surface((34, 24))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    