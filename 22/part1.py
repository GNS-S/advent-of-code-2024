def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        numbers = parse_input(f)
        
        for _ in range(2000):
            for i in range(len(numbers)):
                numbers[i] = fn(numbers[i])

        print(sum(numbers))

def parse_input(file) -> list[int]:
    lines = file.read().strip().splitlines()

    return [int(l) for l in lines]

def prune(x: int):
    return x % 16777216

def fn(x: int):
    out = prune(x ^ (64 * x))
    out = prune(out ^ (out // 32))
    out = prune(out ^ (out * 2048))
    return out

if __name__ == '__main__':
    main()
