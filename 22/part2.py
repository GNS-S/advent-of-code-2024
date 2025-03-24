from collections import Counter
from part1 import parse_input, fn

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        numbers = parse_input(f)

        totals = Counter()

        for x in numbers:
            sequence = [x] 
            for _ in range(2000): sequence.append(fn(sequence[-1]))
            deltas = [x2 % 10 - x1 % 10 for x1, x2 in zip(sequence, sequence[1:])]

            sequence_values = {}
            for i in range(4, len(sequence)):
                key = tuple(deltas[i - 4:i])
                if key not in sequence_values:
                    sequence_values[key] = sequence[i] % 10

            totals.update(sequence_values)

        print(max(totals.values()))
if __name__ == '__main__':
    main()
