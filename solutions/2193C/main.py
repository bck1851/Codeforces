# https://codeforces.com/contest/2193/problem/C
from itertools import accumulate

t = int(input())
for _ in range(t):
    n,q = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    Q = list()
    for _ in range(q):
        l,r = [int(i) for i in input().split()]
        Q.append([l-1, r-1])
    for i in range(n-1, -1, -1):
        if i + 1 < n:
            A[i] = max(A[i], A[i+1])
        A[i] = max(A[i], B[i])
    A = list(accumulate(A))
    res = list()
    for l,r in Q:
        cur = A[r] - (0 if l == 0 else A[l-1])
        res.append(cur)
    print(*res)
