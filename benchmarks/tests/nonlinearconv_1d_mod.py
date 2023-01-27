# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a non-linear convection equation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with pyccel or pythran
"""

from numpy import ones
from numpy import zeros

# pythran export nonlinearconv_1d()
def nonlinearconv_1d():
    """ Solve a non-linear convection equation
    """

    #Input
    nx = 2001
    nt = 2000
    dt = 0.00035
    dx = 2 / (nx-1)
    u0 = ones(nx)
    u0[int(.5 / dx):int(1 / dx + 1)] = 2

    u  = zeros(nx)
    un = zeros(nx)

    u[:] = u0
    for _ in range(nt):
        un[:] = u[:]
        for i in range(1, nx):
            u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

    return u
