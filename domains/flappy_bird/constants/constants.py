SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

GRAVITY = 0.25
FLAP_STRENGTH = -6.5
PIPE_SPEED = 3
PIPE_GAP = 150

FPS = 60

from numpy import linspace

bird_y_bins = linspace(0, SCREEN_HEIGHT, 10)
bird_velocity_bins = linspace(-10, 10, 10)
pipe_distance_bins = linspace(0, SCREEN_WIDTH, 10)
pipe_gap_top_bins = linspace(-SCREEN_HEIGHT, SCREEN_HEIGHT, 10)
pipe_gap_bottom_bins = linspace(-SCREEN_HEIGHT, SCREEN_HEIGHT, 10)