import pygame
import Common
import snake

pygame.init()

snake = snake.SnakeObject()

win = Common.win

FPS = 60

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(Common.white)
    snake.update()
    pygame.display.update()
    clock.tick(FPS)