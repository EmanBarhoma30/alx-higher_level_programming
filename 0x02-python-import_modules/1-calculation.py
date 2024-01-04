#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div as calculator_function

    a = 10
    b = 5

    result_add = calculator_function(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = calculator_function(a, b)

    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")
