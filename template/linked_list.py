from fem.list import List, test_list
from typing import TypeVar, Generic

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


if __name__ == "__main__":
    ll = LinkedList[int]()
    test_list(ll)
    print("OK")
