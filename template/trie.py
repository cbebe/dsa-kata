from fem.trie import Trie as ITrie
from fem.trie import test_trie


class Trie(ITrie):
    def insert(self, item: str):
        pass

    def delete(self, item: str):
        pass

    def find(self, item: str) -> list[str]:
        return []


if __name__ == "__main__":
    t = Trie()
    test_trie(t)
    print("OK")
