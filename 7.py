import re

abba = r".*([a-z])(?!\1)([a-z])\2\1.*"

aba = r"([a-z])(?!\1)([a-z])\1"

def solve(part1: bool):
    cnt = 0
    for line in open("input.txt"):
        line = line.strip()
        s = line
        brackets = re.findall("\[[a-z]+\]", line)
        for b in brackets:
            s = s.replace(b, "|")

        if part1:
            if not brackets or not any(re.search(abba, m) for m in brackets):
                m = re.search(abba, s)
                if m:
                    cnt += 1
        else:
            for i in range(len(s)):
                found = False
                for out in re.finditer(aba, s[i:]):
                    out = out.group()
                    bab = out[1] + out[2] + out[1]
                    if any(bab in b for b in brackets):
                        cnt += 1
                        found = True
                        break
                if found:
                    break


    print(cnt)



if __name__ == '__main__':
    solve(True)
    solve(False)
