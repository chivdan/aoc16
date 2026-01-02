def solve(part1: bool):
    #pwd = "abcdefgh" if part1 else "fbgdceah"
    pwd = "dgfaehcb"
    s = [c for c in pwd]

    instructions = [line.strip() for line in open("input.txt")]

    if not part1:
        instructions = reversed(instructions)

    for line in instructions:
        cmd = line.strip().split()

        if "swap position" in line:
            i, j = int(cmd[2]), int(cmd[5])
            s[i], s[j] = s[j], s[i]
        elif "swap letter" in line:
            a, b = cmd[2], cmd[5]

            for i in range(len(s)):
                if s[i] == a:
                    s[i] = b
                elif s[i] == b:
                    s[i] = a
        elif "rotate left" in line:
            steps = int(cmd[2])
            if not part1:
                steps = -steps
            s = [s[(i + steps) % len(s)] for i in range(len(s))]
        elif "rotate right" in line:
            steps = int(cmd[2])
            if not part1:
                steps = -steps
            s = [s[(i - steps) % len(s)] for i in range(len(s))]
        elif "rotate based on position" in line:
            letter = cmd[-1]
            index = s.index(letter)
            steps = 1 + index + (1 if index >= 4 else 0)
            if not part1:
                steps = -steps
            s = [s[(i - steps) % len(s)] for i in range(len(s))]
        elif "reverse" in line:
            i, j = int(cmd[2]), int(cmd[4])
            s = s[:i] + list(reversed(s[i:j + 1])) + s[j + 1:]
        elif "move" in line:
            i, j = int(cmd[2]), int(cmd[5])
            if not part1:
                i, j = j, i
            letter = s.pop(i)
            s.insert(j, letter)

    print("".join(s))

if __name__ == '__main__':
    #solve(True)
    solve(False)
