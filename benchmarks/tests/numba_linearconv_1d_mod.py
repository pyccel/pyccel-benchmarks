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
import numpy as np


@njit
def linearconv_1d(nx: int, dt: float, nt: int):
    """
    Compute an approximation of the solution u(t, x) to the 1D
    linear advection equation

        du/dt + du/dx = 0

    on the domain [0, 2], with discontinuous initial conditions

        u(t=0, x) = 2   for 0.5 < x < 1,
        u(t=0, x) = 1   otherwise.

    The numerical solution is computed on a uniform grid using
    the 1st-order Godunov method, i.e. explicit Euler time stepping
    combined with upwind fluxes.

    Parameters
    ----------
    nx : int
        Number of grid points in the domain.

    dt : float
        Time step size.

    nt : int
        Number of time steps to be taken.

    Returns
    -------
    x : numpy.ndarray of nx floats
        Spatial grid where solution is computed.

    u : numpy.ndarray of nx floats
        Numerical solution u at final time.

    """

    c  = 1.0
    dx = 2 / (nx-1)
    x  = np.linspace(0, 2, nx)
    u  = np.ones(nx)
    u[int(.5 / dx):int(1 / dx + 1)] = 2

    cp = c * dt / dx
    un = np.zeros(nx)

    for _ in range(nt):
        un[:] = u[:]
        for i in range(1, nx):
            u[i] = un[i] - cp * (un[i] - un[i-1])

    return x, u
