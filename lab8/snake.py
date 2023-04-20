import pygame, sys
import random

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
BLOCK_SIZE = 20
score = 0
level_cnt = 1
FPS = 5

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Food:
    def __init__(self):
        self.location = Point(random.randint(1, 19), random.randint(1, 19))

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 1
        self.dy = 0


    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)

        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (255, 0, 0), rect)


    def check_collision(self, food):
        global score, level_cnt, FPS
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                food.location = Point(random.randint(1, 19), random.randint(1, 19))
                score += 1
                if score % 3 == 0:
                    level_cnt += 1
                    FPS += 0.5
    

    def check_fail(self):
        for block in self.body[1:]:
            if self.body[0].x == block.x and self.body[0].y == block.y:
                pygame.quit()
                sys.exit()


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    font = pygame.font.SysFont("Verdana", 20)
    score_img = font.render("SCORE:", True, BLACK)
    level_img = font.render("LEVEL:", True, BLACK)

    snake = Snake()
    food = Food()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1

        SCREEN.fill((0, 0, 255))

        for block in snake.body[1:]:
            while block == food.location:
                food.draw()

        snake.check_fail()
        
        snake.check_collision(food)
        snake.move()

        snake.draw()
        food.draw()
        
        drawGrid()
        SCREEN.blit(score_img, (0, 0))
        scores = font.render(str(score), True, BLACK)
        levels = font.render(str(level_cnt), True, BLACK)
        SCREEN.blit(levels, (370, 0))
        SCREEN.blit(scores, (85, 0))
        SCREEN.blit(level_img, (300, 0))

        pygame.display.update()
        CLOCK.tick(FPS)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)


main()