#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        last_digit = number % -(10)
        abs_last_digit = -(last_digit)
    else:
        last_digit = number % 10
        abs_last_digit = last_digit

    print(abs_last_digit, end='')
    return abs_last_digit
