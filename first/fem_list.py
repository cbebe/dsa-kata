from abc import ABC, abstractmethod, abstractproperty
from typing import TypeVar, Generic

T = TypeVar('T')


class List(Generic[T], ABC):
    @abstractmethod
    def prepend(self, item: T):
        pass

    @abstractmethod
    def insert_at(self, item: T, idx: int):
        pass

    @abstractmethod
    def append(self, item: T):
        pass

    @abstractmethod
    def remove(self, item: T) -> T | None:
        pass

    @abstractmethod
    def get(self, idx: int) -> T | None:
        pass

    @abstractmethod
    def remove_at(self, idx: int) -> T | None:
        pass

    @abstractproperty
    def length(self) -> int:
        return -1


def test_list(list: List[int]):
    list.append(5)
    list.append(7)
    list.append(9)

    assert list.get(2) == 9
    assert list.remove_at(1) == 7
    assert list.length == 2

    list.append(11)
    assert list.remove_at(1) == 9
    assert list.remove(9) is None
    assert list.remove_at(0) == 5
    assert list.remove_at(0) == 11
    assert list.length == 0

    list.prepend(5)
    list.prepend(7)
    list.prepend(9)

    assert list.get(2) == 5
    assert list.get(0) == 9
    assert list.remove(9) == 9
    assert list.length == 2
    assert list.get(0) == 7

    list.insert_at(6, 1)
    assert list.get(1) == 6
