import numpy as np

class MinHeap:
    def __init__(self):
        self.distances: 'list[int]' = []
        self.nodes: 'list[int]' = []

    def _sift_up(self, index: int):
        parent = (index - 1) // 2
        if index > 0 and self.distances[index] < self.distances[parent]:
            tmp = self.distances[index]
            self.distances[index] = self.distances[parent]
            self.distances[parent] = tmp            
            tmp = self.nodes[index]
            self.nodes[index] = self.nodes[parent]
            self.nodes[parent] = tmp
            self._sift_up(parent)

    def _sift_down(self, index: int):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.distances) and self.distances[left] < self.distances[smallest]:
            smallest = left
        if right < len(self.distances) and self.distances[right] < self.distances[smallest]:
            smallest = right

        if smallest != index:
            tmp = self.distances[index]
            self.distances[index] = self.distances[smallest] 
            self.distances[smallest] = tmp 
            tmp = self.nodes[index]
            self.nodes[index] = self.nodes[smallest]
            self.nodes[smallest] = tmp
            self._sift_down(smallest)

    def push(self, item_distance: 'int', item_node: 'int'):
        self.distances.append(item_distance)
        self.nodes.append(item_node)
        self._sift_up(len(self.distances) - 1)

    def pop(self):
        if len(self.distances) == 1:
            return self.distances.pop(), self.nodes.pop()
        root_distance = self.distances[0]
        root_node = self.nodes[0]
        self.distances[0] = self.distances.pop()
        self.nodes[0] = self.nodes.pop()
        self._sift_down(0)
        return root_distance, root_node


    def length(self) -> int:
        return len(self.distances)

def dijkstra(graph: 'int[:,:]', start: int, num_nodes: int, max_neighbors: int) -> 'int[:]':
    """
    Implements Dijkstra's algorithm to find the shortest paths from a start node.

    Parameters:
    graph (numpy array): A 2D numpy array where each row represents a node and contains up to 5 neighbors as pairs (neighbor, weight). -1 indicates no neighbor.
    start (int): The starting node index.
    num_nodes (int): Total number of nodes in the graph.

    Returns:
    numpy array: Shortest distances from the start node to each node.
    """
    priority_queue = MinHeap()
    shortest_distances = np.full(num_nodes, int(1e9))  
    shortest_distances[start] = 0

    priority_queue.push(0, start)

    while priority_queue.length() > 0:
        current_distance, current_node = priority_queue.pop()

        if current_distance > shortest_distances[current_node]:
            continue

        for i in range(0, 2 * max_neighbors, 2):
            neighbor = graph[current_node, i]
            weight = graph[current_node, i + 1]
            if neighbor == -1 or current_node == neighbor:
                continue

            dist = current_distance + weight

            if dist < shortest_distances[neighbor]:
                shortest_distances[neighbor] = dist
                priority_queue.push(dist, neighbor)

    return shortest_distances

