# https://codeforces.com/contest/2124/problem/B
from math import inf
from itertools import accumulate

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    min_A = [i for i in A]
    for i in range(1, n):
        min_A[i] = min(min_A[i-1], A[i])
    acc = list(accumulate(min_A))
    res = sum(min_A)
    for i in range(n-1):
        pre = inf if i == 0 else min_A[i-1]
        pre_tot = acc[i-1] if i > 0 else 0
        res = min(res, pre_tot + min(pre, A[i] + A[i+1]))
    print(res)
