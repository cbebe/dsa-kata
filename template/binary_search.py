from fem.search import test_search


def binary_fn(haystack: list[int], needle: int):
    return False


if __name__ == "__main__":
    test_search(binary_fn)
