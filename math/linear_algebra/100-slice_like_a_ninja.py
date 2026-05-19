#!/usr/bin/env python3
"""#!/usr/bin/env python3"""


import numpy as np


def np_slice(matrix, axes={}):
    """Returns a sliced matrix"""
    slices = [slice(None)] * matrix.ndim

    for axis, values in axes.items():
        slices[axis] = slice(*values)

    return matrix[tuple(slices)]
