import pygame
import datetime

pygame.init()
START_X = 0
START_Y = 0
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED, vsync=1)

PLACE_FOR_CLOCK_X = SCREEN_WIDTH - 200
PLACE_FOR_CLOCK_Y = 50

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,250,0)
RED = (255,0,0)
BLUE = (0,0,255)
SKY_BLUE = (19,153,242)

FPS = 60
clock = pygame.time.Clock()

#==========================

background = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/clock/mickey-clock.jpg")
WIDTH_BACKGROUND = 500
HEIGHT_BACKGROUND = 500
CENTER_X_POS = SCREEN_WIDTH / 2 - WIDTH_BACKGROUND / 2
CENTER_Y_POS = SCREEN_HEIGHT / 2 - HEIGHT_BACKGROUND / 2


big_arrow = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/clock/big-arrow.png")
BIG_ARROW_WIDTH = 35
BIG_ARROW_ASPECT_RATIO = 0.13
BIG_ARROW_HEIGHT = BIG_ARROW_WIDTH / BIG_ARROW_ASPECT_RATIO
big_arrow = pygame.transform.scale(big_arrow, (BIG_ARROW_WIDTH, BIG_ARROW_HEIGHT))

big_arrow_rect = big_arrow.get_rect()
big_arrow_rect.center = CENTER


small_arrow = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/clock/small-arrow.png")
SMALL_ARROW_WIDTH = 35
SMALL_ARROW_ASPECT_RATIO = 0.305
SMALL_ARROW_HEIGHT = SMALL_ARROW_WIDTH / SMALL_ARROW_ASPECT_RATIO
small_arrow = pygame.transform.scale(small_arrow, (SMALL_ARROW_WIDTH, SMALL_ARROW_HEIGHT))

small_arrow_rect = small_arrow.get_rect()
small_arrow_rect.center = CENTER

#==========================

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle_second = datetime.datetime.now().second * (-6)
    angle_minute = datetime.datetime.now().minute * (-6)
    screen.fill(BLACK)
    screen.blit(background, (CENTER_X_POS, CENTER_Y_POS))

    rotated_big_arrow = pygame.transform.rotate(big_arrow, angle_second)
    rotated_big_arrow_rect = rotated_big_arrow.get_rect()
    rotated_big_arrow_rect.center = big_arrow_rect.center
    screen.blit(rotated_big_arrow, rotated_big_arrow_rect)

    rotated_small_arrow = pygame.transform.rotate(small_arrow, angle_minute)
    rotated_small_arrow_rect = rotated_small_arrow.get_rect()
    rotated_small_arrow_rect.center = small_arrow_rect.center
    screen.blit(rotated_small_arrow, rotated_small_arrow_rect)

    #==========================

    today = datetime.datetime.now().replace(microsecond=0)
    string = str(today)
    string = string[11:]
    pygame.display.update()

    clock.tick(FPS)
    pygame.display.flip()