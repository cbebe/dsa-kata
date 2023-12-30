import math

from fem.crystal_balls import test_two_crystal_balls


def two_crystal_balls(breaks: list[bool]) -> int | None:
    steps = math.floor(math.sqrt(len(breaks)))
    i = -1
    for i in range(steps + 1):
        idx = i * steps
        # Out of bounds, the breaking floor must be in the last portion
        if idx >= len(breaks):
            break
        # Ball broke
        if breaks[idx]:
            break
    for j in range(steps):
        num = (i - 1) * steps + j
        if breaks[num]:
            return num

    return None


if __name__ == "__main__":
    test_two_crystal_balls(two_crystal_balls)
