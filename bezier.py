import numpy as np

from bernstein import get_coefficients_matrix


def interpolate(cps, t):
    if len(cps) == 1:
        return cps[0]

    return (1 - t) * interpolate(cps[:-1], t) + t * interpolate(cps[1:], t)


def fit(data_points, parameters, d):
    """
    fit a `d` degree Bézier curve to a sequence of Data Points

    :return: control points, error
    """

    n = len(data_points)  # amount of data points

    # setup coefficients matrix A
    A = get_coefficients_matrix(parameters, n, d)

    if n == d:  # Determined: c = U⁻¹L⁻¹d
        control_points = np.linalg.solve(A, data_points)
        return control_points, np.linalg.norm((A@control_points)-data_points, axis=0)/n

    elif n > d:  # OverDetermined: Solve c = (AᵀA)⁻¹Aᵀd
        control_points = np.linalg.solve(A.T @ A, A.T @ data_points)
        return control_points, np.linalg.norm((A@control_points)-data_points, axis=0)/n

    elif n < d:  # UnderDetermined: Solve x = A⁺d
        control_points = np.linalg.pinv(A)@data_points
        return control_points, np.linalg.norm((A@control_points)-data_points, axis=0)/n


    return None
