#!/usr/bin/python3
"""
    Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Rotate a matrix 90 degrees clockwise.
        Args:
            matrix: given matrix to rotate
        Return:
            rotated matrix
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
