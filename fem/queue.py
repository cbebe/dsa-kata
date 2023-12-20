from abc import ABC, abstractmethod, abstractproperty
from typing import TypeVar, Generic

T = TypeVar('T')


class Queue(Generic[T], ABC):
    @abstractmethod
    def enqueue(self, item: T):
        pass

    @abstractmethod
    def dequeue(self) -> T | None:
        pass

    @abstractmethod
    def peek(self) -> T | None:
        pass

    @abstractproperty
    def length(self) -> int:
        return -1


def test_queue(q: Queue[int]):
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(9)

    assert q.dequeue() == 5
    assert q.length == 2

    q.enqueue(11)
    assert q.dequeue() == 7
    assert q.dequeue() == 9
    assert q.peek() == 11
    assert q.dequeue() == 11
    assert q.dequeue() is None
    assert q.length == 0

    q.enqueue(69)
    assert q.peek() == 69
    assert q.length == 1
    q.dequeue()

    q.enqueue(1)
    q.enqueue(2)
    assert q.peek() == 1
    print("OK")
