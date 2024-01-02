#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    diff = 0 if i % 2 == 0 else 32
    print("{:c}".format(i - diff), end='')
