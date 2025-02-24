from part1 import parse_input, step

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        line = parse_input(f)
        cache = {}
        print(sum([step(number, 75, cache) for number in line]))

if __name__ == '__main__':
    main()