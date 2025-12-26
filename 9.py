import re
from functools import cache

mult = r"\(([0-9]+)x([0-9]+)\)"
marker = re.compile(mult)

def decompress(s):
    m = re.search(mult, s)
    a, b = int(m.group(1)), int(m.group(2))
    begin, end = m.span()
    lsuff = a * b
    return lsuff, a + len(m.group())

def decompress2(s, start=0, end=None):
    if end is None:
        end = len(s)

    l = 0
    i = start
    while i < end:
        if s[i] == "(":
            m = marker.match(s, i)
            a, b = int(m.group(1)), int(m.group(2))

            sub_start = m.end()
            sub_end = m.end() + a

            chunk_len = decompress2(s, m.end(), m.end() + a)

            l += chunk_len * b
            i = m.end() + a
        else:
            l += 1
            i += 1
    return l


def solve(part1: bool):

    n = 0
    for s in open("input.txt"):
        s = s.strip()
        i = 0
        if part1:
            ans = 0 
            while i < len(s):
                if s[i] == "(":
                    lsuff, di = decompress(s[i:])
                    ans += lsuff
                    i += di
                else:
                    ans += 1
                    i += 1
            n += ans
        else:
            ans = decompress2(s)
            n += ans

    print(n)



if __name__ == '__main__':
    #solve(True)
    solve(False)
