import pygame

def main():
    pygame.init()
    display = pygame.display.set_mode((800, 800))
    LAYER = pygame.Surface((800, 800))
    clock = pygame.time.Clock()

    PREVX = -1
    PREVY = -1
    CURX = -1
    CURY = -1

    display.fill((0, 0, 0))

    mouse_type = 0
    color = (255, 255, 255)
    Down = False

    while True:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]:
            color = (255, 0, 0)
        elif pressed[pygame.K_g]:
            color = (0, 255, 0)
        elif pressed[pygame.K_b]:
            color = (0, 0, 255)
        elif pressed[pygame.K_w]:
            color = (255, 255, 255)
        if pressed[pygame.K_SPACE]:
            display.fill((0, 0, 0))
        if pressed[pygame.K_1]:
            mouse_type = 1
        elif pressed[pygame.K_2]:
            mouse_type = 2
        elif pressed[pygame.K_0]:
            mouse_type = 0


        if mouse_type == 0:
            CURX = PREVX
            CURY = PREVY

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Down = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        Down = False

                if event.type == pygame.MOUSEMOTION:
                    # if mouse moved, add point to list
                    CURX = event.pos[0]
                    CURY = event.pos[1]

            if Down:
                pygame.draw.line(display, color, (PREVX, PREVY), (CURX, CURY))

            PREVX = CURX
            PREVY = CURY

            pygame.display.flip()
            clock.tick(60)

        elif mouse_type == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Down = True
                        CURX = event.pos[0]
                        CURY = event.pos[1]
                        PREVX = event.pos[0]
                        PREVY = event.pos[1]
                        LAYER.blit(display, (0, 0))

                if event.type == pygame.MOUSEBUTTONUP:
                    Down = False
                    LAYER.blit(display, (0, 0))

                if event.type == pygame.MOUSEMOTION:
                    if Down:
                        CURX = event.pos[0]
                        CURY = event.pos[1]

            if Down and PREVX != -1 and PREVY != -1 and CURX != -1 and CURY != -1:
                display.blit(LAYER, (0, 0))
                R = Get_rect(PREVX, PREVY, CURX, CURY)
                pygame.draw.rect(display, color, pygame.Rect(R), 1)
                # print("{} {} {} {}".format(prevX, prevY, currentX, currentY))

            pygame.display.flip()
            clock.tick(60)
        elif mouse_type == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Down = True
                        CURX = event.pos[0]
                        CURY = event.pos[1]
                        PREVX = event.pos[0]
                        PREVY = event.pos[1]
                        LAYER.blit(display, (0, 0))

                if event.type == pygame.MOUSEBUTTONUP:
                    Down = False
                    LAYER.blit(display, (0, 0))

                if event.type == pygame.MOUSEMOTION:
                    if Down:
                        CURX = event.pos[0]
                        CURY = event.pos[1]

            if Down and PREVX != -1 and PREVY != -1 and CURX != -1 and CURY != -1:
                display.blit(LAYER, (0, 0))
                R = Get_radius(PREVX, PREVY, CURX, CURY)
                pygame.draw.circle(display, color, (PREVX, PREVY), R, 1)
            pygame.display.flip()
            clock.tick(60)

def Get_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


def Get_radius(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


main()