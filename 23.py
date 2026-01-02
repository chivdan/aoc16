def solve(part1: bool):
    instructions = [line.strip().split() for line in open("input.txt")]

    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    reg['a'] = 7 if part1 else 12
    
    i = 0
    while i < len(instructions):
        cmd = instructions[i][0]
        args = instructions[i][1:]
        if i + 5 < len(instructions):
            ins = instructions[i:i + 6]

            if (ins[0][0] == 'cpy' and
                ins[1][0] == 'inc' and
                ins[2][0] == 'dec' and
                ins[3] == ['jnz', ins[2][1], '-2'] and
                ins[4][0] == 'dec' and
                ins[5] == ['jnz', ins[4][1], '-5']):

                X = ins[0][1]
                Y = ins[0][2]
                A = ins[1][1]
                Z = ins[4][1]

                xval = reg[X] if X.isalpha() else int(X)

                reg[A] += xval * reg[Z]
                reg[Y] = 0
                reg[Z] = 0

                i += 6
                continue

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
        elif cmd == 'tgl':
            if len(args) > 1:
                i += 1
                continue
            if args[0].isalpha():
                pos = reg[args[0]]
            else:
                pos = int(args[0])
            if i + pos < 0 or i + pos >= len(instructions):
                i += 1    
                continue
            if len(instructions[i + pos]) == 2:
                if instructions[i + pos][0] == "inc":
                    instructions[i + pos][0] = "dec"
                else:
                    instructions[i + pos][0] = "inc"
            elif len(instructions[i + pos]) == 3:
                if instructions[i + pos][0] == "jnz":
                    instructions[i + pos][0] = "cpy"
                else:
                    instructions[i + pos][0] = "jnz"
        i += 1
    print(reg['a'])


if __name__ == '__main__':
    solve(True)
    solve(False)
