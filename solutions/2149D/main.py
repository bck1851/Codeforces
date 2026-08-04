# https://codeforces.com/contest/2149/problem/D

from math import inf

def f(n,s):
    A = [[],[]]
    for idx,i in enumerate(s):
        A[ord(i) - 97].append(idx)
    res = inf
    for a in A:
        if not a: continue
        x = len(a)
        mid = x//2
        if x%2:
            med = a[mid]
            start = med - mid
            res = min(res, sum(abs(start + i - a[i]) for i in range(x)))
        else:
            med = (a[mid-1] + a[mid])//2
            start = med - mid + 1 
            res = min(res, sum(abs(start + i - a[i]) for i in range(x)))
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(f(n,s))
