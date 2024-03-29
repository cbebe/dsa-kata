from typing import TypeVar

from fem.stack import Stack as IStack
from fem.stack import test_stack

T = TypeVar('T')


class Stack(IStack[T]):
    def push(self, item: T):
        pass

    def pop(self) -> T | None:
        pass

    def peek(self) -> T | None:
        pass

    @property
    def length(self) -> int:
        return -1


if __name__ == "__main__":
    s = Stack[int]()
    test_stack(s)
    print("OK")
