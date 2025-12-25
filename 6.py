def solve(part1: bool):
    stats = [{chr(c): 0 for c in range(ord('a'), ord('z') + 1)} for _ in range(8)] 

    for line in open("input.txt"):
        for i, c in enumerate(line.strip()):
            stats[i][c] += 1

    foo = max if part1 else min
    
    ans = "".join([foo(stats[i].items(), key=lambda x: x[1])[0] for i in range(8)])
    print(ans)


if __name__ == '__main__':
    solve(True)
    solve(False)
