import re

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        arguments = parse_input(f)

        s = sum([a * b for (a, b) in arguments])
        print(s)

def parse_input(file) -> list[tuple[int, int]]:
    regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    pairs = regex.findall(file.read().strip())
    return [(int(a), int(b)) for (a, b) in pairs]

if __name__ == '__main__':
    main()