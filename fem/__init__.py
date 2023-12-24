# So tired of having to rewrite all the tests in Python
undefined = None


class expect:
    def __init__(self, v):
        self.v = v

    def toEqual(self, other):
        assert self.v == other, f"want: {other}, got: {self.v}"
