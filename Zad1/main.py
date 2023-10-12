import getopt
import itertools
import math
import sys


def main(argv):
    file = ''
    k = 0
    try:
        opts, args = getopt.getopt(argv, "k:f:", ['file='])
    except:
        print("podano złe parametry")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-k':
            k = int(arg)
        elif opt in ('-f', '--file'):
            file = arg

    if k < 3:
        print("k jest za małe")
        sys.exit(2)

    points = read_points_from_file(file)

    if k >= len(points):
        print("k jest za duże")
        sys.exit(2)

    result = maximize_distance(points, k)

    str = subset_indexes_str(points, result)

    print(calculate_sum_of_distances(result))
    print(str)


def read_points_from_file(file):
    with open(file, 'r') as f:
        str = f.readlines()
        points = []

        for i in str:
            points_str = i.replace('\n', '').split(',')
            points.append((int(points_str[0]), int(points_str[1])))
        return points


def distance(point1, point2):
    return math.dist(point1, point2)


def maximize_distance(points, k):
    max_distance = 0
    max_subset = []

    point_combinations = itertools.combinations(points, k)

    for subset in point_combinations:
        total_distance = sum(distance(p1, p2) for p1, p2 in itertools.combinations(subset, 2))

        if total_distance > max_distance:
            max_distance = total_distance
            max_subset = subset

    return max_subset


def calculate_sum_of_distances(subset):
    total = 0
    for i in range(0, len(subset)):
        for j in range(i + 1, len(subset)):
            total += distance(subset[i], subset[j])
    return round(total, 2)


def subset_indexes_str(set, subset):
    str = f'{set.index(subset[0])}'
    for i in range(1, len(subset)):
        str += f', {set.index(subset[i])}'
    return str


if __name__ == '__main__':
    main(sys.argv[1:])
