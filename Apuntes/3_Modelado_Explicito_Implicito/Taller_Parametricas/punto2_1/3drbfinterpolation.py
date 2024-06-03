from typing import Callable

import matplotlib.pyplot as plt
import numpy as np

from RBFInterpolation import RBFInterp


def original_function(
        x: np.array,
        y: np.array
):
    return np.cos(x**2 + y**2)


def plot_surface(
        x: np.ndarray,
        y: np.ndarray,
        z: np.ndarray,
        title: str
):
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot_trisurf(
        x,
        y,
        z,
        linewidth=0.2,
        antialiased=True
    )
    ax.set_title(title)
    plt.show()


def generate_meshgrid(
        x_min: float,
        x_max: float,
        y_min: float,
        y_max: float,
        x_samples: float,
        y_samples: float,
        z_function: Callable[[np.ndarray, np.ndarray], np.ndarray]
):
    u = np.linspace(x_min, x_max, x_samples)
    v = np.linspace(y_min, y_max, y_samples)
    xk, yk = np.meshgrid(u, v)
    zk = z_function(xk, yk)
    return np.concatenate(
        [
            xk.reshape(-1, 1, 1),
            yk.reshape(-1, 1, 1),
            zk.reshape(-1, 1, 1)
        ],
        axis=2
    )


def main():
    base_grid = generate_meshgrid(-3, 3, -2, 2, 10, 10, original_function)
    inter_grid = generate_meshgrid(-3, 3, -2, 2, 20, 20, original_function)
    plot_surface(
        base_grid[:, :, 0].flatten(),
        base_grid[:, :, 1].flatten(),
        base_grid[:, :, 2].flatten(),
        "base grid"
    )
    # Boolean to use a linear rbf of gaussian rbf
    interp = RBFInterp(False)
    interp.fit(base_grid[:, :, :2], base_grid[:, :, 2])
    y = interp(inter_grid[:, :, :2])

    plot_surface(
        inter_grid[:, :, 0].flatten(),
        inter_grid[:, :, 1].flatten(),
        y.flatten(),
        "interpolated function surface"
    )

    plot_surface(
        inter_grid[:, :, 0].flatten(),
        inter_grid[:, :, 1].flatten(),
        inter_grid[:, :, 2].flatten(),
        "real function surface"
    )


if __name__ == '__main__':
    main()
