from fem.list import List, test_list
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    __slots__ = ('val', 'prev', 'next')

    def __init__(self, item: T):
        self.val = item
        self.prev: Node[T] | None = None
        self.next: Node[T] | None = None

    def __str__(self):
        return f"({self.val})"


class DoublyLinkedList(Generic[T], List[T]):
    def __init__(self):
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self.len = 0

    def prepend(self, item: T):
        n = Node(item)
        if self.head is None:
            self.head = self.tail = n
        else:
            self.head.prev = n
            n.next = self.head
            self.head = n

        self.len += 1

    def insert_at(self, item: T, idx: int):
        if idx == 0:
            return self.prepend(item)
        elif idx == self.len:
            return self.append(item)
        elif idx > self.len:
            raise Exception("oh no")
        else:
            self.len += 1
            curr = self.__get_at(idx)
            n = Node(item)
            n.next = curr
            n.prev = curr.prev
            curr.prev = n
            n.prev.next = n

    def append(self, item: T):
        n = Node(item)
        if self.tail is None:
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.len += 1

    def remove(self, item: T) -> T | None:
        curr = self.head
        for i in range(self.len):
            if not curr or curr.val == item:
                break
            curr = curr.next
        return self.__pop_node(curr)

    def get(self, idx: int) -> T | None:
        n = self.__get_at(idx)
        return n.val if n else None

    def remove_at(self, idx: int) -> T | None:
        curr = self.__get_at(idx)
        return self.__pop_node(curr)

    @property
    def length(self) -> int:
        return self.len

    def __get_at(self, idx: int) -> Node[T] | None:
        curr = self.head
        for i in range(idx):
            if not curr:
                break
            curr = curr.next
        return curr

    def __pop_node(self, curr: Node[T]) -> T | None:
        if not curr:
            return None

        self.len -= 1

        if self.len == 0:
            self.head = self.tail = None
            curr.next = curr.prev = None
            return curr.val

        if curr.prev:
            curr.prev.next = curr.next
            if curr == self.tail:
                self.tail = curr.prev
        if curr.next:
            curr.next.prev = curr.prev
            if curr == self.head:
                self.head = curr.next
        curr.next = curr.prev = None
        return curr.val


if __name__ == "__main__":
    ll = DoublyLinkedList[int]()
    test_list(ll)
    print("OK")
