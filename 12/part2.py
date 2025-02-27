from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid, (rows, cols) = parse_input(f)
        seen = []
        s = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen: continue
                s += get_region_price(grid, (r, c), seen)

        print(s)

def get_region_price(grid: list[list[str]], start: tuple[int, int], seen: list) -> tuple[int, int]:
    rows, cols = len(grid), len(grid[0])
    start_r, start_c = start
    color = grid[start_r][start_c]
    seen.append(start)

    in_bounds = lambda coords: 0 <= coords[0] < rows and 0 <= coords[1] < cols

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    Q = [start]
    size = 0
    corners = 0

    while Q:
        r, c = Q.pop(0)
        seen.append((r, c))
        size += 1

        for dr1, dc1 in directions:
            r1, c1 = r + dr1, c + dc1
            in1 = in_bounds((r1, c1))
            color1 = in1 and grid[r1][c1] == color

            # Rotate the direction 90 degrees, use both directions to check whether adjacement tiles form a corner
            dr2, dc2 = directions[(directions.index((dr1, dc1)) + 1) % 4]
            r2, c2 = r + dr2, c + dc2
            in2 = in_bounds((r2, c2))
            color2 = in2 and grid[r2][c2] == color

            if (not in1 or not color1) and (not in2 or not color2):
                corners += 1
            elif in1 and color1 and in2 and color2 and grid[r1 + dr2][c1 + dc2] != color:
                corners += 1

            if in1 and color1 and (r1, c1) not in seen and (r1, c1) not in Q:
                Q.append((r1, c1))

    return size * corners

if __name__ == '__main__':
    main()
