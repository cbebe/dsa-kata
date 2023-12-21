from fem.stack import Stack as FEMStack, test_stack
from typing import TypeVar

T = TypeVar('T')


class Stack(FEMStack[T]):
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
