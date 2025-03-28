def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        wires, gates, fn = parse_input(f)

        while gates:
            in1, in2, out, op = gates.pop(0)
            if in1 in wires and in2 in wires:
                wires[out] = fn[op](wires[in1], wires[in2])
            else:
                gates.append((in1, in2, out, op))

        zs = sorted([k for k in wires.keys() if k.startswith('z')], reverse=True)
        print(int(''.join([str(wires[z]) for z in zs]), 2))

def parse_input(file) -> dict[str, set]:
    wire_lines, gate_lines = file.read().strip().split('\n\n')

    wires = {}
    for line in wire_lines.splitlines():
        k, v = line.split(': ')
        wires[k] = int(v)

    gates = []
    for line in gate_lines.splitlines():
        in1, op, in2, _, out = line.split()
        gates.append((in1, in2, out, op))

    fn = {
        'AND': lambda x, y: x & y,
        'OR': lambda x, y: x | y,
        'XOR': lambda x, y: x ^ y
    }

    return wires, gates, fn

if __name__ == '__main__':
    main()
