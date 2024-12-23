def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        reports = parse_input(f)

        s = 0
        for report in reports:
            if get_first_invalid_index(report) ==  None:
                s += 1

        print(s)

def parse_input(file) -> list[list[int]]:
    lines = file.read().strip().split('\n')

    reports = []
    for line in lines:
        reports.append([int(level) for level in line.split()])

    return reports

def get_first_invalid_index(report: list[int]) -> int | None:
    last_delta = None
    for i in range(1, len(report)):
        delta = report[i] - report[i - 1]

        if not(1 <= abs(delta) <= 3) or (last_delta != None and last_delta * delta < 0):
            return i - 1

        last_delta = delta

    return None

if __name__ == '__main__':
    main()