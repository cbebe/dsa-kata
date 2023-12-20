from typing import Callable
from random import randint


def test_two_crystal_balls(tcb: Callable[[list[bool]], int | None]):
    size = 10000
    data = [False] * size
    idx = randint(0, size - 1)
    for i in range(idx, size):
        data[i] = True
    assert idx == tcb(data)

    empty = [False] * 821
    assert tcb(empty) is None

    last = [False] * size
    last[size - 1] = True
    assert size - 1 == tcb(last)
    print("OK")
