from heapq import heappop, heappush
from sys import maxsize
from collections import defaultdict

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        start = find_first_tile(grid, symbol='S')
        end = find_first_tile(grid, symbol='E')
        distance = dijkstra(grid, starts=[(start, (0, 1))])

        print(min([distance[(position, direction)] for position, direction in distance if position == end]))

def parse_input(file) -> list[list[str]]:
    lines = file.read().strip().split('\n')

    grid = [list(line) for line in lines]

    return grid

def find_first_tile(grid: list[list[str]], symbol: str) -> tuple[int, int]:
    for r, row in enumerate(grid):
        if symbol in row: return (r, row.index(symbol))

def dijkstra(grid: list[list[str]], starts: list[tuple]) -> dict:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    distance = defaultdict(lambda: maxsize)
    pq = []

    for s in starts:
        position, direction = s
        heappush(pq, (0, position, direction))
        distance[(position, direction)] = 0

    while pq:
        score, position, direction = heappop(pq)
        r, c = position
        dr, dc = direction

        if distance[(position, direction)] < score: continue

        rx, cx = r + dr, c + dc
        if grid[rx][cx] != '#' and distance[((rx, cx), direction)] > score + 1:
            distance[((rx, cx), direction)] = score + 1
            heappush(pq, (score + 1, (rx, cx), direction))

        for turn in directions:
            if distance[(position, turn)] > score + 1000:
                distance[(position, turn)] = score + 1000
                heappush(pq, (score + 1000, position, turn))
    
    return distance

if __name__ == '__main__':
    main()
