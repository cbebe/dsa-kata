from fem.lru import LRU as ILRU, test_lru


class LRU(ILRU):
    def __init__(self, capacity: int):
        pass

    def get(self, key: str) -> int | None:
        pass

    def update(self, key: str, val: int):
        pass


if __name__ == "__main__":
    lru = LRU(3)
    test_lru(lru)
    print("OK")
