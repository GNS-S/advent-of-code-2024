def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        start, total_distance, grid = parse_input(f)
        print(get_cheat_path_count(start, total_distance, grid, cheat_length=2))

def parse_input(file) -> tuple[tuple, tuple, int, list[list], tuple]:
    lines = file.read().strip().split('\n')

    distance = 1
    grid = []
    for r, line in enumerate(lines):
        row = list(line)
        grid.append(row)
        distance += row.count('.')
        if 'S' in row: start = (r, row.index('S'))

    return start, distance, grid

def get_distances_to_end(start: tuple, total_distance: int, grid: list[list]):
    '''
    Returns a dictionary mapping each path coordinate to how far away it is from the end
    '''
    dists = {}
    Q, seen = [(start, total_distance)], []
    while Q:
        (r, c), distance = Q.pop(0)
        dists[(r, c)] = distance

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r, new_c = r + dr, c + dc
            if grid[new_r][new_c] in ['.', 'E'] and (new_r, new_c) not in seen:
                seen.append((new_r, new_c))
                Q.append(((new_r, new_c), distance - 1))

    return dists

def get_cheat_path_count(start: tuple, total_distance: int, grid: list[list], cheat_length: int, min_shortening=100):
    dists = get_distances_to_end(start, total_distance, grid)

    Q, seen = [(start, 0)], []
    s = 0

    while Q:
        (r, c), so_far = Q.pop(0)

        seen.append((r, c))

        for position, to_end in dists.items():
            rx, cx = position
            to_tile = abs(r - rx) + abs(c - cx)
            if to_tile <= cheat_length:
                s += 1 if so_far + to_tile + to_end <= total_distance - min_shortening else 0

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r, new_c = r + dr, c + dc
            if grid[new_r][new_c] in ['.', 'E'] and (new_r, new_c) not in seen:
                Q.append(((new_r, new_c), so_far + 1))

    return s

if __name__ == '__main__':
    main()
