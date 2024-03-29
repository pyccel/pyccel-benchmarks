# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a Poisson equation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with numba
"""

from numba import njit
import numpy as np


@njit(fastmath=True)
def poisson_2d(nx: int, ny: int, nt: int):
    """
    Solve the 2D poisson equation for phi(x, y) on the rectangular
    domain [0, 2] * [0, 1] with 2 point sources (Dirac deltas) of
    charge +1 and -1 respectively, at the positions

        (x, y) = (0.5, 0.25) and
        (x, y) = (1.5, 0.75),

    and subject to the boundary conditions

        phi = 0      at x = xmin,
        phi = y      at x = xmax,
        dphi/dy = 0  at y = ymin,
        dphi/dy = 0  at y = ymax.

    The numerical solution is computed on a uniform grid using 2nd
    order finite differences and the Jacobi method with a fixed
    number of iterations.

    Parameters
    ----------
    nx : int
        Number of grid points along x axis.

    ny : int
        Number of grid points along y axis.

    nt : int
        Number of Jacobi iterations.

    Returns
    -------
    x : numpy.ndarray[nx]
        Computational grid along x axis.

    y : numpy.ndarray[ny]
        Computational grid along y axis.

    phi : numpy.ndarray[ny, nx]
        Numerical solution on the computational grid.

    """

    # Domain size
    xmin, xmax = 0., 2.
    ymin, ymax = 0., 1.

    # Computational grid
    dx  = (xmax - xmin) / (nx - 1)
    dy  = (ymax - ymin) / (ny - 1)
    x   = np.linspace(xmin, xmax, nx)
    y   = np.linspace(ymin, ymax, ny)

    # Charge density with point sources
    b = np.zeros((ny, nx))
    b[    ny // 4,     nx // 4] =  1. / (dx * dy)
    b[3 * ny // 4, 3 * nx // 4] = -1. / (dx * dy)

    # First guess
    phi = np.zeros((ny, nx))

    # Temporary array
    pn = np.empty((ny, nx))

    # Jacobi iteration
    for _ in range(nt):
        pn[:, :] = phi[:, :]

        for j in range(1, ny-1):
            for i in range(1, nx-1):
                phi[j, i] = (((pn[j, i+1] + pn[j, i-1]) * dy**2 +
                              (pn[j+1, i] + pn[j-1, i]) * dx**2 -
                                  b[j, i] * dx**2 * dy**2) /
                                  (2 * (dx**2 + dy**2)))

        phi[ :, 0] = 0           #     phi = 0 @ x = xmin
        phi[ :,-1] = y           #     phi = y @ x = xmax
        phi[ 0, :] = phi[ 1, :]  # dphi/dy = 0 @ y = ymin
        phi[-1, :] = phi[-2, :]  # dphi/dy = 0 @ y = ymax

    # Return axes' grid and solution
    return x, y, phi
