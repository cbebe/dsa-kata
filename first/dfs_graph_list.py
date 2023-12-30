from fem.graph import AdjList, list2, test_graph_traversal


def dfs(g: AdjList, start: int, val: int) -> list[int] | None:
    seen = [False] * len(g)
    paths = []

    def walk(i: int):
        if seen[i]:
            return
        if i == val:
            paths.append(i)
            return True
        seen[i] = True
        for n, _ in g[i]:
            if walk(n):
                paths.append(i)
                return True
        return False
    if walk(start):
        paths.reverse()
        return paths
    else:
        return None


if __name__ == "__main__":
    test_graph_traversal(dfs, list2)
    print("OK")
