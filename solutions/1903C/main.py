# https://codeforces.com/contest/1903/problem/C

from itertools import accumulate

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    acc = list(accumulate(A[::-1]))[::-1]
    res = A[0]
    cur = 1 
    for i in range(1, n):
        if acc[i] > 0:
            cur += 1 
        res += A[i]*cur 
    print(res)
