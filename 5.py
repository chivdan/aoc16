import hashlib

def solve(part1: bool):
    inp = open("input.txt").read().strip()
    
    if part1: 
        pwd = ""
    else:
        pwd = [None] * 8
    filled = 0
    i = 0
    while True:
        h = hashlib.md5((inp + str(i)).encode()).hexdigest()
        if h.startswith("00000"):
            if part1:
                pwd += h[5]
            else:
                pos = h[5]
                if '0' <= pos <= '7':
                    pos = int(pos)
                    if pwd[pos] is None:
                        pwd[pos] = h[6]
                        filled += 1
        if filled == 8:
            break
        i += 1
    if part1:
        print(pwd)
    else:
        print("".join(pwd))




if __name__ == '__main__':
    solve(True)
    solve(False)
