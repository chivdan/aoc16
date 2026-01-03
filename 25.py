def solve(a_value: int):
    instructions = [line.strip().split() for line in open("input.txt")]

    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    reg['a'] = a_value
    cnt = 0   
 
    i = 0
    while i < len(instructions) and cnt < 20:
        cmd = instructions[i][0]
        args = instructions[i][1:]
        if cmd == 'cpy':
            if len(args) > 2 or not args[1].isalpha():
                i += 1
                continue
            if args[0].isalpha():
                reg[args[1]] = reg[args[0]]
            else:
                reg[args[1]] = int(args[0])
        elif cmd == 'inc':
            reg[args[0]] += 1
        elif cmd == 'dec':
            reg[args[0]] -= 1
        elif cmd == 'jnz':
            if len(args) > 2:
                i += 1
                continue
            if (args[0].isalpha() and reg[args[0]] != 0) or (not args[0].isalpha() and args[0] != '0'):
                steps = reg[args[1]] if args[1].isalpha() else int(args[1])
                i += steps
                continue
        elif cmd == "out":
            value = reg[args[0]] if args[0].isalpha() else args[0]
            if value != cnt % 2:
                return False
            cnt += 1
        i += 1

    return True


if __name__ == '__main__':
    a = 1
    while True:
        clock = solve(a)
        if clock:
            print(a)
            break
        a += 1
