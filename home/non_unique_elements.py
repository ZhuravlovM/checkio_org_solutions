"""
You are given a non-empty sequence of integers.
For this task, you should return Iterable consisting of only the non-unique elements from the initial sequence.
To do so you will need to remove all unique elements (elements which are contained in a given sequence only once).
When solving this task, do not change the order of the elements.
Example: in [1, 2, 3, 1, 3] elements 1, 3 are non-unique and result will be [1, 3, 1, 3].
"""

from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    non_unique_elements = [element for element in data if data.count(element) > 1]

    return non_unique_elements


print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

# These "asserts" are used for self-checking
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("The mission is done!")
