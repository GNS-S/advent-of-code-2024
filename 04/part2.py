from part1 import parse_input, check

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        words = ['MAS', 'SAM']

        s = 0
        for ir, row in enumerate(grid):
            for ic, col in enumerate(row):
                if col == 'A':
                    lr_vertical = any([check(grid, (ir - 1, ic - 1), (1, 1), word=w) for w in words])
                    rl_vertical  = any([check(grid, (ir - 1, ic + 1), (1, -1), word=w) for w in words])
                    if lr_vertical and rl_vertical:
                        s += 1

        print(s)

if __name__ == '__main__':
    main()