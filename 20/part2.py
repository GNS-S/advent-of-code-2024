from part1 import parse_input, get_cheat_path_count

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        start, total_distance, grid = parse_input(f)
        print(get_cheat_path_count(start, total_distance, grid, cheat_length=20))

if __name__ == '__main__':
    main()
