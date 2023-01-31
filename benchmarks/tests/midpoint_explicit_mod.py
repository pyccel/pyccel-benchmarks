# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for solving an ordinary differential equation using the explicit midpoint method. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with pyccel or pythran
"""
import numpy as np

# ================================================================
def midpoint_explicit(dydt: '()(real, const real[:], real[:])',
                      tspan: 'real[:]', y0: 'real[:]', n: int,
                      t: 'real[:]', y: 'real[:,:]'):
    """
    Function implementing the explicit midpoint method
    """

    m = len(y0)
    ym = np.zeros(m)

    dt = (tspan[1] - tspan[0]) / float(n)

    t[0] = tspan[0]
    y[0,:] = y0[:]

    for i in range(n):

        dydt(t[i], y[i,:], ym[:])
        tm    = t[i]   + 0.5 * dt
        ym[:] = y[i,:] + 0.5 * dt * ym[:]

        dydt(tm, ym[:], y[i+1,:])
        t[i+1]   = t[i]   + dt
        y[i+1,:] = y[i,:] + dt * y[i+1,:]

# ================================================================
def humps_fun(x: float):
    """
    Humps function
    """

    y = 1.0 / ( ( x - 0.3 )**2 + 0.01 ) \
            + 1.0 / ( ( x - 0.9 )**2 + 0.04 ) \
            - 6.0

    return y

# ================================================================
def humps_deriv(x: 'real', y: 'real[:]', out: 'real[:]'):
    """
    Derivative of the humps function
    """

    out[0] = - 2.0 * ( x - 0.3 ) / ( ( x - 0.3 )**2 + 0.01 )**2 - 2.0 * ( x - 0.9 ) / ( ( x - 0.9 )**2 + 0.04 )**2

# ===============================================================
# pythran export midpoint_explicit_humps_test(float, float, int)
def midpoint_explicit_humps_test(t0: float, t1: float, n: int):
    """
    Compute an approximate solution y_h(t) ~= y(t) of the initial
    value problem

      dy/dt = f(t)
      y(t0) = y0

    over the interval [t0, t1].

    For test purposes we use the method of manufactured solutions,
    i.e. we choose the humps function y(t) as the exact solution
    and we compute f(t) := dy/dt, which is then passed to the ODE
    integrator. Finally the numerical solution y_h(t) is compared to
    the exact solution y(t) at the final time t1.

    Numerical integration is performed with n uniform steps of the
    explicit midpoint method.

    Parameters
    ----------
    t0 : float
        Initial time.

    t1 : float
        Final time.

    n : int
        Number of uniform time steps.

    Returns
    -------
    err : float
        Difference between numerical and exact solution at the
        final time t=t1.

    """

    # Time interval and initial conditions
    tspan = np.array([t0, t1])
    y0 = np.array([humps_fun(t0)])

    # Uniform time array where solution should be computed
    t = np.linspace(t0, t1, n + 1)

    # Empty array which will contain numerical solution
    yh = np.zeros((n + 1, 1))

    # Time integration
    midpoint_explicit(humps_deriv, tspan, y0, n, t, yh)

    # Error at final time
    err = yh[-1, 0] - humps_fun(t1)

    return err
