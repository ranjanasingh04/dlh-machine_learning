#!/usr/bin/env python3
"""Module performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """ Matrix multiplication"""
    if len(mat1[0]) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):
        rows = []
        for j in range(len(mat2[0])):
            value = 0
            for k in range(len(mat2)):
                value += mat1[i][k] * mat2[k][j]
            rows.append(value)
        result.append(rows)
    return result
