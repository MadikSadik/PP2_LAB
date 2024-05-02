from random import randint
import set

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def generate():
        return Point(randint(0, set.SCREEN_WIDTH // set.CELL - 1) * set.CELL, randint(0, set.SCREEN_HEIGHT // set.CELL - 1) * set.CELL)