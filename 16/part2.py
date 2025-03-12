from part1 import parse_input, find_first_tile, dijkstra

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        start = find_first_tile(grid, symbol='S')
        end = find_first_tile(grid, symbol='E')

        start_dists = dijkstra(grid, starts=[(start, (0, 1))])
        end_dists = dijkstra(grid, starts=[(end, d) for d in directions])
        total = min([start_dists[(position, direction)] for position, direction in start_dists if position == end])

        in_optimal = set()
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                for d in directions:
                    opposite = directions[(directions.index(d) + 2) % 4]
                    if start_dists[((r, c), d)] + end_dists[((r, c), opposite)] == total:
                        in_optimal.add((r, c))

        print(len(in_optimal))

if __name__ == '__main__':
    main()
