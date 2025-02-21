from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid, (rows, cols), starts = parse_input(f)

        s = 0
        for start in starts:
            q = [start]

            while q:
                r, c = q.pop()
                if grid[r][c] == 9:
                    s += 1

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    rx, cx = r + dr, c + dc
                    if not (0 <= rx < rows and 0 <= cx < cols): continue

                    if grid[rx][cx] - grid[r][c] == 1:
                        q.append((rx, cx))

        print(s)

if __name__ == '__main__':
    main()