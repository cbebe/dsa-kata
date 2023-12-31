from typing import Callable

from fem import expect


def test_search(search: Callable[[list[int], int], bool]):
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    expect(search(foo, 69)).toEqual(True)
    expect(search(foo, 1336)).toEqual(False)
    expect(search(foo, 69420)).toEqual(True)
    expect(search(foo, 69421)).toEqual(False)
    expect(search(foo, 1)).toEqual(True)
    expect(search(foo, 0)).toEqual(False)
