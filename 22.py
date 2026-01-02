import heapq

def neighbors(p):
    x, y = p
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if abs(dx) + abs(dy) > 1:
                continue
            if x + dx < 0 or x + dx > 30:
                continue
            if y + dy < 0 or y + dy > 30:
                continue
            yield (x + dx, y + dy)


def are_viable(n1, n2):
    p1, d1 = n1
    p2, d2 = n2
    if d1["used"] == 0:
        return False
    if d1["used"] <= d2["avail"]:
        return True
    return False

def dijkstra(start, nodes, zero_size):
    q = [(0, start)]
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0

    while q:
        d, p = heapq.heappop(q)
        if d > dist[p]:
            continue
        for n in neighbors(p):
            if nodes[n]["used"] <= zero_size:
                if d + 1 < dist[n]:
                    dist[n] = d + 1
                    heapq.heappush(q, (d + 1, n)) 

    return dist   
                                   
def solve(part1: bool):
    nodes = {}
    for line in open("input.txt"):
        if "dev" not in line:
            continue
        s = line.strip().split()
        xy = s[0]
        xy = xy.split("node-")[1]
        x, y = xy.split("-")
        x = int(x[1:])
        y = int(y[1:])

        size, used, avail = s[1], s[2], s[3]
        assert "T" in size and "T" in used and "T" in avail
        size = int(size[:-1])
        used = int(used[:-1])
        avail = int(avail[:-1])

        nodes[(x, y)] = {"size": size, "used": used, "avail": avail}

    viable = 0
    for n1 in nodes.items():
        for n2 in nodes.items():
            if n1 == n2:
                continue
            if are_viable(n1, n2):
                viable += 1
            
                
    if part1:
        print(viable)
        return

    zero_size = nodes[(13, 27)]["size"]
    dist_1 = dijkstra((13, 27), nodes, zero_size)
    moves_zero = dist_1[(29, 0)]
    dist_2 = dijkstra((29, 0), nodes, zero_size)
    moves_to_start = dist_2[(0, 0)] * 5 + 1

    print(moves_zero + moves_to_start)
        
            
if __name__ == '__main__':
    solve(True)
    solve(False)
