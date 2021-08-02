from collections import ChainMap, UserDict


class VersionedDict(UserDict):
    data: ChainMap

    def __init__(self, dict_) -> None:
        super().__init__(dict_)
        self.data = ChainMap(self.data)  # type: ignore
        self._versions = {}

    def checkpoint(self, name):
        self._versions[name] = self.data
        self.data = self.data.new_child()

    def rollback(self, version):
        self.data = self._versions[version].new_child()


####

icecream = VersionedDict({"weather": "good", "flavor": "vanilla", "amount": 3})
icecream.checkpoint("monday")
print(f"Monday:      {dict(icecream)}")

# Version 2
icecream["amount"] -= 2
icecream.checkpoint("tuesday")
print(f"Tuesday:     {dict(icecream)}")

# Version 3
icecream["weather"] = "bad"
icecream["cone"] = False  # new key
icecream.checkpoint("wednesday")
print(f"Wednesday:   {dict(icecream)}")

print()
print(icecream)
print()

icecream.rollback("tuesday")
print(f"Rolled back: {dict(icecream)}")
