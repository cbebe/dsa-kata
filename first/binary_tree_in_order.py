from fem import expect
from fem.tree import Node, create_test_tree_1


# recurseL
# visit
# recurseR
def in_order(root: Node):
    nodes = []

    def rec(n: Node):
        if n.left:
            rec(n.left)
        nodes.append(n.val)
        if n.right:
            rec(n.right)

    rec(root)
    return nodes


if __name__ == "__main__":
    a = create_test_tree_1()
    expect(in_order(a)).toEqual([
        5,
        7,
        10,
        15,
        20,
        29,
        30,
        45,
        50,
        100,
    ])
    print("OK")
