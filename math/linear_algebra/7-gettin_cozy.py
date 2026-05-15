#!/usr/bin/env python3
""" Addition of matrix along the axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """7-gettin_cozy.py"""
    if axis == 0:
        """Check if columns are same"""
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2

    elif axis == 1:
        """ check if rows of matrix are same"""
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    return None
