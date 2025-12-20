def solve(part1: bool):
    instructions = open("input.txt").read().split(", ")
    
    y, x = 0, 0
    d = 'N'

    turn = {('N', 'L'): 'W',
            ('N', 'R'): 'E',
            ('W', 'L'): 'S',
            ('W', 'R'): 'N',
            ('S', 'L'): 'E',
            ('S', 'R'): 'W',
            ('E', 'L'): 'N',
            ('E', 'R'): 'S'
            }

    visited = {(y, x)}
    
    for instr in instructions:
        lr = instr[0]
        dist = int(instr[1:])
        d = turn[(d, lr)]
   
        coords = []

        if d == 'N':
            coords = [(yy, x) for yy in range(y - 1, y - dist - 1, -1)]
            y -= dist
        elif d == 'S':
            coords = [(yy, x) for yy in range(y + 1, y + dist + 1)]
            y += dist
        elif d == 'W':
            coords = [(y, xx) for xx in range(x - 1, x - dist - 1, -1)]
            x -= dist
        elif d == 'E':
            coords = [(y, xx) for xx in range(x + 1, x + dist + 1)]
            x += dist

        if not part1:
            for (yy, xx) in coords:
                if (yy, xx) in visited:
                    return abs(yy) + abs(xx)
                visited.add((yy, xx))

    return abs(x) + abs(y)

if __name__ == '__main__':
    print(solve(True))
    print(solve(False))
