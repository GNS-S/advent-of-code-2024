from part1 import parse_input, Parser

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        _, commands = parse_input(f)
        def run(A: int): return Parser({ 'A': A, 'B': 0, 'C': 0 }, commands, pointer=0).run()

        # Inspired by this recursive solution: https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2gge90
        Q = [(len(commands) -1, 0)]
        answer = None

        while Q and answer is None:
           cursor, A = Q.pop(0)
           for candidate in range(8):
              if run(A * 8 + candidate) == commands[cursor:]:
                 
                if cursor == 0: answer = A * 8 + candidate
                Q.append((cursor - 1, A * 8 + candidate))

        print(answer)
                 
if __name__ == '__main__':
    main()
