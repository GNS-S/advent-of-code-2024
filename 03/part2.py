import re

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        arguments = parse_input(f)

        s = sum([a * b for (a, b) in arguments])
        print(s)

def parse_input(file) -> list[tuple[int, int]]:
    text = file.read().strip()

    matches = re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', text)
    arguments = []
    toggle = True
    for m in matches:
        match m[0]:
            case 'do()':
                toggle = True
            case 'don\'t()':
                toggle = False
            case _:
                if toggle:
                    a, b = m.groups()
                    arguments.append((int(a), int(b)))

    return arguments

if __name__ == '__main__':
    main()