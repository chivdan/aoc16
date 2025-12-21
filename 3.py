def possible(sides):
    s = {0, 1, 2}
    return all(sum(sides[i] for i in s.difference({j})) > sides[j] for j in range(3))
 

def solve(part1: bool):
    ans = 0
    if part1:
        for line in open("input.txt"):
            sides = [int(v) for v in line.strip().split()]
            if possible(sides):
                ans += 1
    else:
        data = [[int(v) for v in line.strip().split()] for line in open("input.txt")]
        for col in range(3):
            for i in range(0, len(data), 3):
                if possible([data[i][col], data[i + 1][col], data[i + 2][col]]):
                    ans += 1

    print(ans)

if __name__ == '__main__':
    solve(True)
    solve(False)
