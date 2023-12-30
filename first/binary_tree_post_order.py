from fem import expect
from fem.tree import Node, create_test_tree_1


# recurseL
# visit
# recurseR
def post_order(root: Node):
    nodes = []

    def rec(n: Node):
        if n.left:
            rec(n.left)
        if n.right:
            rec(n.right)
        nodes.append(n.val)

    rec(root)
    return nodes


if __name__ == "__main__":
    a = create_test_tree_1()
    expect(post_order(a)).toEqual([
        7,
        5,
        15,
        10,
        29,
        45,
        30,
        100,
        50,
        20,
    ])
    print("OK")
