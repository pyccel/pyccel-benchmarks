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
from numpy import ones

@njit(fastmath=True)
def linearconv_1d():
    """ Solve the linear convection equation
    """

    #Input
    nx=2001
    nt=2000
    c=1.
    dt=0.0003
    dx = 2 / (nx-1)
    u0 = ones(nx)
    u0[int(.5 / dx):int(1 / dx + 1)] = 2

    u  = zeros(nx)
    un = zeros(nx)

    u[:] = u0
    cp = c * dt / dx

    for _ in range(nt):
        un[:nx] = u[:nx]

        for i in range(1, nx):
            u[i] = un[i] - cp * (un[i] - un[i-1])

    return u
