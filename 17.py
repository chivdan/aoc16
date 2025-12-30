from collections import deque
import hashlib

def doors_open(s):
    h = hashlib.md5(s.encode()).hexdigest()[:4]
    return [c in "bcdef" for c in h]

passcode = "pvhmgsws"


def neighbors(x: int, y: int, moves: str):
    for allowed, move in zip(doors_open(passcode + moves), ["U", "D", "L", "R"]):
        if not allowed:
            continue
        if move == "U" and y > 0:
            yield (x, y - 1), move
        elif move == "D" and y < 3:
            yield (x, y + 1), move
        elif move == "L" and x > 0:
            yield (x - 1, y), move
        elif move == "R" and x < 3:
            yield (x + 1, y), move

def solve(part1: bool):
    q = deque([(0, 0, "")])
    max_len = 0
    while q:
        x, y, moves = q.popleft()
        if (x, y) == (3, 3):
            if part1:
                print(moves)
                return
            else:
                max_len = max(max_len, len(moves))
                continue

        for (nx, ny), move in neighbors(x, y, moves):
            q.append((nx, ny, moves + move))

    if not part1:
        print(max_len)


if __name__ == '__main__':
    solve(True)
    solve(False)
