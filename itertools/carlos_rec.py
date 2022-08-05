def product(elements, repeat):
    product_result = []
    if repeat == 1:
        return [[element] for element in elements]
    for element in elements:
        inner_call = product(elements, repeat-1)
        for r in inner_call:
            result = [element] + r
            product_result.append(result)
    return product_result


def permutations(elements, repeat):
    permutations_result = []
    if repeat == 1:
        return [[element] for element in elements]
    for i, element in enumerate(elements):
        inner_result = permutations(elements[:i] + elements[i+1:], repeat-1)
        for r in inner_result:
            result = [element] + r
            permutations_result.append(result)
    return permutations_result


def combinations(elements, repeat):
    combinations_results = []
    if repeat == 1:
        return [[element] for element in elements]
    for i, element in enumerate(elements):
        inner_call = combinations(elements[i+1:], repeat-1)
        for r in inner_call:
            result = [element] + r
            combinations_results.append(result)
    return combinations_results


