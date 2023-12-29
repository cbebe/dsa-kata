from fem.list import List, test_list
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    __slots__ = ('val', 'prev', 'next')

    def __init__(self, item: T):
        self.val = item
        self.prev: Node[T] | None = None
        self.next: Node[T] | None = None


class DoublyLinkedList(Generic[T], List[T]):
    def __init__(self):
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self.len = 0

    def prepend(self, item: T):
        pass

    def insert_at(self, item: T, idx: int):
        pass

    def append(self, item: T):
        pass

    def remove(self, item: T) -> T | None:
        pass

    def get(self, idx: int) -> T | None:
        pass

    def remove_at(self, idx) -> T | None:
        pass

    @property
    def length(self) -> int:
        return self.len


if __name__ == "__main__":
    ll = DoublyLinkedList[int]()
    test_list(ll)
    print("OK")
