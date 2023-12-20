from fem.search import test_search


def linear_fn(haystack: list[int], needle: int):
    for i in haystack:
        if i == needle:
            return True
    return False


if __name__ == "__main__":
    test_search(linear_fn)
