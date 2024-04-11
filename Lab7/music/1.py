import pygame

pygame.init()
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (19, 153, 242)
GRAY = (150, 167, 179)
INDIGO = (75, 0, 130)

#======================
# PNG of buttons
prev = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/pictures/1.png")
next = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/pictures/2.png")
play = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/pictures/3.png")

WIDTH_MINI = 75
HEIGHT_MINI = 75

# buttons position
HEIGHT_PREV_MINI = HEIGHT_MINI 
HEIGHT_NEXT_MINI = HEIGHT_MINI 
HEIGHT_PLAY_MINI = HEIGHT_MINI 
HEIGHT_PAUSE_MINI = HEIGHT_MINI 

prev = pygame.transform.scale(prev, (WIDTH_MINI, HEIGHT_MINI))
next = pygame.transform.scale(next, (WIDTH_MINI, HEIGHT_MINI))
play = pygame.transform.scale(play, (WIDTH_MINI, HEIGHT_MINI))

current_icon = play

#======================

FPS = 30
clock = pygame.time.Clock()
running = True
screen.fill(GRAY)

# 5 musics
music = ["/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/1.mp3",
         "/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/2.mp3",
         "/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/3.mp3",
         "/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/4.mp3",
         "/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab7/music/5.mp3"]

# First music
current_track = 0

# Function which plays the music
def play_music(current_track):
    pygame.mixer.music.load(music[current_track])
    pygame.mixer.music.play()

#======================

space = False # this is for stopping and playing

while running:
    screen.fill(GRAY)

    # Where buttons located
    next_rect = next.get_rect()
    next_rect.left = SCREEN_WIDTH / 2 - WIDTH_MINI / 2 + 80
    next_rect.top = (SCREEN_HEIGHT / 2 + 150) - HEIGHT_NEXT_MINI / 2

    prev_rect = prev.get_rect()
    prev_rect.left = SCREEN_WIDTH / 2 - WIDTH_MINI / 2 - 80
    prev_rect.top = (SCREEN_HEIGHT / 2 + 150) - HEIGHT_NEXT_MINI / 2

    play_rect = play.get_rect()
    current_icon_rect = current_icon.get_rect(topleft = (SCREEN_WIDTH / 2 - WIDTH_MINI / 2, (SCREEN_HEIGHT / 2 + 150) - HEIGHT_NEXT_MINI / 2))

    screen.blit(current_icon, current_icon_rect)
    screen.blit(next, next_rect)
    screen.blit(prev, prev_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if current_track > 0:
                current_track = (current_track - 1)
                play_music(current_track)
                space = True
            else:
                current_track = 4
                play_music(current_track)
                space = True

        if event.key == pygame.K_RIGHT:
            if current_track < 4:
                current_track = (current_track + 1)
                play_music(current_track)
                space = True
            else:
                current_track = 0
                play_music(current_track)
                space = True

       
    # Keys to play a music
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        current_track = 0
        play_music(current_track)
    if pressed[pygame.K_w]:
        current_track = 1
        play_music(current_track)
    if pressed[pygame.K_e]:
        current_track = 2
        play_music(current_track)
    if pressed[pygame.K_r]:
        current_track = 3
        play_music(current_track)
    if pressed[pygame.K_t]:
        current_track = 4
        play_music(current_track)


    if pressed[pygame.K_SPACE]: # To stop a music
        if space is True:
            pygame.mixer.music.stop()
            space = False
        else:
            play_music(current_track)
            space = True

    clock.tick(FPS)
    pygame.display.flip()
    