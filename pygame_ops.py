import pygame as pg

def pygame_fix():
    for event in pg.event.get():
            pg.time.wait(50)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:

                if event.type == pg.K_ESCAPE:
                    pg.quit()
                    quit()