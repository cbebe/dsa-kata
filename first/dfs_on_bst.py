from fem.tree import Node, test_tree_search


def dfs(n: Node, val: int):
    q = [n]
    while len(q):
        curr = q.pop()
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        if curr.val == val:
            return True
    return False


if __name__ == "__main__":
    test_tree_search(dfs)
