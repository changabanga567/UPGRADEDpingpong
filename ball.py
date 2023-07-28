import pygame
import random

class Ball:
    def __init__(self, x, y, size, width, height):
        self.x = x
        self.y = y
        self.size = size
        self.dx = 2
        self.dy = 2
        self.width = width
        self.height = height

    def move(self, paddle_player, paddle_bot):
        self.x += self.dx
        self.y += self.dy

        if self.y < 0 or self.y > self.height - self.size:
            self.dy *= -1

        if (self.x < paddle_player.x + paddle_player.width and
           paddle_player.y < self.y < paddle_player.y + paddle_player.height):
            self.dx *= -1

        if (self.x + self.size > paddle_bot.x and
           paddle_bot.y < self.y < paddle_bot.y + paddle_bot.height):
            self.dx *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.size, self.size))
