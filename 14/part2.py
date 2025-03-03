from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        robots = parse_input(f)
        grid_r, grid_c = 103, 101
        grid = [['.' for _ in range(grid_c)] for _ in range(grid_r)]

        # Just baselessly guessing that all robots will need to have unique positions when the christmas tree is formed
        # Turns out that's correct (for my input)!
        # Could also try to have some sort of proximity score for the robots and print pictures when an arbitrary
        # threshold is crossed
        unique_positions = set()
        step = 0

        while len(unique_positions) != len(robots):
            unique_positions = set()
            step += 1

            for i in range(len(robots)):
                (r, c), (dr, dc) = robots[i]
                new_pos = (r + dr) % grid_r, (c + dc) % grid_c
                robots[i] = new_pos, (dr, dc)
                unique_positions.add(new_pos)
        
        for (r, c), _ in robots:
            grid[r][c] = '#'
        
        print('\n'.join([''.join(line) for line in grid]))
        print(step)

if __name__ == '__main__':
    main()
