# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a non-linear convection equation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with pyccel or pythran
"""

from numpy import zeros

# pythran export nonlinearconv_1d(float[:], int, int, float, float)
def nonlinearconv_1d(u0: 'float[:]', nt: int, nx: int, dt: float, dx: float):
    """ Solve a non-linear convection equation
    """
    nx = u0.size
    u  = zeros(nx)
    un = zeros(nx)

    u[:] = u0
    for _ in range(nt):
        un[:] = u[:]
        for i in range(1, nx):
            u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

    return u
