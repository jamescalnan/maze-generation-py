from prims_algorithm import generate_maze
#from dfs import solve_maze
from bfs import solve_maze
import pygame as pg
from rich.console import Console

c = Console()

black = (0, 0, 0)
white = (255, 255, 255)

screen_size = 600

pg.init()
game_display = pg.display.set_mode((screen_size, screen_size))
game_display.fill(black)
pixel_array = pg.PixelArray(game_display)


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



def print_maze(maze, multiplier=1):
    for point in maze:
        pg.draw.rect(game_display, white, (point[0] * multiplier, point[1] * multiplier, multiplier, multiplier))
        pg.display.update()

maze_width = 10
multiplier = int((screen_size / maze_width) / 2)


while True:
    game_display.fill((0, 0, 0))
    maze, targets = generate_maze(maze_width, game_display, white, multiplier)

    pg.time.wait(1000)

    solve_maze(maze, game_display, multiplier, (255, 0 , 0,), targets[0], targets[1])

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:

            if event.type == pg.K_ESCAPE:
                pg.quit()
                quit()