"""Creating namedtuples at runtime"""
from collections import namedtuple

# with open("data.csv", "r") as f:
#     lines = f.readlines()
lines = [
    "name,age,gender,job",
    "alice,27,female,programmer",
    "bob,35,male,designer",
    "alex,21,other,devops",
]

# Extract the headers
header, *rows = lines
# Define record type
Record = namedtuple("Record", header.split(","))  # type: ignore
# Parse the records
records = [Record(*row.split(",")) for row in rows]

print(records[0].name)
print(records[1].job)
print(records[2].gender)

# Pros
# - Fields are not addressed by position but by column name -> adding and removing fields only
#   impacts the parts of the code where that field is used
# - More efficient than dictionaries
# - Fields can be added/removed without modifying the module where the CSV is loaded. Field presence
#   can be checked with hasattr()

# Cons
# - Doesn't work in the typed version (NamedTuple)
# - Requires the CSV to have headers
