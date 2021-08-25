import random
from collections import OrderedDict


class Wishes(OrderedDict):
    def __getitem__(self, k):
        if k in self:
            return super().__getitem__(k)
        else:
            self[k] = set()
            return self[k]

    def grant(self):
        person, wishes = self.popitem(last=False)
        print(f"Granting {person}'s wishes:")
        for wish in wishes:
            print(f"  -Granted {wish}")


things = ["ice cream", "a horse", "gold", "love", "Python skills"]
people = ["Alice", "Bob", "Carlos", "Daniel"]

wishes = Wishes()

for _ in range(10):
    person = random.sample(people, 1)[0]
    wish = random.sample(things, 1)[0]

    print(f"{person} wishes {wish.upper()}")
    wishes[person].add(wish)

    if random.random() < 0.5:
        wishes.grant()

print()
print("== Granting everything! ==")
while wishes:
    wishes.grant()
