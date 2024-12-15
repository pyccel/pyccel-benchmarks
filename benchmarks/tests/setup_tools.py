import random
import numpy as np

def setup_sparse_dijkstra():
    random.seed(1337)
    MAX_NEIGHBORS = 100
    NODES = 100_000
    MAX_DIST = 1_000_000

    a = []
    for i in range(NODES):
        neighs = random.randint(1, MAX_NEIGHBORS)
        adj = [random.randint(0, NODES - 1) % NODES if i % 2 == 0 else random.randint(1, MAX_DIST) for i in range(2 * neighs)]
        adj.extend([-1 for i in range(2 * (MAX_NEIGHBORS - neighs))])
        a.append(adj)

    aa = np.array(a, dtype=np.int64)

    return aa, 0, NODES, MAX_NEIGHBORS
