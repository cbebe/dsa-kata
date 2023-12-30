from fem import expect
from fem.tree import Node, create_test_tree_1, create_test_tree_2


def compare(a: Node, b: Node) -> bool:
    return False


if __name__ == "__main__":
    a = create_test_tree_1()
    b = create_test_tree_2()
    expect(compare(a, a)).toEqual(True)
    expect(compare(a, b)).toEqual(False)
    print("OK")
