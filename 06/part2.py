from part1 import parse_input, get_path, get_starting_coords, turn_right

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        rows, cols = len(grid), len(grid[0])

        visited = []
        path = get_path(grid, get_starting_coords(grid))
        jump_table = {}

        s = 0

        for i in range(1, len(path)):
            current_pos = path[i - 1]
            current_r, current_c, current_direction = current_pos            
            next_pos = path[i]
            next_r, next_c, next_direction = next_pos

            visited.append((current_r, current_c))
            if (next_r, next_c) in visited:
                continue

            new_obstacle_r = next_r
            new_obstacle_c = next_c
            new_obstacle = (new_obstacle_r, new_obstacle_c)
            branch_pos = (current_r, current_c, next_direction)

            # Keep track of position and velocity when hitting all original obstacles. If this repeats we have a loop
            obstacles_hit = []
            prev_obstacle = None

            while (0 <= branch_pos[0] <= rows - 1) and (0 <= branch_pos[1] <= cols - 1):
                if branch_pos in obstacles_hit:
                    s += 1
                    break

                r, c, direction = branch_pos
                dr, dc = direction

                if (r, c) == new_obstacle:
                    # Avoid corrupting jump table with temporary obstacles
                    prev_obstacle = None
                    branch_pos = turn_right((r - dr, c - dc, direction))
            
                elif grid[r][c] == '#':
                    obstacles_hit.append(branch_pos)
                    if prev_obstacle != None:
                       jump_table[prev_obstacle] = branch_pos

                    prev_obstacle = branch_pos
                    turn_r, turn_c, turn_direction = turn_right((r - dr, c - dc, direction))

                    # Don't use jump table if we end up in the same rank and file as the obstacle
                    if branch_pos in jump_table and turn_r != new_obstacle_r and turn_c != new_obstacle_c:
                        branch_pos = jump_table[branch_pos]
                    else:
                        branch_pos = (turn_r, turn_c, turn_direction)

                else:
                    branch_pos = (r + dr, c + dc, direction)

        print(s)

if __name__ == '__main__':
    main()