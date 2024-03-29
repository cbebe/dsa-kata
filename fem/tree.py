from typing import Callable

from fem import expect


def str_util(root, space):
    # Base case
    if (root is None):
        return ""
    space += 10
    s = str_util(root.right, space)
    s += "\n"
    s += ((space - 10) * " ")
    s += str(root.val)
    s += str_util(root.left, space)
    return s


class Node:
    __slots__ = ('val', 'right', 'left')

    def __init__(self, item):
        self.val = item
        self.right: Node | None = None
        self.left: Node | None = None

    def __str__(self):
        return str_util(self, 0)


def create_test_tree_1():
    root = Node(20)

    root.right = Node(50)
    root.right.right = Node(100)
    root.right.left = Node(30)
    root.right.left.right = Node(45)
    root.right.left.left = Node(29)

    root.left = Node(10)
    root.left.right = Node(15)
    root.left.left = Node(5)
    root.left.left.right = Node(7)

    return root


def create_test_tree_2():
    root = Node(20)

    root.right = Node(50)
    root.right.left = Node(30)
    root.right.left.right = Node(45)
    root.right.left.left = Node(29)

    root.left = Node(10)
    root.left.right = Node(15)
    root.left.left = Node(5)
    root.left.left.right = Node(7)

    return root


def test_tree_search(search: Callable[[Node, int], bool]):
    tree = create_test_tree_1()
    expect(search(tree, 45)).toEqual(True)
    expect(search(tree, 7)).toEqual(True)
    expect(search(tree, 69)).toEqual(False)
