from part1 import parse_input, get_step_count

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        all_blocks = parse_input(f)
        size = 70, 70
        
        unchecked, connected, blocked = all_blocks.copy(), [], []

        while len(unchecked) > 1:
            split_index = len(unchecked) // 2
            left, right = unchecked[:split_index], unchecked[split_index:]

            active_blocks = connected + left
            
            connects = get_step_count(active_blocks, size) != None

            if connects:
                connected = connected + left
                unchecked = right
            else:
                blocked = right + blocked
                unchecked = left

        y, x = unchecked[0]
        print(f'{x},{y}')
            
if __name__ == '__main__':
    main()
