import heapq
import itertools
from functools import cache

def dijkstra(start, nodes, m):
    def neighbors(p, m):
        x, y = p
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                if abs(dx) + abs(dy) > 1:
                    continue
                if x + dx < 0 or x + dx >= len(m[y]):
                    continue
                if y + dy < 0 or y + dy >= len(m):
                    continue
                if m[y + dy][x + dx] == -1:
                    continue
                yield x + dx, y + dy

    q = [(0, start)]
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0

    while q:
        d, p = heapq.heappop(q)
        if d > dist[p]:
            continue
        for n in neighbors(p, m):
            if d + 1 < dist[n]:
                dist[n] = d + 1
                heapq.heappush(q, (d + 1, n)) 
    return dist

    
def solve(part1: bool):
    @cache
    def cost(n1, n2):
        dist = dijkstra(n1, nodes, m)
        return dist[n2]
    
    def path_cost(ordered_targets):
        return sum(cost(n1, n2) for n1, n2 in itertools.pairwise(ordered_targets))

    m = []
    targets = []
    nodes = []
    for line in open("input.txt"):
        row = []
        for i, c in enumerate(line.strip()):
            if c == "#":
                row.append(-1)
            elif c == ".":
                row.append(0)
                nodes.append((i, len(m)))
            else:
                row.append(0)
                targets.append((c, i, len(m)))
                nodes.append((i, len(m)))
        m.append(row)

    targets.sort()
    targets = [(u, v) for (n, u, v) in targets]

    min_cost = 1e10
    for it in itertools.permutations(targets[1:]):
        order = [targets[0]] + list(it)
        if not part1:
            order.append(targets[0])
        c = path_cost(order)
        min_cost = min(c, min_cost)

    print(min_cost)
    

if __name__ == '__main__':
    solve(True)
    solve(False)
