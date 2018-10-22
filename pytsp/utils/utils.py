import numpy as np

from random import randint


def minimal_spanning_tree(graph, mode='Prim', starting_node=None):
    """

    Args:
        graph:  weighted adjacency matrix as 2d np.array
        mode: method for calculating minimal spanning tree
        starting_node: node number to start construction of minimal spanning tree (Prim)
    Returns:
        minimal spanning tree as 2d array
    """

    if mode == 'Prim':
        return _minimal_spanning_tree_prim(graph, starting_node)


def _minimal_spanning_tree_prim(graph, starting_node):
    """

    Args:
        graph: weighted adj. matrix as 2d np.array
        starting_node: node number to start construction of minimal spanning tree
    Returns:
        minimal spanning tree as 2d array calculted by Prim
    """

    node_count = len(graph)
    all_nodes = [i for i in range(node_count)]

    if starting_node is None:
        starting_node = randint(0, node_count)

    unvisited_nodes = all_nodes
    visited_nodes = [starting_node]
    unvisited_nodes.remove(starting_node)
    mst = np.zeros((node_count, node_count))

    while len(visited_nodes) != node_count:
        selected_subgraph = graph[np.array(visited_nodes)[:, None], np.array(unvisited_nodes)]
        # we mask non-exist edges with -- so it doesn't crash the argmin
        min_edge_index = np.unravel_index(np.ma.masked_equal(selected_subgraph, 0, copy=False).argmin(),
                                          selected_subgraph.shape)
        edge_from = visited_nodes[min_edge_index[0]]
        edge_to = unvisited_nodes[min_edge_index[1]]
        mst[edge_from, edge_to] = graph[edge_from, edge_to]
        mst[edge_to, edge_from] = graph[edge_from, edge_to]
        unvisited_nodes.remove(edge_to)
        visited_nodes.append(edge_to)

    return mst


def count_odd_even_nodes(graph):
    """
    Calculates number of odd and even nodes in graph
    Args:
        graph: adj. matrix as 2d np.array

    Returns:
    dictionary with odd and even nodes
    """
    # TODO: What to do if component is not connected?
    if 2 % 2 == 0:
        pass  # Even
    else:
        pass  # Odd

