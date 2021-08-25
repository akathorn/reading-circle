import random
from collections import UserList


class RandomlyIteratedList(UserList):
    def __iter__(self):
        permutation = list(range(len(self)))
        random.shuffle(permutation)
        return (self[pos] for pos in permutation)


mylist = RandomlyIteratedList([42, "hola", None, True, (1, 2)])

print(mylist)
for item in mylist:
    print(item, end=" ")
print()

print(*mylist)

print()

s = set([1, 2, 3])
for element in RandomlyIteratedList(s):
    print(element, end=" ")
print()
