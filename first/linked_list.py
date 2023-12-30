from typing import Generic, TypeVar

from fem.list import List, test_list

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.next: Node[T] | None = None


class LinkedList(List[T]):
    def __init__(self):
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self._len = 0

    def prepend(self, item: T):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self._len += 1

    def insert_at(self, item: T, idx: int):
        if idx == 0:
            return self.prepend(item)
        if idx == self._len:
            return self.append(item)

        node = self.head
        for _ in range(idx - 1):
            # We went out of bounds
            if not node:
                return
            node = node.next
        if not node or not node.next:
            return
        i = Node[T](item)
        i.next = node.next
        node.next = i
        self._len += 1

    def append(self, item: T):
        # First item
        if self.tail is None:
            return self.prepend(item)
        i = Node(item)
        self.tail.next = i
        self.tail = i
        self._len += 1

    def remove(self, item: T) -> T | None:
        node = self.head
        # It's in the first element
        if node and node.val == item:
            self.head = node.next
            if node == self.tail:
                self.tail = None
            self._len -= 1
            return node.val
        while node and node.next and node.next.val != item:
            node = node.next
        # Out of bounds or not found
        if ((not node)
                or (not node.next)
                or (node.next and node.next.val != item)):
            return None
        ret = node.next
        node.next = ret.next
        self._len -= 1
        if ret == self.tail:
            self.tail = node
        if ret == self.head:
            self.head = ret.next
        ret.next = None
        return ret.val

    def get(self, idx: int) -> T | None:
        if idx == 0:
            return self.head and self.head.val
        if idx == self._len - 1:
            return self.tail and self.tail.val
        node = self.head
        for _ in range(idx):
            if not node:
                break
            node = node.next
        return node and node.val

    def remove_at(self, idx: int) -> T | None:
        node = self.head
        if node is None:
            return None
        if idx == 0:
            self.head = node.next
            self._len -= 1
            node.next = None
            if node == self.tail:
                self.tail = None
            return node.val
        for _ in range(idx - 1):
            if not node:
                return
            node = node.next
        if not node or not node.next:
            return
        ret = node.next
        node.next = ret.next
        if ret == self.tail:
            self.tail = node
        ret.next = None
        self._len -= 1
        return ret.val

    @property
    def length(self) -> int:
        return self._len

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
