from part1 import parse_input, get_first_invalid_index

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        reports = parse_input(f)

        s = 0
        for report in reports:
            index = get_first_invalid_index(report)
            if index == None:
                s += 1
            else:
                excludable = [i for i in [index - 1, index, index + 1] if 0 <= i <= len(report)]
                if any([get_first_invalid_index(exclude(report, i)) == None for i in excludable]):
                    s += 1 
        print(s)

def exclude(array: list, index: int) -> list:
    return array[:index] + array[index + 1:]

if __name__ == '__main__':
    main()