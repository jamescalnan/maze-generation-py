import pygame as pg
from recursive_backtracker import draw_points
from pygame_ops import pygame_fix
from rich.console import Console

c = Console()


def backtrack(goal, root, came_from, colour, multiplier, game_display):
    current = goal
    path = [goal]

    while not current == root:
        path.append(current)
        current = came_from[current]
        c.print(current)
    
    path.append(root)

    path.reverse()

    draw_points(path, game_display, multiplier, colour)
    pg.time.wait(2000)


def adjacent_vertices(G, current_v):
    return_vertices = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            if ((x + current_v[0], y + current_v[1]) in G
                and not all([k == 1 for k in list(map(abs, (x, y)))])):
                return_vertices.append((x + current_v[0], y + current_v[1]))

    return return_vertices

def solve_maze(G, game_display, multiplier, colour, root, goal):
    S = []
    visited = []
    came_from = {}

    S.append(root)

    draw_points([root, goal], game_display, multiplier, (0, 0, 255))
    pg.time.wait(10)
    while len(S) > 0:
        v = S.pop()

        draw_points([v], game_display, multiplier, colour)
        
        #pg.time.wait(1)
        pygame_fix()

        c.print(v)

        if v == goal:
            backtrack(goal, root, came_from, (0, 255, 0), multiplier, game_display)
            return

        if v not in visited:
            visited.append(v)

            for w in adjacent_vertices(G, v):

                S.append(w)
                if w not in visited:
                    came_from[w] = v



