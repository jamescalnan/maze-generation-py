import random as r
import pygame as pg
from pygame_ops import pygame_fix
from rich.console import Console

c = Console()


def draw_points(points: list, game_display, multiplier: int, colour, delay=0):
    for point in points:
        pg.draw.rect(game_display,
                     colour,
                     (point[0] * multiplier + 5,
                      point[1] * multiplier + 5,
                      multiplier,
                      multiplier))
        if delay != 0:
            pg.display.update()
            pg.time.wait(delay)
    pygame_fix()
    pg.display.update()


def available_vertices(width):
    return_vertices = set()

    for i in range(0, width * 2, 2):
        for j in range(0, width * 2, 2):
            return_vertices.add((i, j))

    return list(sorted(return_vertices))


def generate_maze(width, game_display, colour, multiplier=1):
    def midpoint(p1, p2) -> tuple:
        return (int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2))

    graph = available_vertices(width)

    #draw_points(graph, game_display, multiplier, (255, 0, 0))

    current_v = graph[0]

    maze = [current_v]
    stack = [current_v]
    visited = [current_v]

    previous_v = current_v

    while True:
        adjacent_vertices = []#[(x + current_v[0], y + current_v[1]) for x in range(-1, 2) for y in range(-1, 2) if (not (x, y) == (0, 0) and not all(list(map(abs, (x, y)))) and (x + current_v[0], y + current_v[1]) not in visited and (x + current_v[0], y + current_v[1]) in graph)]

        for x in range(-2, 3):
            for y in range(-2, 3):
                if (not (x, y) == (0, 0) 
                    and not all([k == 2 for k in list(map(abs, (x, y)))])
                    and (x + current_v[0], y + current_v[1]) not in visited
                    and (x + current_v[0], y + current_v[1]) in graph):

                    adjacent_vertices.append((x + current_v[0], y + current_v[1]))

        if len(adjacent_vertices) > 0:
            chosen_v = adjacent_vertices[r.randint(0, len(adjacent_vertices) - 1)]
            edge = midpoint(current_v, chosen_v)

            visited.append(chosen_v)
            stack.append(chosen_v)
            maze += [edge, chosen_v]

            draw_points([edge], game_display, multiplier, colour)

            current_v = chosen_v
        elif len(stack) > 0:
            current_v = stack.pop()
        else:
            break

        draw_points([previous_v], game_display, multiplier, colour)
        draw_points([current_v], game_display, multiplier, (0, 255, 0))

        previous_v = current_v

    return maze, (graph[0], graph[-1])
