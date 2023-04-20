import pygame
x = 0
y = 0
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((650, 650))
done = False
while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
    
    press = pygame.key.get_pressed()
    if y > 0:
        if press[pygame.K_UP]:y -= 20
    if y < 600:
        if press[pygame.K_DOWN]: y += 20
    if x > 0:
        if press[pygame.K_LEFT]: x -= 20
    if x < 600:
        if press[pygame.K_RIGHT]: x += 20

    screen.fill((255, 255, 255))
    pygame.draw.ellipse(screen, (255, 0, 0), (x, y, 50, 50))

    clock.tick(60)
    pygame.display.flip()
