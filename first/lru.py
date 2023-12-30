from fem.lru import LRU as ILRU, test_lru
from first.doubly_linked_list import DoublyLinkedList, Node


class LRU(ILRU):
    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList[int]()
        self.hm = dict[str, Node]()
        self.len = 0
        self.cap = capacity

    def __pop(self, key: str, node: Node) -> int | None:
        _, v = self.dll.pop_node(node)
        self.dll.prepend((key, v))
        self.hm[key] = self.dll.head
        return v

    def get(self, key: str) -> int | None:
        return self.__pop(key, n) if (n := self.hm.get(key)) else None

    def update(self, key: str, val: int):
        if (n := self.hm.get(key)):
            return self.__pop(key, n)
        self.dll.prepend((key, val))
        self.hm[key] = self.dll.head
        self.len += 1

        # We still good
        if self.len <= self.cap:
            return
        # Must drop the tail
        tail = self.dll.tail
        k, _ = tail.val
        self.dll.pop_node(tail)
        del self.hm[k]
        self.len = self.cap


if __name__ == "__main__":
    lru = LRU(3)
    test_lru(lru)
    print("OK")
