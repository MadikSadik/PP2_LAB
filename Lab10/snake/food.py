import pygame
import point
import set


class Food:
    def __init__(self):
        self.pos = point.Point.generate()

    def draw(self, screen):
        pygame.draw.rect(screen, set.GREEN, (self.pos.x, self.pos.y, set.CELL, set.CELL))

    def regenerate(self):
        self.pos = point.Point.generate()