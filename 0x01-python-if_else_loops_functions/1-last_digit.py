#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit *= -1 if number < 0 else 1  
#Correcting the sign for negative numbers

output_string = "Last digit of {:d} is {:d} and is".format(number, last_digit)

if last_digit > 5:
    output_string += " greater than 5"
elif last_digit == 0:
    output_string += " 0"
else:
    output_string += " less than 6 and not 0"

print(output_string)
