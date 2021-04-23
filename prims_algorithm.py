import random as r
import pygame as pg
import collections
from pygame_ops import pygame_fix
from rich.console import Console
from recursive_backtracker import draw_points

c = Console()


def available_vertices(width, game_display, multiplier):
    return_vertices = set()
    edges = {}

    for i in range(0, width * 2, 2):
        for j in range(0, width * 2, 2):
            return_vertices.add((i, j))

            if i < width * 2 - 2:
                edges[r.randint(1, 9999)] = (i + 1, j)

            if j < width * 2 - 2:
                edges[r.randint(1, 9999)] = (i, j + 1)

    pygame_fix()

    return list(sorted(return_vertices)), [x[1] for x in sorted(edges.items())]


def connected_vertices(available_v, edge):
    if (edge[0] - 1, edge[1]) in available_v and (edge[0] + 1, edge[1]) in available_v:
        return [(edge[0] - 1, edge[1]), (edge[0] + 1, edge[1])]
    else:
        return [(edge[0], edge[1] + 1), (edge[0], edge[1] - 1)]


def adjacent_edges(available_v, V, edges, maze):
    return_values = []

    for vertex in V:
        possible_edges = [(vertex[0] + 1, vertex[1]),
                          (vertex[0] - 1, vertex[1]),
                          (vertex[0], vertex[1] + 1),
                          (vertex[0], vertex[1] - 1)]
        for edge in possible_edges



def generate_maze(width, game_display, colour, multiplier=1):
    vertices, edges = available_vertices(width, game_display, multiplier)
    
    maze = []

    V = [r.randint(0, len(vertices))]

    while True:
        



        pygame_fix()

    return maze
