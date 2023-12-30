from fem import expect
from fem.tree import Node, create_test_tree_1, create_test_tree_2


def compare_stack(a: Node, b: Node) -> bool:
    qa = [a]
    qb = [b]
    while len(qa) and len(qb):
        na = qa.pop()
        nb = qb.pop()
        if ((na.val != nb.val) or
                ((na.left and not nb.left) or (not na.left and nb.left)) or
                ((na.right and not nb.right) or (not na.right and nb.right))):
            return False
        if na.left:
            qa.append(na.left)
        if na.right:
            qa.append(na.right)
        if nb.left:
            qb.append(nb.left)
        if nb.right:
            qb.append(nb.right)

    return len(qa) + len(qb) == 0


def compare_rec(a: Node, b: Node) -> bool:
    return (
        (a is None and b is None) or
        ((a is not None and b is not None) and
            (a.val == b.val) and
            compare_rec(a.left, b.left) and
            compare_rec(a.right, b.right)))


def compare(a: Node, b: Node) -> bool:
    return compare_rec(a, b)


if __name__ == "__main__":
    a = create_test_tree_1()
    b = create_test_tree_2()
    expect(compare(a, a)).toEqual(True)
    expect(compare(a, b)).toEqual(False)
    print("OK")
