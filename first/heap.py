from typing import Callable, Generic, TypeVar

from fem.heap import MinHeap as IMinHeap
from fem.heap import test_min_heap

T = TypeVar('T')


class MinHeap(IMinHeap[T], Generic[T]):
    __slots__ = ('arr', 'key')

    def __init__(self, key: Callable[[T], int] = lambda x: x):
        self.arr = []
        self.key = key

    def swap(self, a: int, b: int):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    def __heap_up(self):
        i = len(self.arr)-1
        while i:
            p = self.parent(i)
            # Heap condition satisfied
            if self.val(i) > self.val(p):
                break
            self.swap(i, p)
            i = p

    @staticmethod
    def children(i: int):
        return i*2+1, i*2+2

    @staticmethod
    def parent(i: int):
        return (i-1)//2

    def val(self, idx: int) -> int:
        return self.key(self.arr[idx])

    def __heap_down(self):
        i = 0
        while True:
            l, r = self.children(i)
            if l > len(self.arr)-1 or r > len(self.arr)-1:
                break
            v, left, right = self.val(i), self.val(l), self.val(r)
            if left > right and v > right:
                self.swap(i, r)
                i = r
            elif right > left and v > left:
                self.swap(i, l)
                i = l
            else:
                break

    def insert(self, item: T):
        self.arr.append(item)
        self.__heap_up()

    def delete(self) -> T | None:
        if not len(self.arr):
            return None
        val = self.arr[0]
        next = self.arr.pop()
        if len(self.arr):
            self.arr[0] = next
            self.__heap_down()
        return val

    @property
    def length(self) -> int:
        return len(self.arr)


if __name__ == "__main__":
    h = MinHeap[int]()
    test_min_heap(h)
    print("OK")
