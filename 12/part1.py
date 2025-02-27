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

def parse_input(file) -> tuple[list[list[str]], tuple[int, int]]:
    lines = file.read().strip().split('\n')
    return [list(line) for line in lines], (len(lines), len(lines[0]))

def get_region_price(grid: list[list[str]], start: tuple[int, int], seen: list) -> tuple[int, int]:
    rows, cols = len(grid), len(grid[0])
    start_r, start_c = start
    region_symbol = grid[start_r][start_c]
    seen.append(start)

    Q = [start]
    size = 0
    perimeter = 0

    while Q:
        r, c = Q.pop(0)
        seen.append((r, c))
        size += 1

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            rx, cx = r + dr, c + dc

            if not (0 <= rx < rows and 0 <= cx < cols):
                perimeter += 1
            elif grid[rx][cx] != region_symbol:
                perimeter += 1
            elif (rx, cx) not in seen and (rx, cx) not in Q:
                Q.append((rx, cx))
    
    return size * perimeter

if __name__ == '__main__':
    main()
