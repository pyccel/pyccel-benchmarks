# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a Poisson equation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with pyccel or pythran
"""
from numba import njit
import numpy as np

@njit(fastmath=True)
def poisson_2d(p: 'float[:,:]', b: 'float[:,:]', y: 'float[:]',
               nt: int, dx: float, dy: float):
    """ Solve the 2D poisson equation
    """

    ny, nx = p.shape
    pn = np.empty((ny, nx))

    # Point sources
    b[ny // 4, nx // 4]  = 100
    b[3 * ny // 4, 3 * nx // 4] = -100

    # Set first guess to zero
    p[:, :] = 0.0

    for _ in range(nt):
        pn[:, :] = p[:, :]

        for j in range(2, ny):
            for i in range(2, nx):
                p[j-1, i-1] = (((pn[j-1, i] + pn[j-1, i-2]) * dy**2 +
                                (pn[j, i-1] + pn[j-2, i-1]) * dx**2 -
                                b[j-1, i-1] * dx**2 * dy**2) /
                                (2 * (dx**2 + dy**2)))

        p[ :, 0] = 0         #     p = 0 @ x = 0
        p[ :,-1] = y         #     p = y @ x = 2
        p[ 0, :] = p[ 1, :]  # dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1
