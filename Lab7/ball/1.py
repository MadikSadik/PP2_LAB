import pygame

pygame.init() # to make a pygame
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT)) # setting size of window

WHITE = (255,255,255) # colors
RED = (255,0,0)
x = 100 # coordinates
y = 100
SPEED = 20
RADIUS = 25

FPS = 60
clock = pygame.time.Clock() # setting fps

running = True

while running: # to work without stopping
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # to be able to close the window
            running = False
    
    pressed = pygame.key.get_pressed() # setting keys to press
    if pressed[pygame.K_a]:
        if x - RADIUS > 0:
            x -= SPEED
    if pressed[pygame.K_d]:
        if x + RADIUS < SCREEN_WIDTH: # I made controls WASD
            x += SPEED
    if pressed[pygame.K_w]:
        if y - RADIUS > 0:
            y -= SPEED
    if pressed[pygame.K_s]:
        if y + RADIUS < SCREEN_HEIGHT:
            y += SPEED

    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(x,y),RADIUS) # here I drew a ball

    clock.tick(FPS)

    pygame.display.flip()