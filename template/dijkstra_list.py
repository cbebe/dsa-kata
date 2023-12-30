from fem.graph import AdjList, list1, test_graph_traversal


def dijkstra(g: AdjList, start: int, val: int) -> list[int] | None:
    pass


if __name__ == "__main__":
    test_graph_traversal(dijkstra, list1, directed=False)
    print("OK")
