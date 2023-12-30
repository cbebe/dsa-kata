from typing import Generic, TypeVar

from fem.ring_buffer import RingBuffer as IRingBuffer
from fem.ring_buffer import test_ring_buffer

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
