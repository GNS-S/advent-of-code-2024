def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        keys, locks, height = parse_input(f)

        s = 0
        for key in keys:
            for lock in locks:
                if all([key[i] + lock[i] <= height for i in range(height)]):
                    s += 1
        
        print(s)

def parse_input(file) -> dict[str, set]:
    schematics = file.read().strip().split('\n\n')
    keys, locks, height = [], [], 0

    for s in schematics:
        group = keys if s[0] == '.' else locks
        weights = [0, 0, 0, 0, 0]

        lines = s.splitlines()
        height = max(len(lines) - 2, height)

        for line in lines[1:len(lines) -1]:
            for i, c in enumerate(line):
                if c == '#': weights[i] += 1
        
        group.append(weights)
    
    return keys, locks, height

if __name__ == '__main__':
    main()
