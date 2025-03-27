from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        graph = parse_input(f)

        cliques = bron_kerbosch(graph, set(graph.keys()))
        largest = max(cliques, key=len)
        print(','.join(sorted(largest)))

# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def bron_kerbosch(graph: dict, P: set, R=set(), X=set()):
    if not  any([P, X]):
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(graph, P.intersection(graph[v]), R.union([v]), X.intersection(graph[v]))
        X.add(v)

if __name__ == '__main__':
    main()

