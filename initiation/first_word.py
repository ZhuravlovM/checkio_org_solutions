"""
You are given a string, and you have to find its first word.
The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
"""


def first_word(text: str) -> str:
    list_of_strings = text.split()
    return list_of_strings[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done!")
