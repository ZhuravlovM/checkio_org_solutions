"""
You are given list of integers (int).
You should find the sum of the elements with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the list together.
Don't forget that the first element has an index of 0.
For an empty list, the result will always be 0 (zero).
"""


def checkio(array: list[int]) -> int:
    if not array:
        return 0
    sum_even_indexes = sum(array[::2])
    result = sum_even_indexes * array[-1]
    return result


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
