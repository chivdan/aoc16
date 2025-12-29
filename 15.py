def fall(disc, t):
    for i in range(len(disc)):
        npos, start = disc[i]
        pos = (start + t + i + 1) % npos
        assert pos < npos
        if pos != 0:
            return False
    return True


def solve(part1: bool):
    disc = []
    for line in open("input.txt"):
        s = line.strip().split()
        npos = int(s[3])
        pos = int(s[-1].replace(".", ""))

        disc.append((npos, pos))

    if not part1:
        disc.append((11, 0))

    t = 0
    while True:
        if fall(disc, t):
            print(t)
            return
        t += 1

if __name__ == '__main__':
    solve(True)
    solve(False)
