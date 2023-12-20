from typing import Callable


def search_test(search: Callable[[list[int], int], bool]):
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert search(foo, 69)
    assert not search(foo, 1336)
    assert search(foo, 69420)
    assert not search(foo, 69421)
    assert search(foo, 1)
    assert not search(foo, 0)
    print("OK")
