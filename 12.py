def solve(part1: bool):
    instructions = [line.strip().split() for line in open("input.txt")]

    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    if not part1:
        reg['c'] = 1
    
    i = 0
    while i < len(instructions):
        cmd = instructions[i][0]
        args = instructions[i][1:]
        if cmd == 'cpy':
            if args[0].isalpha():
                reg[args[1]] = reg[args[0]]
            else:
                reg[args[1]] = int(args[0])
        elif cmd == 'inc':
            reg[args[0]] += 1
        elif cmd == 'dec':
            reg[args[0]] -= 1
        elif cmd == 'jnz':
            if (args[0].isalpha() and reg[args[0]] != 0) or (not args[0].isalpha() and args[0] != '0'):
                i += int(args[1])
                continue
        i += 1
    print(reg['a'])


if __name__ == '__main__':
    solve(True)
    solve(False)
