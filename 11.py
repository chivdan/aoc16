import copy
import itertools
from functools import cache


def can_move(objs, floor_objs):
    s = objs + floor_objs
    return floor_ok(s)

def can_remove(objs, floor_objs):
    s = floor_objs[:]
    for obj in objs:
        s.remove(obj)
    return floor_ok(s)

def floor_ok(s):
    for obj1 in s:
        if "chip" in obj1:
            chip_type = obj1.split()[0]
            if any("generator" in obj2 and chip_type in obj2 for obj2 in s):
                continue
            # if there is a generator of another type, and no generator of chip_type -- fried
            if any("generator" in obj2 and chip_type not in obj2 for obj2 in s):
                return False
    return True


def canonical(state, floor):
    pos = {}
    for f in range(len(state)):
        for obj in state[f]:
            elem, kind = obj.split()
            if elem not in pos:
                pos[elem] = [None, None]
            if kind == "microchip":
                pos[elem][0] = f
            else:
                pos[elem][1] = f
    pairs = tuple(sorted(tuple(v) for v in pos.values()))
    return (floor, pairs)


def solve(part1: bool):
    state = []
    cnt = 0
    for line in open("input.txt"):
        if len(state) == 3:
            break
        s = line.strip().split()[5:]
        if "and" in s:
            s.remove("and")
        for i in range(len(s)):
            s[i] = s[i].replace("-compatible", "")
        i = 0
        floor = []
        while i < len(s):
            floor.append(s[i] + " " + s[i + 1].replace(".", "").replace(",", ""))
            cnt += 1
            i += 3
        state.append(floor)

    state.append([])
    
    if not part1:
        state[0].append('elerium generator')
        state[0].append('elerium microchip')
        state[0].append('dilithium generator')
        state[0].append('dilithium microchip')

    result = 1e10
    from collections import deque
    q = deque([(state, 0, 0)])
    visited = set()
    while q:
        state, floor, n = q.popleft()
        if not state[floor]:
            continue
        if n >= result:
            continue
        rep = canonical(state, floor)
        if rep in visited:
            continue
        visited.add(rep)

        if all(len(state[i]) == 0 for i in range(3)):
            result = min(result, n)
            continue

        if result < 1e10 and n >= result - 1:
            continue
        if result < 1e10 and n - result > cnt - len(state[-1]):
            continue

        other_floors = []
        if floor == 0:
            other_floors = [floor + 1]
        elif floor == 3:
            other_floors = [floor - 1]
        else:
            other_floors = [floor - 1, floor + 1]
        
        for other in other_floors:
            if other < floor:
                if all(len(state[i]) == 0 for i in range(floor)):
                    continue
            # move pairs
            for it in itertools.combinations(state[floor], 2):
                o1, o2 = it
                if can_move([o1, o2], state[other]) and can_remove([o1, o2], state[floor]):
                    s = [list(f) for f in state]

                    s[floor].remove(o1)
                    s[floor].remove(o2)
                    s[other].extend([o1, o2])
                    if canonical(s, other) in visited:
                        continue
                    q.append((s, other, n + 1))
            # move 1
            for obj in state[floor]:
                if can_move([obj], state[other]) and can_remove([obj], state[floor]):
                    s = [list(f) for f in state]

                    s[floor].remove(obj)
                    s[other].append(obj)
                    if canonical(s, other) in visited:
                        continue
                    q.append((s, other, n + 1))
    print(result)

if __name__ == '__main__':
    solve(True)
    solve(False)
