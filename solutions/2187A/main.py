#https://codeforces.com/contest/2187/problem/A
from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    sA = sorted(A)
    ans = -1 
    mn, mx = sA[0], sA[-1]
    for i,j in zip(A, sA):
        if i == j: continue 
        t = max(mx-i, i-mn)
        ans = t if ans == -1 else min(ans, t)
    print(ans)
