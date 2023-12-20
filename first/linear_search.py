def linear_fn(haystack: list[int], needle: int):
    for i in haystack:
        if i == needle:
            return True
    return False


if __name__ == "__main__":
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert linear_fn(foo, 69)
    assert not linear_fn(foo, 1336)
    assert linear_fn(foo, 69420)
    assert not linear_fn(foo, 69421)
    assert linear_fn(foo, 1)
    assert not linear_fn(foo, 0)
    print("OK")
