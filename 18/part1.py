def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        positions = parse_input(f)
        blocked = positions[:1024]
        size = (70, 70)

        print(get_step_count(blocked, size))

def parse_input(file) -> list[tuple[int, int]]:
    lines = file.read().strip().split('\n')

    positions = []
    for line in lines:
        c, r = line.strip().split(',')
        positions.append((int(r), int(c)))

    return positions


def get_step_count(blocked: list[tuple], size: tuple[int, int]) -> int | None:
    '''
    Returns minimum steps needed to go from top-left corner to bottom-right corner or None when path is impossible
    '''

    max_r, max_c = size

    Q = [(0, 0, 0)]
    seen = []

    while Q:
        r, c, steps = Q.pop(0)

        if r == max_r and c == max_c: return steps

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r, new_c = r + dr, c + dc

            in_bounds = 0 <= new_r <= max_r and 0 <= new_c <= max_c
            not_seen = (new_r, new_c) not in seen
            not_blocked = (new_r, new_c) not in blocked

            if in_bounds and not_seen and not_blocked:
                seen.append((new_r, new_c))
                Q.append((new_r, new_c, steps + 1))

    return None

if __name__ == '__main__':
    main()
