import search_test


def linear_fn(haystack: list[int], needle: int):
    for i in haystack:
        if i == needle:
            return True
    return False


if __name__ == "__main__":
    search_test.search_test(linear_fn)