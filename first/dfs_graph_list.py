from fem.graph import AdjList, list2, test_graph_traversal


def dfs(g: AdjList, start: int, val: int) -> list[int] | None:
    seen = [False] * len(g)
    paths = []

    def walk(i: int):
        if seen[i]:
            return False
        seen[i] = True
        paths.append(i)
        if i == val:
            return True
        for n, _ in g[i]:
            if walk(n):
                return True
        paths.pop()
        return False
    if walk(start):
        return paths
    else:
        return None


if __name__ == "__main__":
    test_graph_traversal(dfs, list2)
    print("OK")
