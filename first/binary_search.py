from fem.search import test_search


def binary_fn(haystack: list[int], needle: int):
    lo = 0
    hi = len(haystack)
    while lo < hi:
        m = lo + ((hi - lo) // 2)
        v = haystack[m]
        if v == needle:
            return True
        elif v > needle:
            hi = m
        else:
            lo = m + 1

    return False


if __name__ == "__main__":
    test_search(binary_fn)
    print("OK")
