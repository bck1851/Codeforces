# https://codeforces.com/contest/2027/problem/B

from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    res = inf
    for idx,i in enumerate(A):
        pre = i 
        delete = idx
        for j in range(idx+1, n):
            if A[j] > pre:
                delete += 1
        res = min(res, delete)
    print(res)
