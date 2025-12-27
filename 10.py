def solve(part1: bool):
    bots = {}
    outputs = {}

    def give(bot, value, to_output):
        d = outputs if to_output else bots
        if bot in d:
            d[bot].append(value)
            d[bot].sort()
        else:
            d[bot] = [value]

    instructions = []

    for line in open("input.txt"):
        line = line.strip()
        s = line.split()
        if "value" in line:
            value = int(s[1])
            dst = int(s[-1])
            give(dst, value, False)
        elif "gives" in line:
            src = int(s[1])
            output_low = s[5] == "output"
            low_dst = int(s[6])
            output_high = s[-2] == "output"
            high_dst = int(s[-1])
            instructions.append((src, output_low, low_dst, output_high, high_dst))

    found = False
    while instructions and not found:
        for i, (src, low_out, low, high_out, high) in enumerate(instructions):
            if src in bots and len(bots[src]) == 2:
                give(low, bots[src][0], low_out)
                give(high, bots[src][1], high_out)
                bots[src] = []
                instructions.pop(i)
                break

        if part1:
            for b in bots:
                if len(bots[b]) == 2 and bots[b][0] == 17 and bots[b][1] == 61:
                    print(b)
                    found = True
                    break

    if not part1:
        print(outputs[0][0] * outputs[1][0] * outputs[2][0])

if __name__ == '__main__':
    solve(True)
    solve(False)
