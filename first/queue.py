from fem.queue import Queue as FQueue, test_queue
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, val: T) -> None:
        self.val = val
        self.next: Node[T] | None = None


class Queue(FQueue[T]):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, item: T):
        n = Node(item)
        if self.tail is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def dequeue(self) -> T | None:
        if not self.head:
            return None
        n = self.head
        # If this is also the tail then the queue is empty
        if n == self.tail:
            self.tail = None
        self.head = self.head.next
        n.next = None
        return n.val

    def peek(self) -> T | None:
        return self.tail.val if self.tail else None

    @property
    def length(self) -> int:
        i = 0
        node = self.head
        while node:
            i += 1
            node = node.next
        return i


if __name__ == "__main__":
    q = Queue[int]()
    test_queue(q)
