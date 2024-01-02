#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print("{}".format(uppercase_char), end="")
    print()

# Example usage:
uppercase("best")
uppercase("Best School 98 Battery street")
