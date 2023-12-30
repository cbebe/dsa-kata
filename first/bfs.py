from fem.tree import Node, test_tree_search
from first.queue import Queue


def bfs(n: Node, val: int):
    q = Queue[Node](n)
    while (curr := q.dequeue()):
        if curr.val == val:
            return True
        if curr.left:
            q.enqueue(curr.left)
        if curr.right:
            q.enqueue(curr.right)
    return False


if __name__ == "__main__":
    test_tree_search(bfs)
    print("OK")
