from fem.list import List, test_list
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
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
            self.head = n
            self.tail = n
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
        else:
            self.len += 1

    def append(self, item: T):
        n = Node(item)
        if self.tail is None:
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.len += 1

    def remove(self, item: T) -> T | None:
        lo, hi = 0, self.len
        h, t = self.head, self.tail
        while lo < hi:
            if h.val == item:
                a, b = h.prev, h.next
                if a:
                    a.next = b
                if b:
                    b.prev = a
                h.prev, h.next = None, None
                self.len -= 1
                return h.val
            if t.val == item:
                a, b = t.prev, t.next
                if a:
                    a.next = b
                if b:
                    b.prev = a
                t.prev, t.next = None, None
                self.len -= 1
                return t.val
            lo += 1
            hi -= 1
        if h and h.val == item:
            self.head = None
            self.tail = None
            self.len -= 1
            return h.val
        else:
            return None

    def get(self, idx: int) -> T | None:
        if idx < self.len//2:
            n = self.head
            for j in range(idx):
                n = n.next
            return n.val
        else:
            n = self.tail
            for j in range(self.len-1-idx):
                n = n.prev
            return n.val

    def remove_at(self, idx) -> T | None:
        if idx < 0 or idx >= self.len:
            return None
        elif idx == 0:
            n = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            n.next = None
            self.len -= 1
            return n.val
        elif idx == self.len - 1:
            n = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            n.prev = None
            self.len -= 1
            return n.val
        elif idx < (self.len//2):
            n = self.head
            for i in range(self.len-1-idx):
                n = n.next
            a, b = n.prev, n.next
            a.next, b.prev = b, a
            n.prev, n.next = None, None
            self.len -= 1
            return n.val
        else:
            n = self.tail
            for i in range(self.len-1-idx):
                n = n.prev
            a, b = n.prev, n.next
            a.next, b.prev = b, a
            n.prev, n.next = None, None
            self.len -= 1
            return n.val

    @property
    def length(self) -> int:
        return self.len

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
    ll = DoublyLinkedList[int]()
    test_list(ll)
    print("OK")
