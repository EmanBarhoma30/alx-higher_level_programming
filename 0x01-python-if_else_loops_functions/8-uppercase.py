#!/usr/bin/python3

def uppercase(some_str):
    for char in some_str:
        # Check if the character is lowercase
        if 97 <= ord(char) <= 122:
            # Convert the lowercase character to uppercase using ASCII values
            upper_char = chr(ord(char) - 32)
            # Print the uppercase character without a newline
            print(upper_char, end="")
        else:
            # Print characters other than lowercase letters
            print(char, end="")
    
    # Print a newline after processing the string
    print()

# Example usage:
uppercase("best")
uppercase("Best School 98 Battery street")
