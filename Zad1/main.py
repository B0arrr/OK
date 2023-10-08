import getopt
import sys
from cmath import sqrt
import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt


def main(argv):
    file = ''
    k = 0
    try:
        opts, args = getopt.getopt(argv, "k:f:", ['file='])
    except:
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-k':
            k = int(arg)
        elif opt in ('-f', '--file'):
            file = arg

    if k < 3:
        sys.exit(2)

    points = read_points_from_file(file)
    edge_list_with_weights = generate_edge_list_with_weights(points)
    graph = nx.Graph()
    graph.add_weighted_edges_from(edge_list_with_weights)
    mst = tree.maximum_spanning_edges(graph, algorithm="kruskal", data=False)
    edgelist = list(mst)
    print(sorted(sorted(e) for e in edgelist))


def read_points_from_file(file):
    with open(file, 'r') as f:
        str = f.readlines()
        points = []

        for i in str:
            points_str = i.replace('\n', '').split(',')
            points.append((int(points_str[0]), int(points_str[1])))
        return points


def generate_edge_list_with_weights(list):
    elist = []

    for i in list:
        list2 = list.copy()
        list2.remove(i)
        for j in list2:
            weight = sqrt(pow(abs(i[0]-j[0]), 2) + pow(abs(i[1] - j[1]), 2))
            weight_fixed = round(weight.real * 1000)
            elist.append((list.index(i), list.index(j), weight_fixed))
    print(elist)
    return elist


if __name__ == '__main__':
    main(sys.argv[1:])
