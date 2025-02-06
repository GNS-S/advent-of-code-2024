from part1 import parse_input, get_first_failing_rule

def main(): # TODO
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        rules, updates = parse_input(f)

        incorrect_updates = [update for update in updates if get_first_failing_rule(rules, update) != None]
        print(incorrect_updates)

        s = 0
        for update in incorrect_updates:
            rule = get_first_failing_rule(rules, update)
            fixed = update

            while rule != None:
                print(rule)
                before, after = rule.split('|')
                fixed[fixed.index(before)], fixed[fixed.index(after)] = after, before
                rule = get_first_failing_rule(rules, fixed)

            middle_index = int((len(fixed) - 1) / 2)
            s += int(fixed[middle_index])

        print(s)

if __name__ == '__main__':
    main()