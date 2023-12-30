from typing import Callable

from fem import expect


def test_sort(sort: Callable[[list[int]], None]):
    arr = [9, 3, 7, 4, 69, 420, 42]
    sort(arr)
    expect(arr).toEqual([3, 4, 7, 9, 42, 69, 420])
    print("OK")
