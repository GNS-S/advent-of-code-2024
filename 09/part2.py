from part1 import Block, parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        disk_map = parse_input(f)
        position = 0
        free_blocks: list[Block] = []
        used_blocks: list[Block] = []

        for i, size in enumerate(disk_map):
            id = int(i / 2) if i % 2 == 0 else None
            (used_blocks if id != None else free_blocks).append(Block(position, id, size))
            position += size

        for used in used_blocks[::-1]:
            for free in free_blocks:
                if free.position <= used.position and free.size >= used.size:
                    used.position = free.position
                    free.size -= used.size
                    free.position += used.size
                    break

        s = sum([block.value() for block in used_blocks])
        print(s)

if __name__ == '__main__':
    main()