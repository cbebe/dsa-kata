from abc import ABC, abstractmethod, abstractproperty
from typing import Generic, TypeVar

from fem import expect

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

    expect(list.get(2)).toEqual(9)
    expect(list.remove_at(1)).toEqual(7)
    expect(list.length).toEqual(2)

    list.append(11)
    expect(list.remove_at(1)).toEqual(9)
    expect(list.remove(9)).toEqual(None)
    expect(list.remove_at(0)).toEqual(5)
    expect(list.remove_at(0)).toEqual(11)
    expect(list.length).toEqual(0)

    list.prepend(5)
    list.prepend(7)
    list.prepend(9)

    expect(list.get(2)).toEqual(5)
    expect(list.get(0)).toEqual(9)
    expect(list.remove(9)).toEqual(9)
    expect(list.length).toEqual(2)
    expect(list.get(0)).toEqual(7)

    list.insert_at(6, 1)
    expect(list.get(1)).toEqual(6)
