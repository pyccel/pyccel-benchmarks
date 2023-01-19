# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a linear convection equation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with numba
"""

from numba import njit
from numpy import zeros

@njit(fastmath=True)
def linearconv_1d(u0: 'float[:]', nt: int,
                  dt: float, dx: float, c: float):
    """ Solve the linear convection equation
    """
    nx = u0.size
    u  = zeros(nx)
    un = zeros(nx)

    u[:] = u0
    cp = c * dt / dx

    for _ in range(nt):
        un[:nx] = u[:nx]

        for i in range(1, nx):
            u[i] = un[i] - cp * (un[i] - un[i-1])

    return u
