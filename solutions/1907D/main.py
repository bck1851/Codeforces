# https://codeforces.com/contest/1907/problem/D

def f(lim, A):
    cur = 0 
    mn = mx = 0 
    for i in range(n):
        l,r = A[i]
        if mx + lim < l or mn - lim > r:
            return False 
        mn = max(mn-lim, l)
        mx = min(mx+lim, r)
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    A = []
    for _ in range(n):
        a = [int(i) for i in input().split()]
        A.append(a)
    left, right = 0, 10**9 
    while left < right:
        mid = (left + right)//2
        if f(mid, A):
            right = mid 
        else:
            left = mid + 1 
    print(left)
