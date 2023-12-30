from collections.abc import Sequence

from fem.trie import Trie as ITrie
from fem.trie import test_trie


class Node:
    pass


class Node(Sequence):
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26

    def __getitem__(self, i: str):
        return self.children[ord(i)-97]

    def __setitem__(self, i: str, val: Node):
        self.children[ord(i)-97] = val

    def __len__(self):
        return 26

    def get_words(self, prefix: str, idx: int, arr: list[str]) -> list[str]:
        word = prefix + chr(idx + 97)
        if self.is_word:
            arr.append(word)
        for i, c in enumerate(self.children):
            if c:
                c.get_words(word, i, arr)
        return arr


class Trie(ITrie):
    def __init__(self):
        self.root = Node()

    def insert(self, item: str):
        c = self.root
        for i in item:
            if c[i] is None:
                c[i] = Node()
            c = c[i]
        c.is_word = True

    def delete(self, item: str):
        c = self.root
        for i in item:
            if c[i] is None:
                break
            c = c[i]
        c.is_word = False

    def find(self, item: str) -> list[str]:
        c = self.root
        for i in item:
            if c[i] is None:
                return []
            c = c[i]
        return c.get_words(item[:-1], ord(item[-1]) - 97, [])


if __name__ == "__main__":
    t = Trie()
    test_trie(t)
    print("OK")
