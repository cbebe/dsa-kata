from fem.sort import test_sort


def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    idx = lo-1
    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    return idx


def qs(arr: list[int], lo: int, hi: int):
    """
    hi is inclusive
    """
    if lo >= hi:
        return
    pidx = partition(arr, lo, hi)
    qs(arr, lo, pidx - 1)
    qs(arr, pidx + 1, hi)


def quick_sort(arr: list[int]):
    qs(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    test_sort(quick_sort)
