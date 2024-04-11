import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
currX = -1
currY = -1
counter_figurs = -1
counter_color = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
COLOR = [RED, BLACK, WHITE, GREEN, BLUE]


LMBPressed = False
screen.fill(WHITE)

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_radius(x1, x2, y1, y2):
    return int(math.hypot(x2 - x1, y2 - y1))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB was clicked!")
            print(event.pos)
            LMBPressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBPressed:
                currX = event.pos[0]
                currY = event.pos[1]
            if counter_figurs == -1:
                pygame.draw.circle(screen, COLOR[counter_color], event.pos, 25)
            
            if counter_figurs == 2:
                pygame.draw.circle(screen, WHITE, event.pos, 25)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB was released!")
            print(event.pos)
            LMBPressed = False
            baseLayer.blit(screen, (0, 0))
            currX = event.pos[0]
            currY = event.pos[1]


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        counter_figurs = 0
    if pressed[pygame.K_e]:
        counter_figurs = 1
    if pressed[pygame.K_q]:
        counter_figurs = -1
    
    if pressed[pygame.K_z]:
        counter_color = 0
    if pressed[pygame.K_b]:
        counter_color = 4
    if pressed[pygame.K_v]:
        counter_color = 3
    if pressed[pygame.K_x]:
        counter_color = 1
    if pressed[pygame.K_c]:
        counter_color = 2

    if LMBPressed:
        if counter_figurs == 0:
            screen.blit(baseLayer, (0, 0))
            pygame.draw.rect(
                screen, COLOR[counter_color], calculate_rect(prevX, currX, prevY, currY), 2
            )
        if counter_figurs == 1:
            screen.blit(baseLayer, (0, 0))
            radius = calculate_radius(prevX, currX, prevY, currY)
            pygame.draw.circle(
                screen, COLOR[counter_color], (prevX, prevY), radius, 2
            )
    pygame.display.flip()