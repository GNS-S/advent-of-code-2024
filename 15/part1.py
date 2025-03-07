def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid, commands = parse_input(f)
        r, c = find_start_coordinates(grid)

        for command in commands:
            dr, dc = command

            to_move = [(r, c)]
            Q = [(r + dr, c + dc)]
            while Q:
                x, y = Q.pop()
                tile = grid[x][y]

                if tile == '#':
                    to_move = []
                elif tile == 'O':
                    to_move.append((x, y))
                    Q.append((x + dr, y + dc))

            if to_move:
                for x, y in reversed(to_move):
                    grid[x + dr][y + dc] = grid[x][y]
                    grid[x][y] = '.'
                r, c = r + dr, c + dc

        s = 0
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == 'O': s += 100 * r + c

        print(s)

def parse_input(file) -> tuple[list[list[str]], list[list[str]]]:
    direction = {
        '^': (-1,  0),
        '>': ( 0,  1),
        'v': ( 1,  0),
        '<': ( 0, -1)
    }

    grid_lines, command_lines = file.read().strip().split('\n\n')

    grid = [list(line) for line in grid_lines.split('\n')]
    commands = [direction[c] for c in sum(map(list, command_lines.split('\n')), [])]

    return grid, commands

def find_start_coordinates(grid: list[list[str]], start_symbol = '@') -> tuple[int, int]:
    for r, row in enumerate(grid):
        if start_symbol in row: return (r, row.index(start_symbol))

if __name__ == '__main__':
    main()
