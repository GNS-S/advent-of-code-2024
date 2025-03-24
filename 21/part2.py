from part1 import parse_input, solve

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        codes, numpad, dirpad = parse_input(f)
        print(solve(codes, numpad, dirpad, dirpad_chain=25))

if __name__ == '__main__':
    main()
