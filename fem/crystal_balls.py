from random import randint
from typing import Callable

from fem import expect


def test_two_crystal_balls(tcb: Callable[[list[bool]], int | None]):
    size = 10000
    data = [False] * size
    idx = randint(0, size - 1)
    for i in range(idx, size):
        data[i] = True
    expect(tcb(data)).toEqual(idx)

    empty = [False] * 821
    expect(tcb(empty)).toEqual(None)

    last = [False] * size
    last[size - 1] = True
    expect(tcb(last)).toEqual(size - 1)

    no_floors = []
    expect(tcb(no_floors)).toEqual(None)

    first = [True] * 100
    expect(tcb(first)).toEqual(0)
