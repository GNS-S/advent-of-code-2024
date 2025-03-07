def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        machines = parse_input(f)

        s = 0
        for machine in machines:
            (a11, a12), (a21, a22), (b1, b2) = machine

            x1 = (b1 * a22 - b2 * a21) / (a11 * a22 - a12 * a21)
            x2 = (b2 * a11 - b1 * a12) / (a11 * a22 - a12 * a21)

            if x1.is_integer() and x2.is_integer():
                s += int(x1 * 3 + x2)

        print(s)

def parse_input(file) -> list[tuple, tuple, tuple]:
    machine_strs = file.read().strip().split('\n\n')

    parse_button = lambda str: tuple([int(coord.split('+')[1]) for coord in str.split(': ')[1].split(', ')])

    machines = []
    for machine in machine_strs:
        a_str, b_str, goal_str = machine.split('\n')
        a = parse_button(a_str)
        b = parse_button(b_str)
        goal = tuple([int(coord.split('=')[1]) for coord in goal_str.split(': ')[1].split(', ')])
        machines.append((a, b, goal))
        
    return machines

if __name__ == '__main__':
    main()
