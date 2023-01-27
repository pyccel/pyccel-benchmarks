# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a Laplace equation. The code is adapted from examples written by
[J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html).
To be accelerated with pyccel or pythran
"""
import numpy as np

# pythran export laplace_2d()
def laplace_2d():
    """ Solve the Laplace equation
    """

    #Input
    nx = 128
    ny = 128
    c = 1.
    l1norm_target = 1.e-4
    dx = 2 / (nx - 1); dy = 2 / (ny - 1)
    p = np.zeros((ny, nx))
    y = np.linspace(0, 1, ny)
    pn = np.empty((ny, nx))

    # Set first guess to one
    #p[:, :] = 1.0

    l1norm = 1.
    niter = 0

    a = np.zeros((ny, nx))
    err = np.zeros((ny, nx))
    diff = np.zeros((ny, nx))
    while l1norm > l1norm_target:
        pn[:, :] = p[:, :]

        p[1:-1, 1:-1] = (dy**2 * (pn[1:-1, 2:] + pn[1:-1, 0:-2]) +
                         dx**2 * (pn[2:, 1:-1] + pn[0:-2, 1:-1])) / (2 * (dx**2 + dy**2))

        p[ :, 0] = 0         #     p = 0 @ x = 0
        p[ :,-1] = y         #     p = y @ x = 2
        p[ 0, :] = p[ 1, :]  # dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1

        diff[:] = p[:] - pn[:]
        a[:] = np.abs(pn[:])
        err[:] = np.abs(diff[:])
        l1norm = np.sum(err) / np.sum(a)
        niter += 1

    return niter
