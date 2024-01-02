#!/usr/bin/python3

print(', '.join(['{}{}'.format(x, y) if not (x == 8 and y == 9) else '89' for x in range(0, 10) for y in range(x + 1, 10)]))
