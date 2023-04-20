import pygame
import random
from pygame import mixer

mixer.init()
pygame.init()

bugatti = pygame.image.load(r'C:\Users\user\Downloads\BUGATTI.jpg')

arr = [
    r'C:\Users\user\Downloads\SAINt JHN _ Imanbek - Roses - Imanbek Remix.mp3',
    r'C:\Users\user\Downloads\Ellis & Laura Brehm - Start Over (Frank Pole remix).mp3',
    r'C:\Users\user\Downloads\Efemero - Amelia.mp3',
    r'C:\Users\user\Downloads\kittie-look-so-pretty.mp3',
    r'C:\Users\user\Downloads\haroinfather - Forever.mp3',
    r'C:\Users\user\Downloads\azimbek-bajlin-men-shn-london-auylda_(muzzonas.ru).mp3',
    r'C:\Users\user\Downloads\Mitchel - Упс Ты Не Та.mp3'
]


screen = pygame.display.set_mode((1280, 720))
done = False

loc = 0
voice = 0.1

pygame.mixer.music.load(arr[loc])
pygame.mixer.music.play()
pygame.mixer.music.queue(arr[random.randrange(0, 7)])

while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if i.key == pygame.K_RSHIFT:
                pygame.mixer.music.unpause()
            if i.key == pygame.K_LEFT:
                if loc >= 1:
                    loc -= 1
                else:
                    loc = 6
                pygame.mixer.music.stop()
                pygame.mixer.music.load(arr[loc])
                pygame.mixer.music.play()
            if i.key == pygame.K_RIGHT:
                if loc <= 6:
                    loc += 1
                else:
                    loc = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load(arr[loc])
                pygame.mixer.music.play()
            if i.key == pygame.K_UP:
                voice += 0.1
                pygame.mixer.music.set_volume(voice)
            if i.key == pygame.K_DOWN:
                voice -= 0.1
                pygame.mixer.music.set_volume(voice)
    screen.blit(bugatti, (0, 0))
    pygame.display.flip()   

pygame.mixer.music.queue(arr[random.randrange(0, 7)])
pygame.quit()

    

