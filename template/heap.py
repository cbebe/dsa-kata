from typing import Generic, TypeVar

from fem.heap import MinHeap as IMinHeap
from fem.heap import test_min_heap

T = TypeVar('T')


class MinHeap(IMinHeap[T], Generic[T]):
    def insert(self, item: T):
        pass

    def delete(self) -> T | None:
        pass

    @property
    def length(self) -> int:
        return -1


if __name__ == "__main__":
    h = MinHeap[int]()
    test_min_heap(h)
    print("OK")
