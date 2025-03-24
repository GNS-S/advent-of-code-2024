from collections import defaultdict

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        codes, numpad, dirpad = parse_input(f)
        print(solve(codes, numpad, dirpad, dirpad_chain=2))

def parse_input(file) -> tuple[tuple, tuple, int, list[list], tuple]:
    lines = file.read().strip().splitlines()

    return lines, pad_to_dict(['789', '456', '123', 'X0A']), pad_to_dict(['X^A', '<v>'])

def pad_to_dict(grid: list) -> dict:
    d = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != 'X': d[char] = (r, c)
    d.update({v:k for k, v in d.items()})
    return d

# Reasoning behind these priorities https://www.reddit.com/r/adventofcode/comments/1hj2odw/comment/m33qs9d
# Could also DFS or Dijkstra on the pad to generate the most efficient paths
def step(start: str, end: str, pad: dict):
    sx, sy = pad[start]
    ex, ey = pad[end]
    dx, dy = ex - sx, ey - sy

    vertical =   'v' * dx + '^' * -dx
    horizontal = '>' * dy + '<' * -dy

    if '>' in horizontal and (ex, sy) in pad:
        return vertical + horizontal + 'A'
    if (sx, ey) in pad:
        return horizontal + vertical + 'A'
    if (ex, sy) in pad:
        return vertical + horizontal + 'A'

def command_counts(buttons: list, pad: dict):
    route = ['A', *buttons]
    counts = defaultdict(lambda: 0)
    for start, end in zip(route[:-1], route[1:]):
        counts[step(start, end, pad)] += 1
    return counts

def solve(codes: list, numpad: dict, dirpad: dict, dirpad_chain=2):
    code_command_counts = [command_counts(code, numpad) for code in codes]
    for _ in range(dirpad_chain):
        updated_counts = []

        for count in code_command_counts:
            new_count = defaultdict(lambda: 0)
            for chunk, qty in count.items():
                for k, v in command_counts(chunk, dirpad).items():
                    new_count[k] += v * qty

            updated_counts.append(new_count)
    
        code_command_counts = updated_counts

    s = 0
    for route, count in zip(code_command_counts, codes):
        s += sum(len(k) * v for k, v in route.items()) * int(count[:-1])

    return s

if __name__ == '__main__':
    main()
