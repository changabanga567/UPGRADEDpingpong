import pygame
import random

class PowerUp:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 255, 0)  # Green
        self.active = False
        self.start_time = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

    def use(self, paddle):
        self.active = True
        self.start_time = pygame.time.get_ticks()

class SpeedBoost(PowerUp):
    def use(self, paddle):
        super().use(paddle)
        paddle.speed *= 2  # Double the paddle's speed

    def end(self, paddle):
        paddle.speed /= 2  # Reset the paddle's speed
