# https://codeforces.com/contest/1899/problem/B

from itertools import accumulate
from math import inf
        
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(accumulate([int(i) for i in input().split()]))
    res = 0
    for i in range(1, n+1):
        if n%i: continue
        mx = -1
        mn = inf
        for j in range(i-1,n,i):
            acc = A[j] - (A[j-i] if j - i >= 0 else 0)
            mx = max(mx, acc)
            mn = min(mn, acc)
        res = max(res, mx - mn)
    print(res)
