#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = float('-inf')  # Start with negative infinity as the initial maximum value
    max_key = None
      for key, value in a_dictionary.items():
        # Update max_value and max_key if a greater value is found
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
