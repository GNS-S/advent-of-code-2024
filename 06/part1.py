def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        path = get_path(grid, get_starting_coords(grid))
        unique_locations = set([(r, c) for r, c, _ in path])

        print(len(unique_locations))

def parse_input(file) -> list[list[str]]:
    lines = file.read().strip().split('\n')

    return [list(line) for line in lines]

def get_starting_coords(grid: list[list[str]]) -> tuple[int, int, tuple[int, int]]:
    starting_symbol = '^'

    for r, row in enumerate(grid):
        if starting_symbol in row:
            return (r, row.index(starting_symbol), (-1, 0))
        
    raise ValueError('Starting symbol not found in grid')

def turn_right(position: tuple[int, int, tuple[int, int]]):
    # North, East, South, West
    r, c, direction = position
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    new_dr, new_dc = directions[(directions.index(direction) + 1) % 4]
    new_r = r + new_dr
    new_c = c + new_dc
    return (new_r, new_c, (new_dr, new_dc))

def get_path(grid: list[list[str]], start: tuple[int, int, tuple[int, int]]) -> tuple[list[tuple], bool]:
    rows, cols = len(grid), len(grid[0])

    path = []
    current = start

    while current not in path and (0 <= current[0] <= rows - 1) and (0 <= current[1] <= cols - 1):
        r, c, direction = current
        dr, dc = direction
        if grid[r][c] == '#':
            current = turn_right((r - dr, c - dc, direction))
        else:
            path.append(current)
            current = (r + dr, c + dc, direction)

    return path

if __name__ == '__main__':
    main()