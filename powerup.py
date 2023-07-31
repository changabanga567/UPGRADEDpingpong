import pygame
from ball import Ball

class PowerUp:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 255, 0)  # Green
        self.active = False
        self.start_time = pygame.time.get_ticks()
        self.spawn_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 24)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        text_surface = self.font.render("P", True, (0, 0, 0))
        screen.blit(text_surface, (self.x - self.size // 2, self.y - self.size // 2))

    def use(self, paddle):
        self.active = True
        self.start_time = pygame.time.get_ticks()

class InvisibleBall(PowerUp):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.color = (255, 255, 0)  # Yellow

    def use(self, paddle):
        super().use(paddle)
        return Ball(paddle.x, paddle.y, 15, paddle.window_width, paddle.window_height, is_powerup_ball=True)
    
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(screen, self.hover_color, pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2,
                                   self.y + self.height / 2 - text_surface.get_height() / 2))

    def is_over(self, pos):
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height


    def update(self):
        self.clicked = False
        self.draw(screen)

