#!/usr/bin/python3

start_char = ord('a')
end_char = ord('z')

for i in range(start_char, end_char + 1):
    current_char = chr(i)
    if current_char not in ['e', 'q']:
        print(current_char, end='')
