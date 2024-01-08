#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        reversed_list = list(reversed(my_list))
        for num in reversed_list:
            print("{:d}".format(num))
