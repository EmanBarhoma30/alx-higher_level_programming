#!/usr/bin/python3
def remove_char_at(s, n):
    return s[:n] + s[n+1:] if n >= 0 else s
