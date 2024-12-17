import pygame
import sys
from numpy import digitize
from flappy_bird.constants.constants import *
from flappy_bird.entities.bird import Bird
from flappy_bird.entities.pipe import Pipe
from copy import deepcopy

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.bins = [bird_y_bins, bird_velocity_bins, pipe_distance_bins, pipe_gap_top_bins, pipe_gap_bottom_bins]

    def discretize_state(self, state):
        discretized_state = tuple(digitize(state[i], self.bins[i]) for i in range(len(state)))
        return discretized_state

    def get_state(self, bird, pipes):
        next_pipe = None
        for pipe in pipes:
            if pipe.x + 50 > bird.rect.x:
                next_pipe = pipe
                break
        if next_pipe is None:
            next_pipe = pipes[0]
        bird_y = bird.rect.y
        bird_velocity = bird.velocity
        pipe_distance = next_pipe.x - bird.rect.x
        pipe_gap_top = bird.rect.y - next_pipe.height
        pipe_gap_bottom = (next_pipe.height + PIPE_GAP) - bird.rect.y
        continuous_state = [bird_y, bird_velocity, pipe_distance, pipe_gap_top, pipe_gap_bottom]
        discretized_state = self.discretize_state(continuous_state)
        return discretized_state
    
    # def get_action(self, state, policy, epsilon=0.1):
    #     if random.uniform(0, 1) < epsilon:  # Explore
    #         return random.choice([0, 1])
    #     else:  # Exploit
    #         if state not in policy:
    #             policy[state] = [0, 0]  # Initialize state-action values
    #         return int(policy[state][1] > policy[state][0])  # Action with max Q-value
    
    def get_reward(self, bird, pipes):
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                return -100
        if bird.rect.top <= 0 or bird.rect.bottom >= SCREEN_HEIGHT:
            return -100
        return 1
    
    def step(self, bird, pipes, action, score, running):
        if action == 1: # flap
            bird.flap()
        bird.update()
        for pipe in pipes:
            pipe.update()
            if pipe.is_off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH))
                score += 1
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                running = False
        if bird.rect.top <= 0 or bird.rect.bottom >= SCREEN_HEIGHT:
            running = False
        return bird, pipes, score, running
    
    def get_next_state(self, bird, pipes, action):
        bird = deepcopy(bird)
        pipes = deepcopy(pipes)
        bird, pipes, _, _ = self.step(bird, pipes, action, 0, True) # does not consider 'score' & 'running'
        discretized_next_state = self.get_state(bird, pipes)
        return discretized_next_state

    def run_game(self):
        bird = Bird()
        pipes = [Pipe(SCREEN_WIDTH)]
        score = 0
        running = True
        while running:
            self.screen.fill(BLUE)
            action = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    action = 1
            bird, pipes, score, running = self.step(bird, pipes, action, score, running)
            bird.draw(self.screen)
            for pipe in pipes:
                pipe.draw(self.screen)
            score_text = self.font.render(f"Score: {score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
