from abc import ABC, abstractmethod

from fem import expect


class Trie(ABC):
    @abstractmethod
    def insert(self, item: str):
        pass

    @abstractmethod
    def delete(self, item: str):
        pass

    @abstractmethod
    def find(self, item: str) -> list[str]:
        return []


def test_trie(trie: Trie):
    trie.insert("foo")
    trie.insert("fool")
    trie.insert("foolish")
    trie.insert("bar")

    expect(sorted(trie.find("fo"))).toEqual([
        "foo",
        "fool",
        "foolish",
    ])

    trie.delete("fool")

    expect(sorted(trie.find("fo"))).toEqual([
        "foo",
        "foolish",
    ])
