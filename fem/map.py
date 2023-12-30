from abc import ABC, abstractmethod

from fem import expect


class HashMap(ABC):
    @abstractmethod
    def set(self, key: str, val: int):
        pass

    @abstractmethod
    def get(self, key: str, val: int) -> int | None:
        pass

    @abstractmethod
    def delete(self, key: str) -> int | None:
        pass

    @abstractmethod
    def size(self) -> int:
        return -1


def test_map(map: HashMap):
    map.set("foo", 55)
    expect(map.size()).toEqual(1)
    map.set("fool", 75)
    expect(map.size()).toEqual(2)
    map.set("foolish", 105)
    expect(map.size()).toEqual(3)
    map.set("bar", 69)
    expect(map.size()).toEqual(4)

    expect(map.get("bar")).toEqual(69)
    expect(map.get("blaz")).toEqual(None)

    map.delete("barblabr")
    expect(map.size()).toEqual(4)

    map.delete("bar")
    expect(map.size()).toEqual(3)
    expect(map.get("bar")).toEqual(None)
