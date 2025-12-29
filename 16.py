def solve(part1: bool):
    s = "00101000101111010"
    s = [c == "1" for c in s]

    L = 272 if part1 else 35651584

    while len(s) < L:
        s = s + [False] + [not c for c in reversed(s)]

    s = s[:L]
    
    ans = []
    while True:
        for i in range(0, len(s), 2):
            ans.append(not (s[i] ^ s[i + 1]))
        if len(ans) % 2 != 0:
            break
        s = ans
        ans = []
    print("".join([str(int(c)) for c in ans]))


if __name__ == '__main__':
    solve(True)
    solve(False)
