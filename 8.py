def solve():
    m = []
    for i in range(6):
        m.append([False] * 50)
    for line in open("input.txt"):
        if "rect" in line:
            b, a = [int(v) for v in line.strip().split()[1].split("x")]
            for i in range(a):
                for j in range(b):
                    m[i][j] = True

        elif "row" in line:
            s = line.strip().split()
            y = int(s[2].split("=")[1])
            d = int(s[-1])
            m[y] = [m[y][(i - d) % 50] for i in range(50)]
        elif "column" in line:
            s = line.strip().split()
            x = int(s[2].split("=")[1])
            d = int(s[-1])
            c = [m[(i - d) % 6][x] for i in range(6)]
            for i in range(6):
                m[i][x] = c[i]

    import numpy as np
    print(np.sum(m))
    for row in m:
        print("".join(["#" if c else "." for c in row]))


if __name__ == '__main__':
    solve()
