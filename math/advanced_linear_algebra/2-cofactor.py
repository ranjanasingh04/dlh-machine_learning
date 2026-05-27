#!/usr/bin/env python3
"""Module that calculates the cofactor matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix."""

    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return ((matrix[0][0] * matrix[1][1]) -
                (matrix[0][1] * matrix[1][0]))

    det = 0

    for col in range(len(matrix)):
        # Build submatrix
        submatrix = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]

        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)

    return det


def minor(matrix):
    """Calculate the minor matrix of a matrix."""

    # Validate matrix type
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    # Validate square non-empty matrix
    if (matrix == [[]] or
            any(len(row) != len(matrix) for row in matrix)):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case for 1x1 matrix
    if len(matrix) == 1:
        return [[1]]

    minors = []

    for i in range(len(matrix)):
        row_minors = []

        for j in range(len(matrix)):
            # Create submatrix excluding row i and column j
            submatrix = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix)
                if k != i
            ]

            row_minors.append(determinant(submatrix))

        minors.append(row_minors)

    return minors


def cofactor(matrix):
    """
    Calculate the cofactor matrix of a matrix.
    """

    # Get minor matrix
    minor_matrix = minor(matrix)

    cofactors = []

    for i in range(len(minor_matrix)):
        row = []

        for j in range(len(minor_matrix)):
            # Apply checkerboard sign pattern
            row.append(((-1) ** (i + j)) * minor_matrix[i][j])

        cofactors.append(row)

    return cofactors
