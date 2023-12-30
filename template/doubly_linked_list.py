from typing import Generic, TypeVar

from fem.list import List, test_list

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

    def reverse(self):
        pass

    def __str__(self):
        s = "["
        node = self.head
        while node:
            s += str(node.val)
            node = node.next
            if node:
                s += ", "

        return s + "]"


def test_reverse():
    a = DoublyLinkedList[int]()
    for i in range(5):
        a.append(i)
    b = DoublyLinkedList[int]()
    for i in range(5):
        b.prepend(i)
    print(a)
    a.reverse()
    print(a)
    for i in range(5):
        x = b.get(i)
        y = a.get(i)
        assert x == y, f"wrong item at index {i}, want: {x}, got: {y}"


if __name__ == "__main__":
    test_reverse()
    ll = DoublyLinkedList[int]()
    test_list(ll)
    print("OK")
