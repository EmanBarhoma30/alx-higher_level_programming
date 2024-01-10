#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix (list of lists): 2-dimensional array.

    Returns:
        list of lists: New matrix with each value being the square of the input value.
    """
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row to store squared values for the current row
        squared_row = []

        # Iterate through each element in the current row and compute the square
        for element in row:
            squared_row.append(element ** 2)

        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix
