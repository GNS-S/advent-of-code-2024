from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        machines = parse_input(f)

        s = 0
        for machine in machines:
            (a11, a12), (a21, a22), (b1, b2) = machine
            b1 += 10000000000000
            b2 += 10000000000000

            x1 = (b1 * a22 - b2 * a21) / (a11 * a22 - a12 * a21)
            x2 = (b2 * a11 - b1 * a12) / (a11 * a22 - a12 * a21)

            if x1.is_integer() and x2.is_integer():
                s += int(x1 * 3 + x2)

        print(s)

if __name__ == '__main__':
    main()
