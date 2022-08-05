from copy import copy
import itertools

itertools.combinations


def combinations(iterable, length=2):
    """combinations('ABCD', 2) --> AB AC AD BC BD CD"""
    # return [(1, 2)]
    yield from _combinations_rec(iter(iterable), length, depth=0)


def _combinations_rec(iterator, length, depth):
    # Base case
    if depth == length:
        yield tuple()
        return

    # General case
    iterator = copy(iterator)
    for head in iterator:
        # Each iteration consumes the head
        # _combinations_rec doesn't consume the iterator
        for ret in _combinations_rec(iterator, length, depth + 1):
            yield (head,) + ret


def permutations(iterable, length=None):
    """combinations('ABCD', 2) --> AB AC AD BC BD CD"""
    yield from _permutations_rec(iter(iterable), length, depth=0)


def _permutations_rec(iterator, length, depth, skip=[]):
    # Base case
    if depth == length:
        yield tuple()
        return

    # General case
    heads = copy(iterator)
    for index, head in enumerate(heads):
        # We make sure we don't use the same element twice. If the current index is in skip, then we
        # skip it
        if index in skip:
            continue
        # We add the new index to the skip list. And, since we consumed the head, now the iterator
        # is shorter and we need to update the existing indices. For example, the element that was
        # previously in position 3 will now be in position 2 in the iterator.
        # new_skip = [i - 1 for i in skip] + [index]
        new_skip = skip + [index]

        for ret in _permutations_rec(copy(iterator), length, depth + 1, new_skip):
            yield (head,) + ret
    # yield tuple()


def product(*iterables, repeat=1):
    """product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD"""
    yield from _product_rec(*iterables * repeat)


# iterables = [range(3), "ab"]
# iterables * 3 = [range(3), "ab", range(3), "ab", range(3), "ab"]


def _product_rec(head, *rest):
    # Base case
    if not rest:
        yield from ((h,) for h in head)
        return

    # General case
    for h in head:
        for r in _product_rec(*rest):
            yield (h,) + r


if __name__ == "__main__":
    # print(list(itertools.product([1, 2], "ab", repeat=1)))
    # print(list(product([1, 2], "ab", repeat=1)))
    # print(list(itertools.product([1, 2], "ab", [True, False], repeat=1)))
    # print(list(product([1, 2], "ab", [True, False], repeat=1)))
    # print(list(itertools.product("ab", repeat=3)))
    # print(list(product("ab", repeat=3)))
    # print(list(itertools.product("ab", [1, 2], repeat=2)))
    # print(list(product("ab", [1, 2], repeat=2)))
    # print(next(product(range(100000000), range(1000000), repeat=100)))

    # import timeit

    # print(
    #     timeit.timeit(
    #         "list(itertools.product([1, 2], 'ab', [True, False], repeat=1))",
    #         number=10000000,
    #     )
    # )

    # print(list(itertools.combinations("abcd", 3)))
    # print(list(combinations("abcd", 3)))

    # print(list(permutations("abcd", 2)))
    # print(list(itertools.permutations("abcd", 3))[:5])
    # print(list(permutations("abcd", 3))[:5])
    print(next(permutations("abcd")))
