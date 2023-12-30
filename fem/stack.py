from abc import ABC, abstractmethod, abstractproperty
from typing import Generic, TypeVar

from fem import expect

T = TypeVar('T')


class Stack(Generic[T], ABC):
    @abstractmethod
    def push(self, item: T):
        pass

    @abstractmethod
    def pop(self) -> T | None:
        pass

    @abstractmethod
    def peek(self) -> T | None:
        pass

    @abstractproperty
    def length(self) -> int:
        return -1


def test_stack(s: Stack[int]):
    s.push(5)
    s.push(7)
    s.push(9)

    expect(s.pop()).toEqual(9)
    expect(s.length).toEqual(2)

    s.push(11)
    expect(s.pop()).toEqual(11)
    expect(s.pop()).toEqual(7)
    expect(s.peek()).toEqual(5)
    expect(s.pop()).toEqual(5)
    expect(s.pop()).toEqual(None)
    expect(s.length).toEqual(0)

    s.push(69)
    expect(s.peek()).toEqual(69)
    expect(s.length).toEqual(1)
    s.pop()

    s.push(1)
    s.push(2)
    expect(s.peek()).toEqual(2)
    print("OK")
