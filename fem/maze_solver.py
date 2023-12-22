from typing import Callable
from . import expect

Point = (int, int)
Path = list[Point]


def test_maze(solver: Callable[[list[str], str, Point, Point], Path]):
    maze = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]
    maze_result = [
        (10, 0),
        (10, 1),
        (10, 2),
        (10, 3),
        (10, 4),
        (9,  4),
        (8,  4),
        (7,  4),
        (6,  4),
        (5,  4),
        (4,  4),
        (3,  4),
        (2,  4),
        (1,  4),
        (1,  5),
    ]

    result = solver(maze, "x", (10, 0), (1, 5))

    expect(draw_path(maze, result)).toEqual(draw_path(maze, maze_result))


def draw_path(data: list[str], path: Path, interactive=False):
    if interactive:
        import os
        for p in path:
            os.system('clear')
            data2 = [[i for i in j] for j in data]
            if data2[p[1]] and data2[p[1]][p[0]]:
                data2[p[1]][p[0]] = '*'
            m = "\n".join(''.join(j) for j in data2)
            print(m)
            input()
    else:
        data2 = [[i for i in j] for j in data]
        for p in path:
            if data2[p[1]] and data2[p[1]][p[0]]:
                data2[p[1]][p[0]] = '*'
        m = "\n".join(''.join(j) for j in data2)
        return m
