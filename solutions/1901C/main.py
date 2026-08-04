# https://codeforces.com/contest/1901/problem/C

from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    ok = all(A[i] == A[i-1] for i in range(1,n))
    res = list()
    while not ok:
        mn1 = mn2 = inf 
        mx1 = mx2 = 0
        for i in A:
            mn1 = min(mn1, i>>1)
            mx1 = max(mx1, i>>1)
            mn2 = min(mn2, (i+1)>>1)
            mx2 = max(mx2, (i+1)>>1)
        res.append(0 if mx1 - mn1 <= mx2 - mn2 else 1)
        yes = mx2 - mn2 < mx1 - mn1
        for i in range(n):
            if yes: A[i] += 1 
            A[i] >>= 1
        ok = all(A[i] == A[i-1] for i in range(1,n))
    print(len(res))
    if len(res) <= n:
        print(*res)
