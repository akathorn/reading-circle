def product(iterable, repeat=1):
    indexes = [0 for _ in range(repeat)]  # indexes = [0,0,0]
    # When all the indexes reach the max value stop
    while all(index < len(iterable) for index in indexes):
        # allways start for the last index
        i_to_increase = len(indexes) - 1
        # yield actual value
        yield tuple(iterable[i] for i in indexes)
        # in case we reach the maximum value to increase in an index, we set it
        # again to 0 and reduce the i_to_increase
        while i_to_increase > 0 and indexes[i_to_increase] == len(iterable) - 1:
            # set back to 0 the actual index
            indexes[i_to_increase] = 0
            # change to previous index
            i_to_increase -= 1
        indexes[i_to_increase] += 1

def product123123(iterable, repeat=1):
    indexes = [0 for _ in range(repeat)]
    # while all(index < len(iterable) for index in indexes):
    while indexes[0] < len(iterable):
        yield tuple(iterable[i] for i in indexes)

        i_to_increase = len(indexes) - 1
        while i_to_increase > 0 and indexes[i_to_increase] == len(iterable) - 1:
            indexes[i_to_increase] = 0
            i_to_increase -= 1
        indexes[i_to_increase] += 1


def combinations(iterable, repeat=1):
    indexes = list(range(repeat))  # indexes = [0,0,0]
    combinations = {}
    # When all the indexes reach the max value stop
    while all(index < len(iterable) for index in indexes):
        # allways start for the last index
        i_to_increase = len(indexes) - 1

        # check if actual value can be yield
        result = {}
        valid = True
        for index in indexes:
            if index in result:
                valid = False
                break
            else:
                result[index] = True
        if valid:
            result = tuple(iterable[i] for i in indexes)
            sorted_indexes = str(sorted(indexes))
            # has this combination already returned
            if sorted_indexes not in combinations:
                yield result
                combinations[sorted_indexes] = True

        # in case we reach the maximum value to increase in an index, we set it
        # again to 0 and reduce the i_to_increase
        while i_to_increase > 0 and indexes[i_to_increase] == len(iterable) - 1:
            # set back to 0 the actual index
            indexes[i_to_increase] = 0
            # change to previous index
            i_to_increase -= 1
        indexes[i_to_increase] += 1


def permutations(iterable, repeat=1):
    indexes = [0 for _ in range(repeat)]  # indexes = [0,0,0]
    # When all the indexes reach the max value stop
    while all(index < len(iterable) for index in indexes):
        # allways start for the last index
        i_to_increase = len(indexes) - 1
        # check if actual value can be yield
        result = {}
        valid = True
        for index in indexes:
            if index in result:
                valid = False
                break
            else:
                result[index] = True
        if valid:
            yield tuple(iterable[i] for i in indexes)
        # in case we reach the maximum value to increase in an index, we set it
        # again to 0 and reduce the i_to_increase
        while i_to_increase > 0 and indexes[i_to_increase] == len(iterable) - 1:
            # set back to 0 the actual index
            indexes[i_to_increase] = 0
            # change to previous index
            i_to_increase -= 1
        indexes[i_to_increase] += 1
