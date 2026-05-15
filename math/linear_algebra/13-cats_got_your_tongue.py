#!/usr/bin/env python3
"""matrix addition axiswise using numbpy"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ Matrix concatination axiswise"""
    return np.concatenate((mat1, mat2), axis=axis)
