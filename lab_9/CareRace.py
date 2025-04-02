
import pygame, sys, random, time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
GRAY = (169, 169, 169)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
font_button = pygame.font.SysFont("Verdana", 30)

background = pygame.image.load("Lab8/images/AnimatedStreet.png")
pygame.mixer.music.load("Lab8/images/background.wav")
pygame.mixer.music.play(-1)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(10,15)
        self.color = GOLD
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.radius)

    def get_value(self):
        if self.radius <= 11:
            return 1
        elif self.radius <= 13:
            return 2
        elif self.radius <= 15:
            return 3
        elif self.radius <= 17:
            return 4
        else:
            return 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

def restart_game():
    global SPEED, SCORE, game_over, P1, E1, C1, all_sprites, enemies, coins
    SPEED = 5
    SCORE = 0
    game_over = False

    P1 = Player()
    E1 = Enemy()
    C1 = Coin()

    enemies = pygame.sprite.Group()
    enemies.add(E1)

    coins = pygame.sprite.Group()
    coins.add(C1)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)
    all_sprites.add(C1)

def draw_restart_button():
    button_rect = pygame.Rect(120, 400, 160, 50)
    pygame.draw.rect(DISPLAYSURF, GRAY, button_rect, border_radius=10)
    text = font_button.render("Restart", True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    DISPLAYSURF.blit(text, text_rect)
    return button_rect

restart_game()

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED and not game_over:
            SPEED += 0.1

    if not game_over:
        DISPLAYSURF.blit(background, (0, 0))
        scores = font_small.render(str(SCORE), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))

        for entity in all_sprites:
            if isinstance(entity, Coin):
                entity.draw(DISPLAYSURF)
            else:
                DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('Lab8/images/crash.wav').play()
            time.sleep(0.5)
            
            DISPLAYSURF.fill(RED)
            game_over_text = font.render("Game Over", True, BLACK)
            score_text = font_small.render(f"Your score: {SCORE}", True, BLACK)

            DISPLAYSURF.blit(game_over_text, (50, 250))
            DISPLAYSURF.blit(score_text, (120, 320))

            restart_button = draw_restart_button()
            pygame.display.update()

            for entity in all_sprites:
                entity.kill()
            
            game_over = True

        coins_collected = pygame.sprite.spritecollide(P1, coins, True)
        for coin in coins_collected:
            SCORE += coin.get_value()
            if SCORE % 20 == 0 :
                SPEED += 1
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

    elif game_over:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        restart_button = draw_restart_button()
        pygame.display.update()

        if restart_button.collidepoint(mouse_pos) and mouse_click[0]:
            restart_game()

    pygame.display.update()
    FramePerSec.tick(FPS)
