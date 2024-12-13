def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        l, r = parse_input(f)

        assert len(l) == len(r)
        l.sort()
        r.sort()

        s = 0
        for i in range(len(l)):
            s += abs(l[i] - r[i])
        
        print(s)

def parse_input(file) -> tuple[list, list]:
    lines = file.read().strip().split('\n')

    left, right = [], []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    return left, right

if __name__ == '__main__':
    main()