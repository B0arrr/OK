import networkx as nx
import dwave_networkx as dnx
import dimod


if __name__ == '__main__':
    graph = nx.Graph(nx.nx_pydot.read_dot("graph.dot"))
    sampler = dimod.ExactSolver()
    result = dnx.algorithms.cover.min_vertex_cover(graph, sampler)
    print(result)
    print(f'Minimalna ilość strachów na wróble: {len(result)}')
