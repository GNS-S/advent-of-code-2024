from collections import defaultdict
from itertools import combinations

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        graph = parse_input(f)

        s = 0
        for (a, b, c) in combinations(graph, 3):
            if 't' not in a[0] + b[0] + c[0]: continue
            if graph[a] > {b, c} and graph[b] > {a, c} and graph[c] > {a, b}: s += 1

        print(s)

def parse_input(file) -> dict[str, set]:
    lines = file.read().strip().splitlines()
    graph = defaultdict(set)

    for line in lines:
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)

    return graph

if __name__ == '__main__':
    main()

