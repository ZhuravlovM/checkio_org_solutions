# You should return a given string in reverse order.


def backward_string(val: str) -> str:
    return val[::-1]


print("Example:")
print(backward_string("Please, reverse"))

# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("Ohio") == "Ohio"
assert backward_string("123456789") == "987654321"

print("The mission is done!")
