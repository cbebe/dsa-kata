from fem.graph import AdjList, list2, test_graph_traversal
from first.queue import Queue


def bfs(g: AdjList, start: int, val: int) -> list[int] | None:
    seen = [False] * len(g)
    prev = [-1] * len(g)
    q = Queue[int](start)
    seen[start] = True
    while q.length:
        curr = q.dequeue()
        if curr == val:
            break
        for i, _ in g[curr]:
            if seen[i]:
                continue
            seen[i], prev[i] = True, curr
            q.enqueue(i)
        seen[curr] = True
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
    test_graph_traversal(bfs, list2)
    print("OK")
