from fem import expect
from fem.tree import Node, create_test_tree_1


# visit
# recurseL
# recurseR
def pre_order(root: Node):
    nodes = []

    def rec(n: Node):
        nodes.append(n.val)
        if n.left:
            rec(n.left)
        if n.right:
            rec(n.right)

    rec(root)
    return nodes


if __name__ == "__main__":
    a = create_test_tree_1()
    expect(pre_order(a)).toEqual([
        20,
        10,
        5,
        7,
        15,
        50,
        30,
        29,
        45,
        100,
    ])
    print("OK")
