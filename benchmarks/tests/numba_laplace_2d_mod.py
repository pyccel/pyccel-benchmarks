# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a Laplace equation. The code is adapted from examples written by
[J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html).
To be accelerated with numba
"""
from numba import njit
import numpy as np

@njit
def laplace_2d(nx: int, ny: int, rtol: float, maxiter: int):
    """
    Solve the 2D Laplace equation for phi(x, y) on the rectangular
    domain [0, 2] * [0, 1] with boundary conditions

        phi = 0      at x = xmin,
        phi = y      at x = xmax,
        dphi/dy = 0  at y = ymin,
        dphi/dy = 0  at y = ymax.

    The numerical solution is computed on a uniform grid using 2nd
    order finite differences and the Jacobi method with a prescribed
    relative tolerance.

    Parameters
    ----------
    nx : int
        Number of grid points along x axis.

    ny : int
        Number of grid points along y axis.

    rtol : float
        Stopping condition for the Jacobi method: the relative L1 norm
        of the difference between successive solutions should be lower
        than the value provided.

    maxiter : int
        Maximum number of Jacobi iterations allowed.

    Returns
    -------
    x : numpy.ndarray[nx]
        Computational grid along x axis.

    y : numpy.ndarray[ny]
        Computational grid along y axis.

    phi : numpy.ndarray[ny, nx]
        Numerical solution on the computational grid.

    niter : int
        Number of Jacobi iterations performed.
    """

    # Domain size
    xmin, xmax = 0., 2.
    ymin, ymax = 0., 1.

    # Computational grid
    dx = (xmax - xmin) / (nx - 1)
    dy = (ymax - ymin) / (ny - 1)
    x  = np.linspace(xmin, xmax, nx)
    y  = np.linspace(ymin, ymax, ny)

    # Initial values
    phi = np.ones((ny, nx))
    l1norm = 2 * rtol
    niter = 0

    # Temporary arrays
    pn   = np.empty((ny, nx))
    diff = np.empty((ny, nx))
    a    = np.empty((ny, nx))
    err  = np.empty((ny, nx))

    # Jacobi iteration
    while l1norm > rtol and niter < maxiter:
        pn[:, :] = phi[:, :]

        phi[1:-1, 1:-1] = ((dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) +
                            dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) /
                            (2 * (dx**2 + dy**2)))

        phi[ :, 0] = 0           #     phi = 0 @ x = 0
        phi[ :,-1] = y           #     phi = y @ x = 2
        phi[ 0, :] = phi[ 1, :]  # dphi/dy = 0 @ y = 0
        phi[-1, :] = phi[-2, :]  # dphi/dy = 0 @ y = 1

        diff[:] = phi[:] - pn[:]
        err[:] = np.abs(diff[:])
        a[:] = np.abs(pn[:])
        l1norm = np.sum(err) / np.sum(a)
        niter += 1

    # Return axes' grid, solution, and number of iterations
    return x, y, phi, niter
