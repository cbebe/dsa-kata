from typing import Callable


def test_sort(sort: Callable[[list[int]], None]):
    arr = [9, 3, 7, 4, 69, 420, 42]
    sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
    print("OK")

