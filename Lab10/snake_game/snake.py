import pygame
import random
import time
import db

pygame.init()

# Основные параметры
width, height = 800, 600
block_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

font_small = pygame.font.SysFont(None, 20)
font_large = pygame.font.SysFont(None, 40)
font_input = pygame.font.SysFont(None, 40)

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

clock = pygame.time.Clock()
MOVE_SNAKE = pygame.USEREVENT + 1

# Игровые переменные
snake = []
fruit = ()
golden_fruit = None
golden_fruit_timer = None
direction = "right"
SCORE = 0
grow = 0
last_level_up_score = 0

# Пользователь и уровень
current_user_id = None
current_username = ""
current_level = 1

level_data = {
    1: {"speed": 120, "walls": []},
    2: {"speed": 100, "walls": [pygame.Rect(100, 200, 600, 10)]},
    3: {"speed": 80, "walls": [pygame.Rect(150, 150, 10, 300), pygame.Rect(640, 100, 10, 400)]},
}

current_speed = level_data[current_level]["speed"]
pygame.time.set_timer(MOVE_SNAKE, current_speed)

def draw_multiline_text(text, x, y, font, color):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        screen.blit(line_surface, (x, y + i * font.get_height()))

def draw_score():
    screen.blit(font_small.render(f"SCORE: {SCORE}", True, colors["white"]), (10, 10))

def draw_level():
    screen.blit(font_small.render(f"LEVEL: {current_level}", True, colors["white"]), (width - 100, 10))

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, colors["red"], wall)

def draw_timer(timer):
    text = font_small.render(f"gold time: {max(0, round(5 - timer, 1))}", True, colors["white"])
    screen.blit(text, (10, 30))

def spawn_fruit():
    while True:
        new = (
            random.randint(0, (width // block_size) - 1) * block_size,
            random.randint(0, (height // block_size) - 1) * block_size,
        )
        collision = False
        if current_level in level_data:
            for wall in level_data[current_level]["walls"]:
                if wall.collidepoint(new):
                    collision = True
                    break
        if not collision:
            return new

def reset_game():
    global snake, fruit, golden_fruit, golden_fruit_timer, direction, SCORE, grow, last_level_up_score, current_level
    snake = [(width // 2, height // 2)]
    fruit = spawn_fruit()
    golden_fruit = None
    golden_fruit_timer = None
    direction = "right"
    SCORE = 0
    grow = 0
    current_level = 1
    last_level_up_score = 0
    update_speed()

def update_speed():
    pygame.time.set_timer(MOVE_SNAKE, level_data[current_level]["speed"])

def get_top_3_users():
    return db.get_top_3_users()

def draw_top_users(users):
    text = "TOP 3 PLAYERS\n"
    for username, score, level in users:
        text += f"{username} - {score} pts (Lvl {level})\n"
    draw_multiline_text(text.strip(), 300, 270, font_small, colors["white"])

def game_over():
    screen.fill(colors["red"])
    draw_multiline_text(f"YOU LOST\nSCORE: {SCORE}", 300, 100, font_large, colors["white"])
    
    top_users = get_top_3_users()
    draw_top_users(top_users)
    
    restart_button = pygame.Rect(300, 400, 200, 50)
    pygame.draw.rect(screen, colors["green"], restart_button)
    screen.blit(font_large.render("RESTART", True, colors["black"]), (restart_button.x + 20, restart_button.y + 10))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    db.save_score(current_user_id, SCORE, current_level)
                    reset_game()
                    return
        clock.tick(30)

def prompt_for_username():
    global current_user_id, current_username
    input_box = pygame.Rect(width // 4, height // 3, width // 2, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    username = ""
    prompt_text = font_large.render("Enter your username:", True, colors["white"])
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN and username:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
        
        screen.fill(colors["black"])
        screen.blit(prompt_text, (width // 4, height // 4))
        txt_surface = font_input.render(username, True, color)
        input_box.w = max(200, txt_surface.get_width() + 10)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

    current_username = username
    current_user_id = db.get_or_create_user(username)

# Старт
db.create_tables()
reset_game()
prompt_for_username()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            db.save_score(current_user_id, SCORE, current_level)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                db.save_score(current_user_id, SCORE, current_level)
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != "left":
                direction = "right"
            elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != "right":
                direction = "left"
            elif event.key in (pygame.K_UP, pygame.K_w) and direction != "down":
                direction = "up"
            elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != "up":
                direction = "down"

        if event.type == MOVE_SNAKE:
            head_x, head_y = snake[0]
            if direction == "right":
                head_x += block_size
            elif direction == "left":
                head_x -= block_size
            elif direction == "up":
                head_y -= block_size
            elif direction == "down":
                head_y += block_size

            head_x %= width
            head_y %= height
            new_head = (head_x, head_y)

            if new_head in snake[1:]:
                game_over()
                continue

            if current_level in level_data:
                for wall in level_data[current_level]["walls"]:
                    if wall.collidepoint(new_head):
                        game_over()
                        continue

            snake.insert(0, new_head)

            if new_head == fruit:
                fruit = spawn_fruit()
                SCORE += 1

                if SCORE % 10 == 0 and SCORE != last_level_up_score:
                    last_level_up_score = SCORE
                    current_level += 1
                    if current_level in level_data:
                        update_speed()
                

                if golden_fruit is None and random.random() < 0.1:
                    golden_fruit = spawn_fruit()
                    golden_fruit_timer = time.time()
            elif golden_fruit and new_head == golden_fruit:
                SCORE += 3
                grow += 3
                golden_fruit = None
                golden_fruit_timer = None
            else:
                if golden_fruit and time.time() - golden_fruit_timer >= 5:
                    golden_fruit = None
                    golden_fruit_timer = None
                if grow > 0:
                    grow -= 1
                else:
                    snake.pop()

    screen.fill(colors["black"])
    if current_level in level_data:
        draw_walls(level_data[current_level]["walls"])

    for segment in snake:
        pygame.draw.rect(screen, colors["red"], pygame.Rect(segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, colors["green"], pygame.Rect(fruit[0], fruit[1], block_size, block_size))

    if golden_fruit:
        pygame.draw.rect(screen, colors["white"], pygame.Rect(golden_fruit[0], golden_fruit[1], block_size, block_size))
        draw_timer(time.time() - golden_fruit_timer)

    draw_score()
    draw_level()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
