#!/usr/bin/env python3
"""Module that calculates the inverse of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return ((matrix[0][0] * matrix[1][1]) -
                (matrix[0][1] * matrix[1][0]))

    det = 0

    for col in range(len(matrix)):
        submatrix = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]

        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)

    return det


def minor(matrix):
    """Calculate the minor matrix of a matrix."""
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    if (matrix == [[]] or
            any(len(row) != len(matrix) for row in matrix)):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    minors = []

    for i in range(len(matrix)):
        row_minors = []

        for j in range(len(matrix)):
            submatrix = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix)
                if k != i
            ]

            row_minors.append(determinant(submatrix))

        minors.append(row_minors)

    return minors


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix."""
    minor_matrix = minor(matrix)

    cofactors = []

    for i in range(len(minor_matrix)):
        row = []

        for j in range(len(minor_matrix)):
            row.append(((-1) ** (i + j)) * minor_matrix[i][j])

        cofactors.append(row)

    return cofactors


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix."""
    cofactor_matrix = cofactor(matrix)

    adj_matrix = []

    for i in range(len(cofactor_matrix)):
        row = []

        for j in range(len(cofactor_matrix)):
            row.append(cofactor_matrix[j][i])

        adj_matrix.append(row)

    return adj_matrix


def inverse(matrix):
    """
    Calculate the inverse of a matrix.

    Returns None if matrix is singular.
    """
    det = determinant(matrix)

    if det == 0:
        return None

    adj_matrix = adjugate(matrix)

    inv_matrix = []

    for i in range(len(adj_matrix)):
        row = []

        for j in range(len(adj_matrix)):
            row.append(adj_matrix[i][j] / det)

        inv_matrix.append(row)

    return inv_matrix
