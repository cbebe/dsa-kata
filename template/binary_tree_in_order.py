from fem import expect
from fem.tree import Node, create_test_tree_1


def in_order(root: Node):
    return []


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
