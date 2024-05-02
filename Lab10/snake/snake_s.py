import pygame
import set
import point

class Snake:
    def __init__(self):
        self.body = [point.Point.generate()]
        self.dx = 0
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        head = self.body[0]
        head.x += self.dx * set.CELL
        head.y += self.dy * set.CELL
        if head.x == set.SCREEN_WIDTH:
            head.x = 0
        if head.x < 0:
            head.x = (set.SCREEN_WIDTH // set.CELL - 1) * set.CELL
        if head.y == set.SCREEN_HEIGHT:
            head.y = 0
        if head.y < 0:
            head.y = (set.SCREEN_HEIGHT // set.CELL - 1) * set.CELL

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(point.Point(head.x , head.y))
            print("Got food! Lenght is:", len(self.body))
            return True

    def draw(self, screen):
        head = self.body[0]
        pygame.draw.rect(screen, set.RED, (head.x, head.y, set.CELL, set.CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, set.YELLOW, (segment.x, segment.y, set.CELL, set.CELL))

