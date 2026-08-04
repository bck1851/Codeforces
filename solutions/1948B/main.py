# https://codeforces.com/contest/1948/problem/B

from functools import cache

def h(A):
    @cache
    def f(idx, pre):
        if idx == len(A):
            return True 
        res = False
        if A[idx] >= pre:
            res = f(idx+1, A[idx])
        elems = [int(i) for i in str(A[idx])]
        if A[idx] >= 10 and pre <= elems[0] <= elems[1]:
            res |= f(idx+1, elems[1])
        return res 
    return f(0,-1)

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    print("YES" if h(A) else "NO")
