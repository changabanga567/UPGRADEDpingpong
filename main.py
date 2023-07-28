import pygame
from paddle import Paddle
from ball import Ball
from powerup import PowerUp, SpeedBoost

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
BALL_SIZE = 15
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a font object
font = pygame.font.Font(None, 36)

# Create the paddles and ball
paddle_player = Paddle(50, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT)
paddle_bot = Paddle(WIDTH - 50, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT)
ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_SIZE, WIDTH, HEIGHT)

clock = pygame.time.Clock()

# Create a list of powerups and a timer
powerups = []
powerup_timer = 0

# Main game loop
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_player.move(-2)
    elif keys[pygame.K_DOWN]:
        paddle_player.move(2)
    elif keys[pygame.K_SPACE]:
        paddle_player.use_powerup()

    paddle_bot.ai(ball)
    ball.move(paddle_player, paddle_bot)

    # Check if the ball is off the screen
    if ball.x < 0:
        paddle_bot.score += 1
        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_SIZE, WIDTH, HEIGHT)
    elif ball.x > WIDTH - ball.size:
        paddle_player.score += 1
        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_SIZE, WIDTH, HEIGHT)

    # Check if any power-ups have ended
    for powerup in paddle_player.powerups:
        if powerup.active and pygame.time.get_ticks() - powerup.start_time > 5000:  # 5 seconds
            powerup.end(paddle_player)
            paddle_player.powerups.remove(powerup)

    # Drawing
    screen.fill((0, 0, 0))
    paddle_player.draw(screen)
    paddle_bot.draw(screen)
    ball.draw(screen)

    # Draw the scores
    score_text = font.render(f"Player: {paddle_player.score}   AI: {paddle_bot.score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
