def solve(part1: bool):
    forbidden = [[int(v) for v in line.strip().split("-")] for line in open("input.txt")]
    result = 0
    forbidden.sort()
    if part1:
        for (a, b) in forbidden:
            if a <= result <= b:
                result = b + 1
    else:
        result = 4294967295 + 1
        last_b = -1
        for (a, b) in forbidden:
            if b <= last_b:
                continue
            if last_b < a:
                result -= (b - a + 1)
            elif last_b == a:
                result -= (b - a)
            else:
                result -= (b - last_b)
            last_b = b
    print(result)


if __name__ == '__main__':
    solve(True)
    solve(False)
