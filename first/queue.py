from typing import Generic, TypeVar

from fem.queue import Queue as FQueue
from fem.queue import test_queue

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, val: T) -> None:
        self.val = val
        self.next: Node[T] | None = None


class Queue(FQueue[T]):
    def __init__(self, *args: T) -> None:
        self.head = None
        self.tail = None
        self._len = 0
        for i in args:
            self.enqueue(i)

    def enqueue(self, item: T):
        n = Node(item)
        if self.tail is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self._len += 1

    def dequeue(self) -> T | None:
        if not self.head:
            return None
        n = self.head
        # If this is also the tail then the queue is empty
        if n == self.tail:
            self.tail = None
        self.head = self.head.next
        n.next = None
        self._len -= 1
        return n.val

    def peek(self) -> T | None:
        return self.head.val if self.head else None

    @property
    def length(self) -> int:
        return self._len


if __name__ == "__main__":
    q = Queue[int]()
    test_queue(q)
    print("OK")
