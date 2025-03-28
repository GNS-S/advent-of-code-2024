from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        _, gates, _ = parse_input(f)

        # Based on (by which I mean stolen from) https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3kt1je
        # Which is just checking whether gates conform to the structure of a ripple-carry adder:
        # https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
        #
        # I couldn't realize its a ripple carry adder on my own :(

        highest_z = max([out for _, _, out, _ in gates if out.startswith('z')])
        wrong = set()
        for in1, in2, out, op in gates:
            if out[0] == 'z' and op != 'XOR' and out != highest_z:
                wrong.add(out)

            if op == 'XOR' and out[0] != 'z' and in1[0] not in ['x', 'y'] and in2[0] not in ['x', 'y']:
                wrong.add(out)

            if op == 'AND' and 'x00' not in [in1, in2]:
                for next_in1, next_in2, _, next_op in gates:
                    if out in [next_in1, next_in2] and next_op != 'OR':
                        wrong.add(out)

            if op == 'XOR':
                for next_in1, next_in2, _, next_op in gates:
                    if out in [next_in1, next_in2] and next_op == 'OR':
                        wrong.add(out)

        print(','.join(sorted(wrong)))

if __name__ == '__main__':
    main()

