def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        disk_map = parse_input(f)
        position = 0
        free_blocks: list[Block] = []
        used_blocks: list[Block] = []

        for i, size in enumerate(disk_map):
            id = i / 2 if i % 2 == 0 else None
            for _ in range(size):
                (used_blocks if id != None else free_blocks).append(Block(position, id))
                position += 1

        for used in used_blocks[::-1]:
            for free in free_blocks:
                if free.position <= used.position:
                    used.position, free.position = free.position, used.position
                    break

        s = sum([block.value() for block in used_blocks])
        print(s)

class Block():
    def __init__(self, position: int, id: int | None, size: int = 1):
        """id of None signifies an empty space block"""
        self.position = position
        self.size = size
        self.id = id

    def value(self) -> int:
        position_sum = (2 * self.position + self.size - 1) * (self.size / 2);
        return int(position_sum * self.id if self.id != None else 0)

def parse_input(file) -> list[(  )]:
    lines = file.read().strip().split('\n')
    return [int(number) for number in list(lines[0])]

if __name__ == '__main__':
    main()