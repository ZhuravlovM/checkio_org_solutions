# You have a number, and you need to determine which digit in this number is the biggest.


def max_digit(value: int) -> int:
    value_string = str(value)
    max_value = max(map(int, value_string))
    return max_value


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done!")
