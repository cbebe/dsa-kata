from abc import ABC, abstractmethod, abstractproperty
from typing import TypeVar, Generic

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

    assert s.pop() == 9
    assert s.length == 2

    s.push(11)
    assert s.pop() == 11
    assert s.pop() == 7
    assert s.peek() == 5
    assert s.pop() == 5
    assert s.pop() is None
    assert s.length == 0

    s.push(69)
    assert s.peek() == 69
    assert s.length == 1
    s.pop()

    s.push(1)
    s.push(2)
    assert s.peek() == 2
    print("OK")
