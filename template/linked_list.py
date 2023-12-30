from typing import Generic, TypeVar

from fem.list import List, test_list

T = TypeVar('T')


class LinkedList(Generic[T], List[T]):
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
        return -1

    def __str__(self):
        s = "["
        node = self.head
        while node:
            s += str(node.val)
            node = node.next
            if node:
                s += ", "

        return s + "]"


if __name__ == "__main__":
    ll = LinkedList[int]()
    test_list(ll)
    print("OK")
