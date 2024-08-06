import pygame
from snake import Snake

snake = Snake()


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True
velocity = 10

while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for segment in snake.body:
        pygame.draw.rect(
            screen,
            snake.color,
            pygame.Rect(segment[0], segment[1], snake.body_size, snake.body_size)
        )

    pygame.display.update()
    clock.tick(60)

pygame.quit()
