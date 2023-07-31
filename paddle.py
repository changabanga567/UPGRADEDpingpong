import pygame
from ball import Ball

class Paddle:
    def __init__(self, x, y, width, height, window_height, window_width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0
        self.speed = 2.8
        self.color = (255, 255, 255)  # White
        self.score = 0
        self.powerups = []  # List to hold powerups
        self.window_height = window_height
        self.window_width = window_width
        self.powerup_balls = []  # List to hold balls created by powerups

    def move(self, dy):
        if (self.y + dy > 0) and (self.y + dy < self.window_height - self.height):
            self.y += dy

    def ai(self, ball):
        middle_paddle = self.y + self.height / 2
        if ball.dx > 0:  # Only move if the ball is moving towards the AI
            if middle_paddle < ball.y + ball.size / 2:
                self.move(self.speed)
            elif middle_paddle > ball.y + ball.size / 2:
                self.move(-self.speed)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def use_powerup(self):
        if self.powerups:
            new_ball = self.powerups[-1].use(self)  # Use the last powerup in the list
            if new_ball:  # If the powerup returns a new ball
                self.powerup_balls.append(new_ball)
                print("Power-up used!")  # Debug print statement
