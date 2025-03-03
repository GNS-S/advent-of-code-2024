from re import findall
from math import floor

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        robots = parse_input(f)
        grid_r, grid_c = 103, 101
        middle_r, middle_c = floor(grid_r / 2), floor(grid_c / 2)
        steps = 100

        quadrants = { 'NW': 0, 'NE': 0, 'SW': 0, 'SE': 0 }
        for robot in robots:
            (r, c), (dr, dc) = robot
            
            new_r, new_c = (r + dr * steps) % grid_r, (c + dc * steps) % grid_c

            if new_r == middle_r or new_c == middle_c: continue
            quadrants[f"{'S' if new_r > middle_r else 'N'}{'E' if new_c > middle_c else 'W'}"] += 1

        print(quadrants['NW'] * quadrants['NE'] * quadrants['SW'] * quadrants['SE'])

def parse_input(file) -> tuple[list[list[str]], tuple[int, int]]:
    lines = file.read().strip().split('\n')

    robots = []
    for line in lines:
        c, r, dc, dr = findall(r'-?[0-9]\d*', line)
        robots.append(((int(r), int(c)), (int(dr), int(dc))))

    return robots

if __name__ == '__main__':
    main()
