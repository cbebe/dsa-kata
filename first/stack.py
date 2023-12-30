from typing import Generic, TypeVar

from fem.stack import Stack as FEMStack
from fem.stack import test_stack

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, item: T):
        self.val = item
        self.prev: Node[T] | None = None


class Stack(FEMStack[T]):
    def __init__(self):
        self.head: Node[T] | None = None
        self._len = 0

    def push(self, item: T):
        node = Node(item)
        node.prev = self.head
        self.head = node
        self._len += 1

    def pop(self) -> T | None:
        if self.head is None:
            return None
        node = self.head
        self.head = node.prev
        self._len -= 1
        node.prev = None
        return node.val

    def peek(self) -> T | None:
        return self.head.val if self.head else None

    @property
    def length(self) -> int:
        return self._len


if __name__ == "__main__":
    s = Stack[int]()
    test_stack(s)
