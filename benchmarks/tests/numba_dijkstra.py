# coding: utf-8
#------------------------------------------------------------------------------------------#
# This file is part of Pyccel which is released under MIT License. See the LICENSE file or #
# go to https://github.com/pyccel/pyccel/blob/master/LICENSE for full license details.     #
#------------------------------------------------------------------------------------------#
""" Module containing functions for testing the Dijkstra algorithm using numba
"""
from numba import njit
import numpy as np

# ================================================================
@njit(fastmath=True)
def find_nearest ( nv: int, mind: 'int[:]', connected: 'bool[:]' ):
    """ Find the nearest node
    """

    i4_huge = 2147483647

    d = i4_huge
    v = -1
    for i in range ( 0, nv ):
        if ( not connected[i] and mind[i] <= d ):
            d = mind[i]
            v = i

    return d, v

# ================================================================
@njit(fastmath=True)
def update_mind ( nv: int, mv: int, connected: 'bool[:]', ohd: 'int[:,:]', mind: 'int[:]' ):
    """ Update the minimum distance
    """

    i4_huge = 2147483647

    for i in range ( 0, nv ):
        if ( not connected[i] ):
            if ( ohd[mv,i] < i4_huge ):
                mind[i] = min ( mind[i], mind[mv] + ohd[mv,i] )

# ================================================================
@njit(fastmath=True)
def dijkstra_distance ( nv: int, ohd: 'int[:,:]', mind: 'int[:]' ):
    """ Find the shortest paths between nodes in a graph
    """

    #  Start out with only node 1 connected to the tree.
    connected = np.zeros (nv, dtype = 'bool' )

    connected[0] = True
    for i in range ( 1, nv ):
        connected[i] = False

    #  Initialize the minimum distance to the one-step distance.
    for i in range ( 1, nv ):
        mind[i] = ohd[0,i]

    #  Attach one more node on each iteration.

    for _ in range ( 1, nv ):
        #  Find the nearest unconnected node.
        _, mv = find_nearest ( nv, mind, connected )

        if ( mv == - 1 ):
            print ( 'DIJKSTRA_DISTANCE - Fatal error!' )
            print ( '  Search terminated early.' )
            print ( '  Graph might not be connected.' )
            # TODO exit
            #exit ( 'DIJKSTRA_DISTANCE - Fatal error!' )

        #  Mark this node as connected.
        connected[mv] = True

        #  Having determined the minimum distance to node MV, see if
        #  that reduces the minimum distance to other nodes.
        update_mind ( nv, mv, connected, ohd, mind )

# ================================================================
@njit(fastmath=True)
def init ( nv: int, ohd: 'int[:,:]' ):
    """ Create a graph
    """

    i4_huge = 1 << 20

    for i in range ( 0, nv ):
        for j in range ( 0, nv ):
            ohd[i,j] = i4_huge

        ohd[i,i] = 0

    ohd[0,333] = 33

# ================================================================
@njit(fastmath=True)
def dijkstra_distance_test ( ):
    """ Test Dijkstra's algorithm
    """

    #  Initialize the problem data.
    nv = 6
    ohd = np.zeros ( ( nv, nv ), dtype = 'int' )
    init ( nv, ohd )

    #  Carry out the algorithm.
    min_distance = np.zeros ( nv, dtype = 'int' )
    dijkstra_distance ( nv, ohd, min_distance )

    return min_distance
