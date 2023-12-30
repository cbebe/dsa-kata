from fem.map import HashMap as IHashMap
from fem.map import test_map


class HashMap(IHashMap):
    def set(self, key: str, val: int):
        pass

    def get(self, key: str) -> int | None:
        pass

    def delete(self, key: str) -> int | None:
        pass

    def size(self) -> int:
        return -1


if __name__ == "__main__":
    m = HashMap()
    test_map(m)
    print("OK")
