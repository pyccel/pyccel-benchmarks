# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
"""
Functions for running a small molecular dynamics simulation. The code is adapted from examples written by [J. Burkardt](https://people.sc.fsu.edu/~jburkardt/py_src/py_src.html)
To be accelerated with numba
"""
from jax import jit
from numpy import zeros
from numpy import sqrt
from numpy import pi
from numpy import sin

# ================================================================
@jit
def compute_kinetic_energy(vel: 'double[:,:]', mass: float):
    """ Compute the kinetic energy associated with the current configuration.
    """
    d_num, p_num = vel.shape

    kinetic = 0.0
    for k in range(d_num):
        for j in range(p_num):
            kinetic = kinetic + vel[k, j] ** 2

    return 0.5 * mass * kinetic

# ================================================================
@jit
def compute(mass: float, pos: 'double[:,:]', vel: 'double[:,:]',
        force: 'double[:,:]'):
    """
    Calculate the potential energy and forces associated with the
    current configuration.

    """

    (d_num, p_num) = pos.shape
    rij = zeros(d_num)

    potential = 0.0
    force[:, :] = 0.0

    for i in range(p_num):
        #
        #  Compute the potential energy and forces.
        #
        for j in range(p_num):
            if i != j:
                #  Compute RIJ, the displacement vector.
                for k in range(d_num):
                    rij[k] = pos[k, i] - pos[k, j]

                #  Compute D and D2, a distance and a truncated distance.
                d = 0.0
                for k in range(d_num):
                    d = d + rij[k] ** 2

                d = sqrt(d)
                d2 = min(d, pi / 2.0)

                #  Attribute half of the total potential energy to particle J.
                potential = potential + 0.5 * sin(d2) * sin(d2)

                #  Add particle J's contribution to the force on particle I.
                for k in range(d_num):
                    force[k, i] = force[k, i] - rij[k] * sin(2.0 * d2) / d

    return potential

# ================================================================
@jit
def update(dt: float, mass: float, force: 'double[:,:]',
           pos: 'double[:,:]', vel: 'double[:,:]', acc: 'double[:,:]'):

    """ Update the position, velocity and acceleration of the particles
    """

    rmass = 1.0 / mass
    #
    #  Update positions.
    #
    pos += vel * dt + 0.5 * acc * dt * dt
    #
    #  Update velocities.
    #
    vel += 0.5 * dt * ( force * rmass + acc )
    #
    #  Update accelerations.
    #
    acc[:] = force * rmass

# ================================================================
@jit
def r8mat_uniform_ab(r: 'double[:, :]', a: float, b: float, seed: int):
    """ Fill r with random numbers with a uniform distribution
    """

    (m, n) = r.shape
    i4_huge = 2147483647

    if seed <= 0:
        seed += i4_huge

    elif seed > 0:

        for j in range(n):
            for i in range(m):

                k = seed // 127773
                seed = 16807 * (seed - k * 127773) - k * 2836
                seed = seed % i4_huge

                if seed <= 0:
                    seed += i4_huge

                r[i, j] = a + (b - a) * seed * 4.656612875E-10

    return seed

# ================================================================
@jit
def initialize(pos: 'double[:,:]'):
    """ Initialise the positions of the particles
    """
    #  Positions.
    seed = 123456789
    seed = r8mat_uniform_ab(pos, 0.0, 10.0, seed)

# ================================================================
@jit
def md(d_num: int, p_num: int, step_num: int, dt: float):
    """
    Run a molecular dynamics simulation. This consists of an N-body
    problem in 3D, where N identical particles of unit mass
    interact through a given potential and accelerate according
    to Newton's 2nd law of motion.

    Parameters
    ----------
    d_num : int
        Number of dimensions, i.e. number of components of
        position and velocity vectors.

    p_num : int
        Number of particles.

    dt : float
        Time step size.

    step_num : int
        Number of time steps to be taken.

    Returns
    -------
    potential : float
        Total potential energy of the system.

    kinetic : float
        Total kinetic energy of the system.

    """

    # Set particles' mass
    mass = 1.0

    # Allocate work arrays
    pos   = zeros((d_num, p_num))  # positions
    vel   = zeros((d_num, p_num))  # velocities
    acc   = zeros((d_num, p_num))  # accelerations
    force = zeros((d_num, p_num))  # forces

    # Initialization
    initialize(pos)
    potential = compute(mass, pos, vel, force)

    # Time stepping
    for _ in range(step_num):
        update(dt, mass, force, pos, vel, acc)
        potential = compute(mass, pos, vel, force)

    # Compute total kinetic energy at final time
    kinetic = compute_kinetic_energy(vel, mass)

    # Return total potential and kinetic energies
    return potential, kinetic
