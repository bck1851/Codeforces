# https://codeforces.com/contest/2218/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    res = 0
    t = dict()
    start = max(A).bit_length()
    
    def add(num):
        tmp = t 
        for i in range(start, -1, -1):
            bit = (num >> i)&1 
            if bit not in tmp:
                tmp[bit] = dict()
            tmp = tmp[bit]
    
    def query(num):
        tmp = t
        res = 0 
        for i in range(start, -1, -1):
            res *= 2 
            bit = (num >> i)&1
            res += 1 if bit^1 in tmp else 0 
            tmp = tmp[bit^1 if bit^1 in tmp else bit^0]
        return res
    
    for i in A:
        add(i)
        res = max(res, query(i))
    print(res)
