# https://codeforces.com/contest/2193/problem/D

import bisect
from itertools import accumulate

t = int(input())
for _ in range(t):
    n = int(input())
    B = sorted([int(i) for i in input().split()])
    A = list(accumulate([int(i) for i in input().split()]))
    res = 0
    for idx,i in enumerate(B):
        swords = n - idx
        defeat = bisect.bisect_right(A, swords)
        res = max(res, i*defeat)
    print(res)
