import mitertools
import itertools
import operator

# Infinite iterators. Iterators for which next() is very slow.


if __name__ == "__main__":
    res = mitertools.combinations("abcd", 3)
    res2 = itertools.combinations("abcd", 3)
    print(list(res))
    print(list(res2))
    assert all([a == b for a, b in zip(res, res2)])

    res = mitertools.permutations("abc", 3)
    res2 = itertools.permutations("abc", 3)
    print(list(res))
    print(list(res2))
    assert all([a == b for a, b in zip(res, res2)])

    res = mitertools.product([1, 2], ["a", "b"], [True, False])
    res2 = itertools.product([1, 2], ["a", "b"], [True, False])
    print(list(res))
    print(list(res2))
    assert all([a == b for a, b in zip(res, res2)])
    res = mitertools.product([1, 2], ["a", "b"])
    res2 = itertools.product([1, 2], ["a", "b"])
    print(list(res))
    print(list(res2))
    assert all([a == b for a, b in zip(res, res2)])
    res = mitertools.product("ab", repeat=3)
    res2 = itertools.product("ab", repeat=3)
    print(list(res))
    print(list(res2))
    assert all([a == b for a, b in zip(res, res2)])
