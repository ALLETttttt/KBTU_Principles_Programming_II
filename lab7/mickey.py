import pygame
import datetime
width,height = 800, 800
pygame.init()
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Mickey`s CLOCK')
running = True
image = pygame.image.load(r'C:\Users\user\Downloads\777.jpg')
hand1 = pygame.image.load('mikey_hand1.png')
hand2 = pygame.image.load('mikey_hand2.png')
while running:
    screen.blit(image,(0, 0))
    key = pygame.key.get_pressed()
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    anglesecond = second*6-56
    angleminute = minute*6+50
    img1 = pygame.transform.rotate(hand1,-anglesecond)
    x1 = img1.get_width()/2
    y1 = img1.get_height()/2
    img2=pygame.transform.rotate(hand2,-angleminute)
    x2 = img2.get_width()/2
    y2 = img2.get_height()/2
    screen.blit(img1,(400-int(x1), 400-int(y1)))
    screen.blit(img2,(400-int(x2), 400-int(y2)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.flip()