import heapq

def wall(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y + 1358
    return bin(n)[2:].count('1') % 2 != 0

def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if abs(dx) + abs(dy) > 1:
                continue
            if x + dx < 0:
                continue
            if y + dy < 0:
                continue
            p = (x + dx, y + dy)
            if not wall(*p):
                yield p


def solve(part1: bool):
    p = 1, 1

    visited = set()
    q = [(0, p)]
    d = {}
    for x in range(200):
        for y in range(200):
            d[(x, y)] = float('inf')
    d[p] = 0

    while q:
        dist, p = heapq.heappop(q)
        if part1:
            if dist > d[p]:
                continue
        else:
            if dist > 50:
                continue
            visited.add(p)
        x, y = p
        
        for n in neighbors(x, y):
            if n not in d:
                continue
            if dist + 1 < d[n]:
                d[n] = dist + 1
                heapq.heappush(q, (dist + 1, n))

    if part1: 
        print(d[(31, 39)])
    else:
        print(len(visited))

if __name__ == '__main__':
    solve(True)
    solve(False)
