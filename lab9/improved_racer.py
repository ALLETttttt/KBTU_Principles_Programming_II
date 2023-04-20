import pygame
import random, time
import sys
from pygame import mixer


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over!", True, black)
score_font = pygame.font.SysFont("Verdana", 40)
total_score = score_font.render("Total score: ", True, black)
coin_font = pygame.font.SysFont("Verdana", 40)
coin = pygame.image.load("coin8.jpg")

FPS = 60
WIDTH = 400
HEIGHT = 600
STEP = 5
ENEMY_STEP = 7
coin_step = 5
upper_coin_step = 6
SCORE = 0
coin_score = 0


clock = pygame.time.Clock()
back_ground = pygame.image.load("AnimatedStreet.png")


screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(white)
pygame.display.set_caption("Street racer")

pygame.mixer.music.load("back_ground.wav")
pygame.mixer.music.play(-1)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, WIDTH-20), 0)

    def update(self):
        global SCORE, ENEMY_STEP, coin_score
        self.rect.move_ip(0, ENEMY_STEP)
        if self.rect.bottom > HEIGHT:
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(20, WIDTH-20), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, WIDTH-20), 500)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -STEP)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, STEP)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin9.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 500)

    def update(self):
        global coin_score
        self.rect.move_ip(0, coin_step)
        if self.rect.top > HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(40, WIDTH-40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def disappear(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, WIDTH-40), 0)


class Upper_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("upper_coin.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 500)

    def update(self):
        global coin_score
        self.rect.move_ip(0, upper_coin_step)
        if self.rect.top > HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(40, WIDTH-40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def disappear(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, WIDTH-40), 0)


P = Player()
E = Enemy()
C = Coin()
U_c = Upper_Coin()

enemies = pygame.sprite.Group()
enemies.add(E)

coins = pygame.sprite.Group()
coins.add(C)

up_coin = pygame.sprite.Group()
up_coin.add(U_c)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    P.update()
    E.update()
    C.update()
    U_c.update()
    
    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                    
        screen.fill(red)
        screen.blit(game_over, (30,250))
        screen.blit(total_score, (30, 320))
        screen.blit(coin_img, (275, 320))
           
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P, coins):
        C.disappear()
        coin_score += 1
        if coin_score % 10 == 0:
            ENEMY_STEP += 2
    
    if pygame.sprite.spritecollideany(P, up_coin):
        U_c.disappear()
        coin_score += 3
        if coin_score % 10 == 0:
            ENEMY_STEP += 2
    

    screen.blit(back_ground, (0, 0))

    E.draw(screen)
    P.draw(screen)
    C.draw(screen)
    U_c.draw(screen)

    coin_img = coin_font.render(str(coin_score), True, white)
    screen.blit(coin_img, (325, 0))

    score_img = score_font.render(str(SCORE), True, black)
    screen.blit(score_img, (0, 0))
    screen.blit(coin, (370, 0))

    pygame.display.update()
    clock.tick(FPS)




