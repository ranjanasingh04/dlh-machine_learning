#!/usr/bin/env python3
"""Adds two matrices"""


def add_matrices(mat1, mat2):
    """Returns a new matrix containing the sum"""

    if type(mat1) != list or type(mat2) != list:
        return mat1 + mat2

    if len(mat1) != len(mat2):
        return None

    result = []

    for row1, row2 in zip(mat1, mat2):

        added = add_matrices(row1, row2)

        if added is None:
            return None

        result.append(added)

    return result
