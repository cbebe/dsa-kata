from fem.map import HashMap as IHashMap
from fem.map import test_map


class HashMap(IHashMap):
    def __init__(self):
        self.arr = [None] * 10
        self.len = 0

    def set(self, key: str, val: int):
        idx = hash(key) % len(self.arr)
        if not self.arr[idx]:
            self.arr[idx] = []
        for i, (k, v) in enumerate(self.arr[idx]):
            if k == key:
                self.arr[i] = (key, val)
                return
        self.arr[idx].append((key, val))
        self.len += 1

    def get(self, key: str) -> int | None:
        idx = hash(key) % len(self.arr)
        if not self.arr[idx]:
            return
        for k, v in self.arr[idx]:
            if k == key:
                return v

    def delete(self, key: str) -> int | None:
        idx = hash(key) % len(self.arr)
        if not self.arr[idx]:
            return
        for i, (k, v) in enumerate(self.arr[idx]):
            if k == key:
                self.arr[idx] = self.arr[idx][0:i] + self.arr[idx][i+1:]
                if not len(self.arr[idx]):
                    self.arr[idx] = None
                self.len -= 1
                return v

    def size(self) -> int:
        return self.len


if __name__ == "__main__":
    m = HashMap()
    test_map(m)
    print("OK")
