def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid, (rows, cols), starts = parse_input(f)

        s = 0
        for start in starts:
            q = [start]
            visited = set()

            while q:
                r, c = q.pop()
                visited.add((r, c))
                if grid[r][c] == 9:
                    s += 1

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    rx, cx = r + dr, c + dc
                    if not (0 <= rx < rows and 0 <= cx < cols): continue
                    if (rx, cx) in visited: continue

                    if grid[rx][cx] - grid[r][c] == 1:
                        q.append((rx, cx))

        print(s)

def parse_input(file) -> list[(  )]:
    lines = file.read().strip().split('\n')

    grid = [list(map(int, list(line))) for line in lines]
    rows, cols = len(lines), len(lines[0])
    starts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    return grid, (rows, cols), starts

if __name__ == '__main__':
    main()