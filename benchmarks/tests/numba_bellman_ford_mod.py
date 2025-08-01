# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
""" Module containing functions for testing the Bellman-Ford algorithm using numba
"""

from numba import njit
import numpy as np


@njit(fastmath=True)
def bellman_ford ( v_num: int, e_num: int, source: int, e: 'int[:,:]', e_weight: 'float[:]',
                   v_weight: 'float[:]', predecessor: 'int[:]' ):
    """ Calculate the shortest paths from a source vertex to all other
    vertices in the weighted digraph
    """

    r8_big = 1.0E+14

    #  Step 1: initialize the graph.
    for i in range ( 0, v_num ):
        v_weight[i] = r8_big
    v_weight[source] = 0.0

    predecessor[:v_num] = -1

    #  Step 2: Relax edges repeatedly.
    for i in range ( 1, v_num ):
        for j in range ( e_num ):
            u = e[1, j]
            v = e[0, j]
            t = v_weight[u] + e_weight[j]
            if ( t < v_weight[v] ):
                v_weight[v] = t
                predecessor[v] = u

    #  Step 3: check for negative-weight cycles
    for j in range ( e_num ):
        u = e[1, j]
        v = e[0, j]
        if ( v_weight[u] + e_weight[j] < v_weight[v] ):
            print ( '' )
            print ( 'BELLMAN_FORD - Fatal error!' )
            print ( '  Graph contains a cycle with negative weight.' )
            return 1

    return 0


@njit(fastmath=True)

def bellman_ford_test():
    """ Test bellman ford's algorithm
    """

    e_num = 19900
    v_num = 200

    e = np.zeros((2, e_num), dtype = 'int')
    e_weight = np.zeros(e_num, dtype = 'float')
    idx = 0

    for i in  range(v_num):
        for j in range(v_num):
            if i > j:
                e[0, idx] = i
                e[1, idx] = j
                idx += 1

    for i in range(e_num):
        e_weight[i] = np.cos(i) * i

    source = 0
    v_weight = np.zeros(v_num, dtype = 'float')
    predecessor = np.zeros(v_num, dtype = 'int')

    bellman_ford(v_num, e_num, source, e, e_weight, v_weight, predecessor)

    return v_weight
