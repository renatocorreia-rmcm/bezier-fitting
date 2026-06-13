from matplotlib import pyplot as plt


def matrix_show(A):
    # label each cell
    for i, line in enumerate(A):
        for j, cell in enumerate(line):
            plt.text(
                j, i, round(cell, 3),
                ha="center", va="center", color=('w' if cell <= 0.5 else 'k')
            )

    plt.xticks([])
    plt.yticks([])
    plt.title("")
    plt.imshow(A, cmap="cubehelix")


def experiment_show(data_points, raw_bezier, fitted_bezier):
    r_color = 'orange'  # raw curve color
    f_color = 'aqua'  # fitted curve color

    plt.gca().set_facecolor('k')

    # DATA POINTS
    plt.scatter(data_points[:, 0], data_points[:, 1], label="Data Points", alpha=0.2, color=r_color)
    plt.plot(data_points[:, 0], data_points[:, 1], linestyle="--", alpha=0.1, color=r_color)
    # RAW BEZIER CURVE
    plt.plot(raw_bezier[:, 0], raw_bezier[:, 1], label="Raw Bezier Curve", color=r_color)

    # FITTED CONTROL POINTS - UNIFORM
    # plt.scatter(control_points[:,0],control_points[:,1], label="Control Points", alpha=0.2, color=f_color)
    # plt.plot(control_points[:,0],control_points[:,1], linestyle="--", alpha=0.1, color=f_color)

    # FITTED BEZIER CURVE - UNIFORM
    plt.plot(fitted_bezier[:, 0], fitted_bezier[:, 1], label="Fitted Bezier Curve - Uniform",
             color=f_color)

    # FITTED BEZIER CURVE - CHORDAL

    plt.legend()