from part1 import parse_input, find_start_coordinates

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        initial_grid, commands = parse_input(f)
        expansion = {
            '@': ['@', '.'],
            '#': ['#', '#'],
            '.': ['.', '.'],
            'O': ['[', ']']
        }
        grid = []
        for row in initial_grid:
            grid.append([])
            for tile in row:grid[-1] += expansion[tile]

        r, c = find_start_coordinates(grid)

        for command in commands:
            dr, dc = command

            to_move = [(r, c)]
            Q = [(r + dr, c + dc)]
            while Q:
                x, y = Q.pop(0)
                tile = grid[x][y]

                if tile in ['[', ']']:
                    if (x, y) not in to_move: to_move.append((x, y))
                    Q.append((x + dr, y + dc))

                    if dr != 0:
                        y_offset = 1 if tile == '[' else - 1
                        if (x, y + y_offset) not in to_move: to_move.append((x, y + y_offset))
                        Q.append((x + dr, y + dc + y_offset))

                if tile == '#':
                    to_move = []
                    Q = []

            if to_move:
                for x, y in reversed(to_move):
                    grid[x + dr][y + dc] = grid[x][y]
                    grid[x][y] = '.'
                r, c = r + dr, c + dc

        s = 0
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == '[': s += 100 * r + c

        print(s)

if __name__ == '__main__':
    main()
