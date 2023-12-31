from abc import ABC, abstractmethod, abstractproperty
from typing import Generic, TypeVar

from fem import expect

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

    expect(q.dequeue()).toEqual(5)
    expect(q.length).toEqual(2)

    q.enqueue(11)
    expect(q.dequeue()).toEqual(7)
    expect(q.dequeue()).toEqual(9)
    expect(q.peek()).toEqual(11)
    expect(q.dequeue()).toEqual(11)
    expect(q.dequeue()).toEqual(None)
    expect(q.length).toEqual(0)

    q.enqueue(69)
    expect(q.peek()).toEqual(69)
    expect(q.length).toEqual(1)
    q.dequeue()

    q.enqueue(1)
    q.enqueue(2)
    expect(q.peek()).toEqual(1)
