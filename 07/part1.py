def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        equations = parse_input(f)
        
        s = 0
        for equation in equations:
            goal, numbers = equation
            totals = [numbers[0]]

            for x in numbers[1:]:
                new_totals = []
                for total in totals:
                    new_totals.append(total + x)
                    new_totals.append(total * x)
                totals = new_totals

            if goal in totals:
                s += goal

        print(s)

def parse_input(file) -> list[list[str]]:
    lines = file.read().strip().split('\n')

    equations = []
    for line in lines:
        total, numbers = line.split(': ')
        equations.append((int(total), [int(x) for x in numbers.split()]))

    return equations

if __name__ == '__main__':
    main()