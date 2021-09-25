import itertools
from memory_profiler import memory_usage


def combinations(iterable, length=2):
    """combinations('ABCD', 2) --> AB AC AD BC BD CD"""
    elements = list(iterable)
    indices = list(reversed(range(len(elements))))

    stack = [[i] for i in indices]
    while stack:
        current = stack.pop()
        if len(current) == length:
            yield tuple(elements[i] for i in current)
        else:
            stack.extend(
                current + [i] for i in indices if i not in current and i > current[-1]
            )


# def combinations2(iterable, length=2):
#     class Combinations:
#         def __init__(self) -> None:
#             self.elements = []
#             self.indices = list(range(length))
#             self.iterator = iter(iterable)

#         def __iter__(self):
#             return self

#         def __next__(self):
#             res = tuple(self._get(i) for i in self.indices)
#             self._increment_indices()
#             return res

#         def _get(self, index):
#             while len(self.elements) - 1 < index:
#                 try:
#                     self.elements.append(next(self.iterator))
#                 except StopIteration:
#                     raise IndexError
#             return self.elements[index]

#         def _index_within_bounds(self, index):
#             try:
#                 self._get(index)
#                 return True
#             except:
#                 return False

#         def _increment_indices(self, i=length - 1):
#             new_index = self.indices[i] + 1
#             while new_index in self.indices[:i]:
#                 new_index += 1
#             if self._index_within_bounds(new_index):
#                 self.indices[i] = new_index
#             elif i == 0:
#                 n
#             else:
#                 self._increment_indices(i - 1)
#                 self.indices[i] = max(self.indices[:i]) + 1

#     return Combinations()


def permutations(iterable, length=2):
    """permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC"""
    elements = list(iterable)
    indices = list(reversed(range(len(elements))))

    stack = [[i] for i in indices]
    while stack:
        current = stack.pop()
        if len(current) == length:
            yield tuple(elements[i] for i in current)
        else:
            stack.extend(current + [i] for i in indices if i not in current)


def product(*iterables, repeat=1):
    """product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD"""
    iterables = list(iterables) * repeat
    iterables.reverse()
    used = [iterables[-1]]
    stack = [iter(iterables.pop())]
    result = []

    while stack:
        try:
            result.append(next(stack[-1]))
        except:
            iterables.append(used.pop())
            stack.pop()
            if stack:
                result.pop()
            continue

        # Base case
        if not iterables:
            yield tuple(result)
            result.pop()
        # General case
        else:
            used.append(iterables[-1])
            stack.append(iter(iterables.pop()))


if __name__ == "__main__":
    print(list(itertools.combinations("abcd", 3)))
    for c in combinations2("abcd", 3):
        print(c, end=", ")

    # def f():
    #     list(combinations(range(10), 3))

    # def g():
    #     list(combinations2(range(10), 3))

    # mem_usage = memory_usage(f)
    # print("Memory usage (in chunks of .1 seconds): %s" % mem_usage)
    # print("Maximum memory usage: %s" % max(mem_usage))
    # mem_usage = memory_usage(g)
    # print("Memory usage (in chunks of .1 seconds): %s" % mem_usage)
    # print("Maximum memory usage: %s" % max(mem_usage))
