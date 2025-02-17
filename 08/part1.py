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
                    
                    for (rx, cx) in [(r - dr, c - dc), (r2 + dr, c2 + dc)]:
                        if in_bounds(rx, cx):
                            antinodes.add((rx, cx))
                nodes[value].append((r, c))

        print(len(antinodes))

def parse_input(file) -> tuple[list[list[str]], tuple[int, int]]:
    lines = file.read().strip().split('\n')
    rows, cols = len(lines), len(lines[0])

    return [list(row) for row in lines], (rows, cols)

if __name__ == '__main__':
    main()