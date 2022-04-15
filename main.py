
import sys
import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 640, 480
FPS = 60

pg.init()

fps_clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

while True:
    screen.fill(BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()
    fps_clock.tick(FPS)
