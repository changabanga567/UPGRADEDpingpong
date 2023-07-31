import pygame
import random


class Ball:
    def __init__(self, x, y, size, window_width, window_height, is_powerup_ball=False):
        self.x = x
        self.y = y
        self.size = size
        self.dx = random.choice([-5, 5])  # Change here
        self.dy = random.choice([-5, 5])  # Change here
        self.window_width = window_width
        self.window_height = window_height
        self.is_powerup_ball = is_powerup_ball

    def move(self, paddle_player, paddle_bot, powerups):
        self.x += self.dx
        self.y += self.dy

        if self.y < 0 or self.y > self.window_height - self.size:  # Change here
            self.dy *= -1

        if not self.is_powerup_ball:
            if (self.x < paddle_player.x + paddle_player.width and
                paddle_player.y < self.y < paddle_player.y + paddle_player.height):
                self.dx *= -1

            if (self.x + self.size > paddle_bot.x and
                paddle_bot.y < self.y < paddle_bot.y + paddle_bot.height):
                self.dx *= -1

        # Interact with powerups
        for powerup in powerups:
            if powerup.x - powerup.size < self.x < powerup.x + powerup.size and \
               powerup.y - powerup.size < self.y < powerup.y + powerup.size:
                powerup.active = True
                powerups.remove(powerup)

    def move_straight(self):
        self.x += self.dx
        self.y += self.dy

        if self.y < 0 or self.y > self.window_height - self.size:  # Change here
            self.dy *= -1

    def draw(self, screen):
        if self.is_powerup_ball:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(self.x, self.y, self.size, self.size))
            print("Power-up ball drawn!")  # Debug print statement
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.size, self.size))
