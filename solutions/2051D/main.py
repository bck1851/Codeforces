# https://codeforces.com/contest/2051/problem/D

import bisect

t = int(input())
for _ in range(t):
    n,x,y = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()])
    res = 0
    tot = sum(A)
    for idx,i in enumerate(A):
        rem = tot - i  
        start = bisect.bisect_left(A, rem - y, hi = idx)
        end = bisect.bisect_right(A, rem - x, hi = idx)
        res += end - start
    print(res)
