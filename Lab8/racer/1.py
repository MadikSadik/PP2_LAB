import pygame
import random
import sys
import time

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

coins = 0

BACKGROUND = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab8/racer/resources/AnimatedStreet.png")

clock = pygame.time.Clock()

music = ["/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab8/racer/resources/background.wav",
         "/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab8/racer/resources/crash.wav"]

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

current_track = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab8/racer/resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab8/racer/resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.acpect_ratio = 1
        self.height = self.width / self.acpect_ratio
        self.image = pygame.image.load("/Users/madiyarbekmutat/Desktop/kbtu_pp/pp2_lab/Lab8/racer/resources/coin.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)


def play_music(current_track):
    pygame.mixer.music.load(music[current_track])
    pygame.mixer.music.play()


SPEED = 5

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
E1 = Enemy()
COIN = Coin()

enemies.add(E1)
all_sprites.add(P1, E1, COIN)

done = False

FPS = 60

play_music(current_track)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        current_track = 1
        play_music(current_track)
        screen.fill(colorRED)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()
        
    pygame.display.flip()
    clock.tick(FPS)