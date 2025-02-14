from part1 import parse_input

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
                    # This just works and is very reasonably fast
                    #
                    # A more elegant solution would be working through the numbers in reverse, checking whether the last
                    # number could be used to make the goal value (the goal value shifting to the last number checked)
                    # e.g. concateneation is only tractable if the last digits of the value is equal to the goal
                    #      multiplication is only tractable if the goal is divisible by the value
                    #
                    # Source: https://www.reddit.com/r/adventofcode/comments/1h8l3z5
                    new_totals.append(int(str(total) + str(x)))
                totals = new_totals

            if goal in totals:
                s += goal

        print(s)

if __name__ == '__main__':
    main()