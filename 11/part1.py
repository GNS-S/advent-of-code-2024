def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        line = parse_input(f)
        cache = {}
        print(sum([step(number, 25, cache) for number in line]))

def parse_input(file) -> list[int]:
    lines = file.read().strip().split('\n')
    return [int(number) for number in lines[0].split()]

def step(number: int, steps_left: int, cache: dict):
    if steps_left == 0: return 1
    if (number, steps_left) in cache: return cache[(number, steps_left)]

    string = str(number)

    if number == 0:
        result = step(1, steps_left - 1, cache)
    elif len(string) % 2 == 1:
        result = step(number * 2024, steps_left - 1, cache)
    else: 
        half = len(string) // 2
        a, b = int(string[:half]), int(string[half:])
        result = step(a, steps_left - 1, cache) + step(b, steps_left - 1, cache)

    cache[(number, steps_left)] = result
    return result

if __name__ == '__main__':
    main()