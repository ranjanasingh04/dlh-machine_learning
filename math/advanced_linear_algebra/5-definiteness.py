#!/usr/bin/env python3
"""Module that calculates the definiteness of a matrix."""

import numpy as np


def definiteness(matrix):
    """
    Calculate the definiteness of a matrix.

    Returns:
        - Positive definite
        - Positive semi-definite
        - Negative definite
        - Negative semi-definite
        - Indefinite
        - None
    """

    # Check if matrix is numpy.ndarray
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Check if matrix is valid
    if (matrix.ndim != 2 or
            matrix.shape[0] == 0 or
            matrix.shape[0] != matrix.shape[1]):
        return None

    # Matrix must be Hermitian / symmetric
    if not np.allclose(matrix, matrix.T):
        return None

    # Compute eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)

    # Positive definite
    if np.all(eigenvalues > 0):
        return "Positive definite"

    # Positive semi-definite
    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"

    # Negative definite
    if np.all(eigenvalues < 0):
        return "Negative definite"

    # Negative semi-definite
    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"

    # Indefinite
    if (np.any(eigenvalues > 0) and
            np.any(eigenvalues < 0)):
        return "Indefinite"

    return None
