#!/usr/bin/env python3
"""Module that calculates the determinant of a matrix."""


def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    Args:
        matrix (list of lists): Matrix whose determinant is calculated.

    Returns:
        int/float: Determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    """

    # Validate matrix type
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Special case for 0x0 matrix
    if matrix == [[]]:
        return 1

    rows = len(matrix)

    # Check square matrix
    if not all(len(row) == rows for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if rows == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if rows == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    # Recursive case for nxn matrix
    det = 0

    for col in range(rows):
        # Build minor matrix
        minor = []

        for row in range(1, rows):
            minor_row = (
                matrix[row][:col] +
                matrix[row][col + 1:]
            )
            minor.append(minor_row)

        # Cofactor expansion
        cofactor = ((-1) ** col) * matrix[0][col]
        det += cofactor * determinant(minor)

    return det
