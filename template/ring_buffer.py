from fem.ring_buffer import RingBuffer as FEMRingBuffer, test_ring_buffer
from typing import TypeVar, Generic

T = TypeVar('T')

class RingBuffer():
    def push(self, item: T):
        pass

    def pop(self) -> T | None:
        pass

    def get(self, idx: int) -> T | None:
        pass

    @property
    def length(self) -> int:
        return -1

if __name__ == "__main__":
    rb = RingBuffer()
    test_ring_buffer(rb)
