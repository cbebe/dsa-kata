from fem import expect
from fem.tree import Node, create_test_tree_1
# Assumes that we have a working implementation of `compare`
from first.compare_binary_trees import compare


def insert(n: Node, item: int):
    if item <= n.val:
        if n.left:
            insert(n.left, item)
        else:
            n.left = Node(item)
    else:
        if n.right:
            insert(n.right, item)
        else:
            n.right = Node(item)


def create_bst() -> Node:
    """
    Creates a Binary search tree identical to the tree in create_test_tree_1
    """
    n = Node(20)
    insert(n, 10)
    insert(n, 15)
    insert(n, 5)
    insert(n, 7)
    insert(n, 50)
    insert(n, 100)
    insert(n, 30)
    insert(n, 29)
    insert(n, 45)

    return n


if __name__ == "__main__":
    a = create_test_tree_1()
    bst = create_bst()
    expect(compare(a, bst)).toEqual(True)
    print("OK")
