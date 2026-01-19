# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving a non-linear convection equation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with numba
"""


import jax.numpy as np



def nonlinearconv_1d(nx: int, dt: float, nt: int):
    """
    Compute an approximation of the solution u(t, x) to the 1D
    Burgers' equation

        du/dt + u du/dx = 0

    on the domain [0, 2], with initial conditions consisting of
    a Gaussian perturbation over a uniform background:

        u(t=0, x) = 1 + 0.5 exp( -((x-0.5)^2 / 0.15^2) ).

    The numerical solution is computed on a uniform grid using
    one-sided upwind finite-differences combined with explicit
    Euler time stepping.

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
    x : jax.numpy.ndarray of nx floats
        Spatial grid where solution is computed.

    u : jax.numpy.ndarray of nx floats
        Numerical solution u at final time.

    """

    dx = 2 / (nx-1)
    x  = np.linspace(0, 2, nx)
    u  = 1.0 + 0.5 * np.exp(-((x - 0.5)/0.15)**2)

    dt_dx = dt / dx
    un = np.zeros(nx)

    for _ in range(nt):
        un[:] = u[:]
        for i in range(1, nx):
            u[i] = un[i] - un[i] * dt_dx * (un[i] - un[i-1])

    return x, u
