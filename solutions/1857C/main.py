# https://codeforces.com/contest/1857/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted([int(i) for i in input().split()]) 
    m = len(A)
    res = list()
    ptr = m - 1 
    cur = 1 
    while ptr >= 0:
        res.append(A[ptr])
        ptr -= cur 
        cur += 1 
    res.append(res[0])
    print(*res)   
