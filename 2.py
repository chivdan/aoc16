def solve(part1: bool):
    if part1:
        keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    else:
        keypad = [[None, None, 1, None, None],
                  [None, 2, 3, 4, None],
                  [5, 6, 7, 8, 9],
                  [None, "A", "B", "C", None],
                  [None, None, "D", None, None]]

    code = ""

    for line in open("input.txt"):
        if part1:
            y, x = 1, 1
        else:
            y, x, = 2, 0

        for c in line.strip():
            if c == "L":
                if x > 0 and keypad[y][x - 1] is not None:
                    x -= 1
            elif c == "R":
                if x < len(keypad[y]) - 1 and keypad[y][x + 1] is not None:
                    x += 1
            elif c == "U":
                if y > 0 and keypad[y - 1][x] is not None:
                    y -= 1
            elif c == "D":
                if y < len(keypad) - 1 and keypad[y + 1][x] is not None:
                    y += 1
        code += str(keypad[y][x])
    print(code)


if __name__ == '__main__':
    solve(True)
    solve(False)
