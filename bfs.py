import random as r
import pygame as pg
from recursive_backtracker import draw_points
from rich.console import Console
from pygame_ops import pygame_fix
from dfs import adjacent_vertices, backtrack


def solve_maze(G, game_display, multiplier, colour, root, goal):
    Q = []
    visited = []
    came_from = {}

    visited.append(root)
    Q.append(root)

    while len(Q) > 0:
        v = Q.pop(0)

        draw_points([v], game_display, multiplier, colour)
        pygame_fix()

        if v == goal:
            backtrack(goal, root, came_from, (0, 255, 0), multiplier, game_display)
            return

        for w in adjacent_vertices(G, v):
            if w not in visited:
                visited.append(w)
                Q.append(w)
                came_from[w] = v
