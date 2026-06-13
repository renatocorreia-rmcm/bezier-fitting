import numpy as np


def parameterize(data_points, micro=0):
    parameters = np.zeros(shape=len(data_points))

    for i in range(1, len(data_points)):
        parameters[i] = (
                parameters[i - 1] +  # t_{i-1}
                np.linalg.norm(data_points[i] - data_points[i - 1]) ** micro  # d_{i-1}
        )

    parameters /= parameters[-1]  # normalization

    return parameters
