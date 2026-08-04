# https://codeforces.com/contest/2111/problem/C
 
from math import inf

def f(A):
    n = len(A)
    start = [-1]*n 
    pre_idx = pre_elem = -1 
    for idx,i in enumerate(A):
        if i != pre_elem:
            pre_idx = idx 
            pre_elem = i 
        start[idx] = pre_idx
    return start

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    start = f(A)
    end = [n-i-1 for i in f(A[::-1])[::-1]]
    res = inf 
    for i in range(n):
        s, e = start[i], end[i]
        tot = (s-1)*A[i] + (n-e)*A[i]
        res = min(res, tot)
    print(res)
