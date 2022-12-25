import pygame
import Common

class SnakeObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.countBlock = 3
        self.widthBlock = 50
        self.heightBlock = 50
        self.width = self.countBlock * self.widthBlock
        self.height = self.countBlock * self.heightBlock

    def update(self):
        pygame.draw.rect(Common.win, Common.red, (1 + self.x, self.y, 50, 50), 2)
        pygame.draw.rect(Common.win, Common.red, (1 + self.x + 50, 0, 50, 50), 2)
        pygame.draw.rect(Common.win, Common.red, (1 + self.x + 100, 0, 50, 50), 2)
        self.move_by_keys()

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += 1
        if keys[pygame.K_LEFT]:
            self.x -= 1