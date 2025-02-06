def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        rules, updates = parse_input(f)
        s = 0
        for update in updates:
            if get_first_failing_rule(rules, update) == None:
                middle_index = int((len(update) - 1) / 2)
                s += int(update[middle_index])

        print(s)


def parse_input(file) -> tuple[list[str], list[str]]:
    rules, updates = file.read().strip().split('\n\n')

    return rules.split('\n'), [update.split(',') for update in updates.split('\n')]

def get_first_failing_rule(rules: list[str], update: list[str]) -> int | None:
    for rule in rules:
        before, after = rule.split('|')
        if (
            before in update and
            after in update and
            update.index(before) > update.index(after)
        ):
            return rule
            
if __name__ == '__main__':
    main()