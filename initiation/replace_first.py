"""
In a given sequence the first element should become the last one.
An empty sequence or with only one element should stay the same.
"""

from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        items.append(items.pop(0))
    return items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done!")
