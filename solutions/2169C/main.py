# https://codeforces.com/contest/2169/problem/C

# tot + (l+r+2)*(r-l+1) - (acc[r] - acc(l-1))
# tot + (-ll+l-2l) + acc[l-1]
# tot + 2 + (rr + 3r - acc[r]) + (-ll - l + acc[l-1])

from itertools import accumulate
from math import inf

def f(n,A):
    acc = list(accumulate(A))
    res = acc[-1]
    mx = -inf
    for r in range(len(acc)):
        mx = max(mx, -r*r - r + (0 if r == 0 else acc[r-1]))
        res = max(res, acc[-1] + 2 + mx + r*r + 3*r - acc[r])
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    print(f(n,A))
