import pygame
import set
import snake_s
import food
from datetime import datetime
import psycopg2

pygame.init()
screen = pygame.display.set_mode((set.SCREEN_WIDTH, set.SCREEN_HEIGHT))

clock = pygame.time.Clock()
# our class
snake = snake_s.Snake()
food_1 = food.Food()

def draw_grid():
    for i in range(0, set.SCREEN_HEIGHT, set.CELL):
        for j in range(0, set.SCREEN_WIDTH, set.CELL):
            pygame.draw.rect(screen, set.GRAY, (i, j, set.CELL, set.CELL), 1)

#________________________________________________________________________________________________________________________________________

running = True
counter = 0
counter_fon = 0
wait_food = True

#________________________________________________________________________________________________________________________________________


conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Madikosh4268'
)

cur = conn.cursor()

def find_user_and_take_score(text):
    select_query = f"select user_score from users_snake where user_name = '{text}'"
    cur.execute(select_query)
    user_score = cur.fetchone()
    return user_score

def CreateNewAccount(text):
    insert_query = f"insert into users_snake (user_name, user_score) values ('{text}', '{0}')"
    cur.execute(insert_query)
    conn.commit()

def updateScore(coin, name):
    update_query = f"update users_snake set user_score = '{coin}' where user_name = '{name}'"
    cur.execute(update_query)
    conn.commit()
#________________________________________________________________________________________________________________________________________

counter_for_name = 0
in_game = False
in_lobby = True

INPUT_BOX_WIDTH = (set.SCREEN_WIDTH // 4) * 3
INPUT_BOX_HEIGHT = set.SCREEN_HEIGHT // 4
INPUT_BOX_X0 = set.SCREEN_WIDTH // 8 
INPUT_BOX_Y0 = set.SCREEN_HEIGHT // 2  - INPUT_BOX_HEIGHT // 2

TEXT_GREEDING_X0 = set.SCREEN_WIDTH // 2 - set.SCREEN_WIDTH // 4
TEXT_GREEDING_Y0 = INPUT_BOX_Y0 - 60

INPUT_TEXT_Y0 = set.SCREEN_HEIGHT // 2 - set.SCREEN_HEIGHT // 16
INPUT_TEXT_X0 = INPUT_BOX_X0 + 5

START_SAVE_POINT_X0 = 0
START_SAVE_POINT_Y0 = 0
WIDTH_SAVE_BOX = set.CELL - 10
HEIGHT_SAVE_BOX = set.CELL // 2

text_introdution = "Введите ваше имя:"
text = ''
text_for_db = ''
color_inactive = pygame.Color('lightskyblue3')

font = pygame.font.Font("/Users/madiyarbekmutat/Fonts_copy/Arial Unicode.ttf", 40)
font_1 = pygame.font.Font("/Users/madiyarbekmutat/Fonts_copy/Arial Unicode.ttf", 30)
font_2 = pygame.font.Font("/Users/madiyarbekmutat/Fonts_copy/Arial Unicode.ttf", 15)
save_box = pygame.Rect(START_SAVE_POINT_X0, START_SAVE_POINT_Y0, WIDTH_SAVE_BOX, HEIGHT_SAVE_BOX)

#________________________________________________________________________________________________________________________________________

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if in_game:
            # move our snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1 
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1 
                    snake.dy = 0
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if save_box.collidepoint(event.pos):
                    in_lobby = True
                    in_game = False
                    counter_db = counter
                    updateScore(counter_db, text_for_db)
                    counter = 0
        if in_lobby:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if text != '':
                        in_lobby = False
                        in_game = True
                        text_for_db = text
                        user_score = find_user_and_take_score(text_for_db)
                        if user_score is not None:
                            counter += user_score[0]
                            # snake.counter_snake(counter)
                        else:
                            CreateNewAccount(text_for_db)
                        text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    if counter_for_name > 0:
                        counter_for_name -= 1
                else:
                    text += event.unicode
                    counter_for_name += 1
                
    if in_game:
        screen.fill(set.COLORS[counter_fon])
        time_food = datetime.now().second
        

        snake.move()
        # snake.counter_snake(counter)
        for i in range(len(snake.body) - 1, 0, -1):
            if food_1.pos.x == snake.body[i].x and food_1.pos.y == snake.body[i].y:
                food_1.regenerate()
        if snake.check_collision(food_1):
            counter += 1
            food_1.regenerate()
        if time_food % 15 == 0 and wait_food:
            wait_food = False
            food_1.regenerate()
        if time_food % 15 != 0:
            wait_food = True
        

        pygame.draw.rect(screen, set.COLORS[counter_fon], save_box)
        pygame.draw.rect(screen, set.GRAY, save_box, 2)
        save_word = font_2.render('save', True, set.RED)
        screen.blit(save_word, (START_SAVE_POINT_X0 + 5,START_SAVE_POINT_Y0 + 5))
        coins_counter = font.render(str(counter), True, set.GRAY)
        screen.blit(coins_counter, (set.SCREEN_WIDTH - 50, 10))
        coins_counter_fon = font.render(str(counter_fon), True, set.GRAY)
        screen.blit(coins_counter_fon, (set.SCREEN_WIDTH - 50, set.CELL))
        
        if counter >= 4 and counter <8:
            counter_fon = 1
        if counter >= 8 and counter <12:
            counter_fon = 2
        if counter >= 12:
            counter_fon = 3

        snake.draw(screen)
        food_1.draw(screen)
        draw_grid()

    elif in_lobby:
        input_box = pygame.Rect(INPUT_BOX_X0, INPUT_BOX_Y0, INPUT_BOX_WIDTH, INPUT_BOX_HEIGHT)
        color = color_inactive
        screen.fill(set.GRAY)
        pygame.draw.rect(screen, set.WHITE, input_box)
        pygame.draw.rect(screen, color, input_box, 2)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_BACKSPACE]:
            text = text[:-1]

        text_greeding = font.render(text_introdution, True, set.BLACK)
        screen.blit(text_greeding, (TEXT_GREEDING_X0, TEXT_GREEDING_Y0))

        txt_surface = font_1.render(text, True, set.BLACK)
        if txt_surface.get_width() >= INPUT_BOX_WIDTH - 10:
            text = text[:-1]
        screen.blit(txt_surface, (INPUT_TEXT_X0, INPUT_TEXT_Y0))

    pygame.display.flip()
    clock.tick(set.FPS + counter_fon * 5)