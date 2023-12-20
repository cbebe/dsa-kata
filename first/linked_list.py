import fem_list
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, val: T):
        self.val = val
        self.next: Node[T] | None = None


class LinkedList(fem_list.List[T]):
    def __init__(self):
        self.head: Node[T] | None = None

    def prepend(self, item: T):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_at(self, item: T, idx: int):
        if idx == 0:
            self.prepend(item)
            return
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

    def append(self, item: T):
        i = Node(item)
        node = self.head
        if node is None:
            self.head = i
        else:
            while node.next:
                node = node.next
            node.next = i

    def remove(self, item: T) -> T | None:
        node = self.head
        # This is the only element
        if node and node.val == item:
            self.head = node.next
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
        return ret.val

    def get(self, idx: int) -> T | None:
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
            return node.val
        for _ in range(idx - 1):
            if not node:
                return
            node = node.next
        if not node or not node.next:
            return
        ret = node.next
        node.next = ret.next
        return ret.val

    @property
    def length(self) -> int:
        node = self.head
        total = 0
        while node:
            total += 1
            node = node.next
        return total

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
    fem_list.test_list(ll)
    print("OK")
