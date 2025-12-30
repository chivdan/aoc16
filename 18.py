def solve(part1: bool):
    cur = [True if c == '^' else False for c in open("input.txt").read().strip()]
    N = len(cur)
    cur = [False] + cur + [False]
    ans = N - sum(cur)

    nrows = 40 if part1 else 400000

    for k in range(nrows - 1):
        nxt = [False] + [cur[i - 1] ^ cur[i + 1] for i in range(1, N + 1)] + [False]
        ans += N - sum(nxt)
        cur = nxt
    print(ans)

if __name__ == '__main__':
    solve(True)
    solve(False)
