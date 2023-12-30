from fem import expect
from abc import ABC, abstractmethod


class LRU(ABC):
    @abstractmethod
    def get(self, key: str) -> int | None:
        pass

    @abstractmethod
    def update(self, key: str, val: int):
        pass


def test_lru(lru: LRU):
    """
    Make sure to set the capacity to 3
    """
    expect(lru.get("foo")).toEqual(None)
    lru.update("foo", 69)
    expect(lru.get("foo")).toEqual(69)

    lru.update("bar", 420)
    expect(lru.get("bar")).toEqual(420)

    lru.update("baz", 1337)
    expect(lru.get("baz")).toEqual(1337)

    lru.update("ball", 69420)
    expect(lru.get("ball")).toEqual(69420)
    expect(lru.get("foo")).toEqual(None)
    expect(lru.get("bar")).toEqual(420)
    lru.update("foo", 69)
    expect(lru.get("bar")).toEqual(420)
    expect(lru.get("foo")).toEqual(69)

    expect(lru.get("baz")).toEqual(None)
