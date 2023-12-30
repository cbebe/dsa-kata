from fem.tree import Node, test_tree_search


def dfs(n: Node, val: int):
    """
    On Binary Tree
    """
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


def dfs_on_bst(n: Node, val: int):
    """
    On Binary Search Tree
    """
    if not n:
        return False
    if n.val == val:
        return True
    elif n.val > val:
        return dfs_on_bst(n.left, val)
    else:
        return dfs_on_bst(n.right, val)


if __name__ == "__main__":
    test_tree_search(dfs)
    test_tree_search(dfs_on_bst)
