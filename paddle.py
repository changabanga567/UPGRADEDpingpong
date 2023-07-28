import pygame

class Paddle:
    def __init__(self, x, y, width, height, window_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0
        self.speed = 2
        self.color = (255, 255, 255)  # White
        self.score = 0
        self.powerups = []  # List to hold powerups
        self.window_height = window_height

    def move(self, dy):
        if (self.y + dy > 0) and (self.y + dy < self.window_height - self.height):
            self.y += dy

    def ai(self, ball):
        if self.y < ball.y:
            self.move(self.speed)
        elif self.y > ball.y:
            self.move(-self.speed)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def use_powerup(self):
        if self.powerups:
            powerup = self.powerups.pop(0)
            powerup.use(self)
