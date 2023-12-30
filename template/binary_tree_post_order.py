from fem import expect
from fem.tree import Node, create_test_tree_1


def post_order(root: Node):
    return []


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
