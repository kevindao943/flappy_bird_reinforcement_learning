import pygame
from random import randint
from flappy_bird.constants.constants import *

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.top_rect = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, 50, SCREEN_HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

    def is_off_screen(self):
        return self.x + 50 < 0