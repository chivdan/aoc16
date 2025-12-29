import hashlib
import re
from collections import deque

def make_hash(s):
    return hashlib.md5(s.encode()).hexdigest()

def has_three(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]
    return None

def solve(part1: bool):
    salt = "ngcjuoqr" 

    hashes = deque()
    true_hashes = []
    key_ids = set()

    i = 0
    target = None
    nbad = 0
    while target is None or i <= target + 1000:
        h = f"{salt}{i}"
        if part1:
            h = make_hash(h)
        else:
            for _ in range(2017):
                h = make_hash(h)

        while hashes and i - hashes[0][1] > 1000:
            hashes.popleft()

        for five, k in hashes:
            if k in key_ids:
                continue
            if five in h:
                true_hashes.append((five, k))
                key_ids.add(k)
                if len(true_hashes) >= 64 and target is None:
                    target = sorted(t for _, t in true_hashes)[63]

        m = has_three(h)
        if m:
            char = m * 5
            hashes.append((char, i))
        i += 1
    true_hashes.sort(key=lambda x: x[1])
    print(true_hashes[63][1])

if __name__ == '__main__':
    solve(True)
    solve(False)
