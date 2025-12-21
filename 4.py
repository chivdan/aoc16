def solve(part1: bool):
    ans = 0
    for line in open("input.txt"):
        lhs, rhs = line.strip().split("[")
        checksum = rhs[:-1]
        s = lhs.split("-")
        sid = int(s[-1])
        text = "".join(s[:-1])
        if part1:
            counts = {c: text.count(c) for c in set(text)}
            five_lead = sorted(counts.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
            five_lead = "".join([v[0] for v in five_lead[:5]])
            if five_lead == checksum:
                ans += sid 
        else:
            encoded = ""
            for c in text:
                x = ord(c) + sid % 26
                encoded += chr(min(x, x - ord('z') + ord('a') - 1))
            if "northpoleobjects" in encoded:
                print(sid)
    if part1:        
        print(ans)

if __name__ == '__main__':
    solve(True)
    solve(False)
