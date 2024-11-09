import pygame
import time
import random

pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake properties
block_size = 10
snake_speed = 15
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 35)

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x, y = width / 2, height / 2
    dx, dy = 0, 0

    snake_body = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -block_size, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = block_size, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -block_size
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, block_size

        # Update snake position
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += dx
        y += dy

        screen.fill(blue)
        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(screen, black, [segment[0], segment[1], block_size, block_size])

        # Eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
