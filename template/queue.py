from typing import TypeVar

from fem.queue import Queue as FQueue
from fem.queue import test_queue

T = TypeVar('T')


class Queue(FQueue[T]):
    def enqueue(self, item: T):
        pass

    def dequeue(self) -> T | None:
        pass

    def peek(self) -> T | None:
        pass

    @property
    def length(self) -> int:
        return -1


if __name__ == "__main__":
    q = Queue[int]()
    test_queue(q)
