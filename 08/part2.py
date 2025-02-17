from part1 import parse_input
from collections import defaultdict

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid, shape = parse_input(f)
        rows, cols = shape
        in_bounds = lambda rx, cx: 0 <= rx < rows and 0 <= cx < cols

        nodes = defaultdict(list)
        antinodes = set()

        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if value == '.':
                    continue
    
                for other in nodes[value]:
                    r2, c2 = other
                    dr, dc = (r2 - r, c2 - c)

                    rx, cx = r, c
                    while in_bounds(rx, cx):
                        antinodes.add((rx, cx))
                        rx, cx = rx - dr, cx - dc

                    rx, cx = r2, c2
                    while in_bounds(rx, cx):
                        antinodes.add((rx, cx))
                        rx, cx = rx + dr, cx + dc
                    
                nodes[value].append((r, c))

        print(len(antinodes))

if __name__ == '__main__':
    main()