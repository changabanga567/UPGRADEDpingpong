import pygame
import random
from paddle import Paddle
from ball import Ball
from powerup import PowerUp, InvisibleBall, Button

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
font_game_over = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 36)

# Create a button
continue_button = Button(WIDTH / 2 - 100, HEIGHT / 2 + 50, 200, 60, 'Continue', (50, 50, 50), (100, 100, 100))

def run_game():
    # Create the paddles and ball
    paddle_player = Paddle(50, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT, WIDTH)
    paddle_bot = Paddle(WIDTH - 50, HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, HEIGHT, WIDTH)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_SIZE, WIDTH, HEIGHT)

    # Create a list of powerups and a timer
    powerups = []
    powerup_timer = 0

    # Create a variable to store the game state
    game_over = False
    winner = None

    # Create a clock object
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if game_over and continue_button.is_over((x, y)):
                    run_game()

        # Game logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle_player.move(2.8)  # Positive value moves the paddle up
        elif keys[pygame.K_DOWN]:
            paddle_player.move(-2.8)  # Negative value moves the paddle down

        paddle_bot.ai(ball)
        ball.move(paddle_player, paddle_bot, powerups)

        for powerup_ball in paddle_player.powerup_balls:
            powerup_ball.move_straight()
            if powerup_ball.x < 0 or powerup_ball.x > WIDTH - powerup_ball.size:
                paddle_player.powerup_balls.remove(powerup_ball)

        # Check if the ball has hit any powerups
        for powerup in powerups:
            if powerup.x - powerup.size < ball.x < powerup.x + powerup.size and \
                powerup.y - powerup.size < ball.y < powerup.y + powerup.size:
                paddle_player.powerups.append(powerup)
                powerups.remove(powerup)

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

        # Spawn powerups
        powerup_timer += 1
        if powerup_timer >= FPS * 5:  # Spawn a new powerup every 5 seconds
            powerup = InvisibleBall(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20)
            powerups.append(powerup)
            powerup_timer = 0

        # Check if the game is over
        if paddle_player.score >= 5:
            game_over = True
            winner = "Player"
        elif paddle_bot.score >= 5:
            game_over = True
            winner = "AI"

        # Drawing
        screen.fill((0, 0, 0))
        if not game_over:
            paddle_player.draw(screen)
            paddle_bot.draw(screen)
            ball.draw(screen)

            # Draw the powerups
            for powerup in powerups:
                powerup.draw(screen)

            # Draw the scores
            score_text = font.render(f"Player: {paddle_player.score}   AI: {paddle_bot.score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
        else:
            game_over_text = font_game_over.render(f"{winner} Wins!", True, (255, 255, 255))
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
            continue_button.draw(screen)

        # Flip the display
        pygame.display.flip()
        
    # Quit Pygame
    pygame.quit()

# Start the game
run_game()
