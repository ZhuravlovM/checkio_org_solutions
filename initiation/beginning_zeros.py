"""
You have a string that consist only of digits.
You need to find how many zero digits ("0") are at the beginning of the given string.
"""


def beginning_zeros(a: str) -> int:
    return len(str(a)) - len(str(a).lstrip('0'))


print("Example:")
print(beginning_zeros("010"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done!")
