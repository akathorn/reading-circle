import random
from enum import Enum
from collections import Counter


class Error(Enum):
    NOT_FOUND = 1
    WRONG_CREDENTIALS = 2
    TIMEOUT = 3
    SANDWICH = 4
    UNKNOWN = 5


all_errors = Counter()
api_errors = Counter()
internal_errors = Counter()
user_errors = [Counter() for _ in range(5)]

while random.random() > 0.05:
    error = Error(random.randint(1, 5))
    api_errors[error] += 1
    all_errors[error] += 1

while random.random() > 0.05:
    error = Error(random.randint(1, 5))
    internal_errors[error] += 1
    all_errors[error] += 1

while random.random() > 0.05:
    error = Error(random.randint(1, 5))
    user = random.randint(0, 4)
    user_errors[user][error] += 1
    all_errors[error] += 1


all_user_errors = sum(user_errors, start=Counter())

print("Total sandwiches:        ", all_errors[Error.SANDWICH])
print("Non-user sandwiches:     ", (all_errors - all_user_errors)[Error.SANDWICH])
print("User sandwiches:         ", all_user_errors[Error.SANDWICH])
print("User 1 sandwiches:       ", user_errors[1][Error.SANDWICH])
print("User sandwiches except 1:", (all_user_errors - user_errors[1])[Error.SANDWICH])

print("Most common error:", all_errors.most_common(1))
