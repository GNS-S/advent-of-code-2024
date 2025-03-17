def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        blocks, patterns = parse_input(f)
        cache = {}
        s = 0

        for pattern in patterns:
            if combinations(blocks, pattern, cache) > 0: s += 1

        print(s)

def combinations(blocks: list[str], pattern: str, cache: dict):
    if pattern in cache: return cache[pattern]

    total = 0
    if pattern == '': total += 1

    for block in blocks:
        if pattern.startswith(block):
            total += combinations(blocks, pattern.removeprefix(block), cache)

    cache[pattern] = total

    return total

def parse_input(file) -> tuple[list, list]:
    blocks, patterns = file.read().strip().split('\n\n')

    return blocks.split(', '), patterns.split('\n')

if __name__ == '__main__':
    main()
