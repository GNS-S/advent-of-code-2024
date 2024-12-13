from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        l, r = parse_input(f)

        s = 0
        for num in l:
            s += num * r.count(num)
        
        print(s)

if __name__ == '__main__':
    main()