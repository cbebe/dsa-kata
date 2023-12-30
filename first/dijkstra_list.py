from math import inf

from fem.graph import AdjList, list1, test_graph_traversal
from first.heap import MinHeap


def dijkstra(g: AdjList, start: int, val: int) -> list[int] | None:
    seen = [False] * len(g)
    prev = [-1] * len(g)
    dists = [inf] * len(g)
    dists[start] = 0
    pq = MinHeap(key=lambda x: dists[x])
    pq.insert(start)
    while pq.length:
        curr = pq.delete()
        seen[curr] = True
        if curr == val:
            break
        for i, w in g[curr]:
            if seen[i]:
                continue
            d = dists[curr] + w
            if d < dists[i]:
                prev[i] = curr
                dists[i] = d
                pq.insert(i)
    path = []
    next = val
    while (next := prev[next]) != -1:
        path.append(next)

    if len(path):
        path.reverse()
        path.append(val)
        return path
    else:
        return None


if __name__ == "__main__":
    test_graph_traversal(dijkstra, list1, directed=False)
    print("OK")
