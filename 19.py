class Node:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None


def solve(part1: bool):
    def remove(node):
        node.prev.next = node.next
        node.next.prev = node.prev

    n = 3014387

    if part1:
    
        start = Node(0)
        prev = start
        for i in range(1, n):
            node = Node(i)
            node.prev = prev
            prev.next = node
            prev = node

        node.next = start
        start.prev = node
        
        node = start
        cnt = n
        while cnt > 0:
            to_remove = node.next
            nxt = node.next.next
            remove(to_remove)
            node = nxt
            cnt -= 1

        print(node.num + 1)

        # alternative
        b = bin(n)[2:]
        l = int(b[1:], base=2)
        print(2 * l + 1)
    else:
        p = 3 
        while True:
            next_val = pow(3, p) 
            if next_val > n:
                break
            p += 1

        p = pow(3, p - 1)

        if p == n:
            print(p)
        if p < n < 2*p:
            print(n - p)
        if 2*p < n < 3*p:
            print(2*n - 3*p)

if __name__ == '__main__':
    solve(True)
    solve(False)
