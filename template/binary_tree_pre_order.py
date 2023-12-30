from fem import expect
from fem.tree import Node, create_test_tree_1


def pre_order(root: Node):
    return []


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
