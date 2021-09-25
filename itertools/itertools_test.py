import pytest
import time

import mitertools
import itertools

# Infinite iterators. Iterators for which next() is very slow.


class BaseTest:
    f = ""

    def call(self, *args, **kwargs):
        result = getattr(mitertools, self.f)(*args, **kwargs)
        expected = getattr(itertools, self.f)(*args, **kwargs)
        return result, expected

    def compare(self, a, b, n=None):
        """Compare the first n elements of iterables a and b."""
        slice = itertools.islice(zip(a, b), n)
        assert all([x == y for x, y in slice])


class TestCombinations(BaseTest):
    f = "combinations"

    def test_basic(self):
        result, expected = self.call("abc", 2)
        self.compare(result, expected)

    def test_big(self):
        result, expected = self.call(range(100), 3)
        self.compare(result, expected)

    # def test_bigger(self):
    #     result, expected = self.call(range(100000000), 2)
    #     self.compare(result, expected, 100)


class TestPermutations(BaseTest):
    f = "permutations"

    def test_basic(self):
        result, expected = self.call("abc", 2)
        self.compare(result, expected)

    def test_big(self):
        result, expected = self.call(range(100), 3)
        self.compare(result, expected)

    # def test_bigger(self):
    #     result, expected = self.call(range(100000000))
    #     self.compare(result, expected, 100)


class TestProduct(BaseTest):
    f = "product"

    def test_basic(self):
        result, expected = self.call([1, 2], ["a", "b"])
        self.compare(result, expected)

    def test_multiple(self):
        result, expected = self.call(
            [1, 2], ["a", "b"], [True, False], [None, None, None]
        )
        self.compare(result, expected)

    def test_repeat(self):
        result, expected = self.call("ab", "cd", repeat=4)
        self.compare(result, expected)

    def test_big(self):
        result, expected = self.call(range(10000), range(1000))
        self.compare(result, expected)

    # def test_bigger(self):
    #     assert next(mitertools.product(range(1000000000)))
