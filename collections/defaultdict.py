from collections import defaultdict


def new_id():
    last_id = -1

    def f():
        nonlocal last_id
        last_id += 1
        return last_id

    return f


unique_id = defaultdict(new_id())

print(unique_id["alice"])
print(unique_id["bob"])
print(unique_id["alice"])
