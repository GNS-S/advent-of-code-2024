def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        s = 0
        for ir, row in enumerate(grid):
            for ic, col in enumerate(row):
                for d in directions:
                    s += 1 if check(grid, (ir, ic), d) else 0

        print(s)

def parse_input(file) -> list[list[str]]:
    lines = file.read().strip().split('\n')
    return [list(l) for l in lines]

def check(grid: list[list[str]], start: tuple[int, int], direction: tuple[int, int], word = 'XMAS') -> bool:
    dx, dy = direction
    position = start
    for letter in word:
        x, y = position
        if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
            return False
        if grid[x][y] != letter:
            return False
        position = (x  + dx, y + dy)
    return True

if __name__ == '__main__':
    main()