import pygame as pg
import sys
pg.init()

size = width, height = 1000, 600
colors = dict(black = (0, 0, 0),
              white = (255, 255, 255)
              )

screen = pg.display.set_mode(size)

bg_1 = pg.transform.scale(pg.image.load("background_layer_1.png"), (size))
bg_2 = pg.transform.scale(pg.image.load("background_layer_2.png"), (size))
bg_3 = pg.transform.scale(pg.image.load("background_layer_3.png"), (size))

x = 20
y = 50

i = 0
while True:
    screen.blit(bg_1, (i * 0.1, 0))
    screen.blit(bg_1, (width + i * 0.1, 0))
    screen.blit(bg_2, (i * 0.7, 0))
    screen.blit(bg_2, (width + i * 0.7, 0))
    screen.blit(bg_3, (i * 1, 0))
    screen.blit(bg_3, (width + i * 1, 0))

    if (i==-width):
        screen.blit(bg_1, (width + i * 0.1, 0))
        screen.blit(bg_2, (width + i * 0.7, 0))
        screen.blit(bg_3, (width + i * 1, 0))
        i = 0

    i -= 1

    # add the square
    pg.draw.rect(screen, 'red', pg.Rect(x, y, 60, 60))

    # moving square on pressing keys
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        y -= 2
    if key[pg.K_DOWN]:
        y += 2
    if key[pg.K_LEFT]:
        x -= 2
    if key[pg.K_RIGHT]:
        x += 2

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.display.update()

pg.QUIT()