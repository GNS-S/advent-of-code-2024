from heapq import heappop, heappush
from sys import maxsize
from collections import defaultdict

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        registers, commands = parse_input(f)
        parser = Parser(registers, commands, pointer=0)
        print(','.join(map(str, parser.run())))

class Parser:
    def __init__(self, registers: dict, commands: list[int], pointer: int):
        self.registers = registers.copy()
        self.commands = commands.copy()
        self.pointer = pointer

    def combo_operand(self, operand: int):
        match operand:
            case 4: return self.registers['A']
            case 5: return self.registers['B']
            case 6: return self.registers['C']
            case _: return operand

    def run(self) -> list[int]:
        out = []
        while self.pointer < len(self.commands):

            opcode, operand = self.commands[self.pointer], self.commands[self.pointer + 1]

            match opcode:
                case 0:
                    self.registers['A'] = int(self.registers['A'] / (2**self.combo_operand(operand)))
                case 1:
                    self.registers['B'] = self.registers['B'] ^ operand
                case 2:
                    self.registers['B'] = self.combo_operand(operand) % 8
                case 3:
                    if self.registers['A'] != 0:
                        self.pointer = operand
                        continue
                case 4:
                    self.registers['B'] = self.registers['B'] ^ self.registers['C']
                case 5:
                    out.append(self.combo_operand(operand) % 8)
                case 6:
                    self.registers['B'] = int(self.registers['A'] / (2**self.combo_operand(operand)))
                case 7:
                    self.registers['C'] = int(self.registers['A'] / (2**self.combo_operand(operand)))
                
            self.pointer += 2

        return out

def parse_input(file) -> tuple[dict, list]:
    registers_str, commands_str = file.read().strip().split('\n\n')

    registers = {}
    for line in registers_str.split('\n'):
        register, value = line[len('Register: ') - 1:].split(': ')
        registers[register] = int(value)

    return registers, [int(c) for c in commands_str[len('Program: ') - 1:].split(',')]


if __name__ == '__main__':
    main()
