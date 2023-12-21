from abc import ABC, abstractmethod, abstractproperty
from typing import TypeVar, Generic
from . import expect, undefined

T = TypeVar('T')


class RingBuffer(Generic[T], ABC):
    @abstractmethod
    def push(self, item: T):
        pass

    @abstractmethod
    def pop(self) -> T | None:
        pass

    @abstractmethod
    def get(self, idx: int) -> T | None:
        pass

    @abstractproperty
    def length(self) -> int:
        return -1


def test_ring_buffer(buffer: RingBuffer[int]):
    buffer.push(5);
    expect(buffer.pop()).toEqual(5);
    expect(buffer.pop()).toEqual(undefined);

    buffer.push(42);
    buffer.push(9);
    expect(buffer.pop()).toEqual(42);
    expect(buffer.pop()).toEqual(9);
    expect(buffer.pop()).toEqual(undefined);

    buffer.push(42);
    buffer.push(9);
    buffer.push(12);
    expect(buffer.get(2)).toEqual(12);
    expect(buffer.get(1)).toEqual(9);
    expect(buffer.get(0)).toEqual(42);
    print("OK")
