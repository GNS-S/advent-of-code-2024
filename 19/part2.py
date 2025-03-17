from part1 import parse_input, combinations

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        blocks, patterns = parse_input(f)
        cache = {}
        s = 0

        for pattern in patterns:
            s += combinations(blocks, pattern, cache)

        print(s)
            
if __name__ == '__main__':
    main()
