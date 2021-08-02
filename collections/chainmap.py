import time
from collections import ChainMap, UserDict


class VersionedDict(UserDict):
    data: ChainMap

    def __init__(self, dict_) -> None:
        # Initialize and redefine data as a ChainMap
        super().__init__(dict_)
        self.data = ChainMap(self.data)

        # Initialize versions
        self._versions = [(time.time(), self.data)]
        self._named_versions = {}

    def checkpoint(self, name=None):
        # If name is provided, create a named version
        if name:
            self._named_versions[name] = self.data
        # Create a checkpoint at the current time
        self._versions.append((time.time(), self.data))

        # Add a new layer
        self.data = self.data.new_child()

    def rollback(self, timestamp=None, version=None):
        assert bool(version) ^ bool(timestamp), "Only one argument can be specified"

        if version:
            self.data = self._named_versions[version].new_child()
        else:
            # Search for the i such that the timestamp is older that version i but newer than i+1
            i = 0
            while self._versions[i][0] < timestamp and i < len(self._versions):
                i += 1

            # Rollback
            self.data = self._versions[i][1].new_child()


print("### Named versions ###")

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

icecream.rollback(version="tuesday")
print(f"Rolled back: {dict(icecream)}")

###

print("### Rolling back to a point in time ###")
icecream["amount"] = 0
for _ in range(10):
    time.sleep(0.1)
    icecream["amount"] += 1
    icecream.checkpoint()


print("Amount: ", icecream["amount"])
icecream.rollback(time.time() - 0.51)  # Half a second ago
print("Amount: ", icecream["amount"])
