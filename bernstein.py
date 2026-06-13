from math import comb

import numpy as np


def bernstein_basis(n, j, t):
    return comb(n, j) * (t ** j) * ((1 - t) ** (n - j))


def get_coefficients_matrix(parameters, n, d):
    return np.array(
        [[bernstein_basis(d-1, j, parameters[i]) for j in range(d)] for i in range(n)]
    )