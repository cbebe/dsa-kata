from fem.maze_solver import test_maze, Point, Path


def solve_maze(maze: list[str], wall: str, start: Point, end: Point) -> Path:
    g = [*map(list, maze)]
    seen = [*map(lambda x: [False] * len(x), maze)]
    path = []

    def dfs(p: (int, int)):
        if p == end:
            path.append(p)
            return True
        x, y = p
        if (not (0 <= y < len(g))
                or not (0 <= x < len(g[y]))
                or seen[y][x]
                or g[y][x] == wall):
            return False
        seen[y][x] = True
        for (v, w) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs((x+v, y+w)):
                path.append(p)
                return True
    dfs(start)
    path.reverse()
    return path


if __name__ == "__main__":
    test_maze(solve_maze)
    print("OK")
