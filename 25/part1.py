def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        keys, locks = parse_input(f)

        s = 0
        for key in keys:
            for lock in locks:
                if all([key[i] != '#' or lock[i] != '#' for i in range(len(key))]):
                    s += 1
        
        print(s)

def parse_input(file) -> dict[str, set]:
    schematics = file.read().strip().split('\n\n')
    keys, locks = [], []

    for s in schematics:
        (keys if s[0] == '.' else locks).append(s)

    return keys, locks

if __name__ == '__main__':
    main()
