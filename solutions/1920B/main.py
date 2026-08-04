# https://codeforces.com/contest/1920/problem/B

from math import gcd,inf
from itertools import accumulate

t = int(input())
for _ in range(t):
    n,k,x = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()], reverse = True)
    A = list(accumulate(A))
    res = -inf
    for i in range(k+1):
        a = A[i-1] if i > 0 else 0 
        b = (A[n-1] if i+x-1 >= n else A[i+x-1]) - (A[i-1] if i > 0 else 0)
        res = max(res, A[-1] - a -2*b)
    print(res)
