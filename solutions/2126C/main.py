# https://codeforces.com/contest/2126/problem/C

from bisect import bisect_left

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    start = A[k-1]
    A = sorted(set(A))
    n = len(A)
    idx = bisect_left(A, start)
    level = 1 
    ok = True 
    for j in range(idx, n-1):
        dif = A[j+1] - A[j]
        if level + dif - 1 > A[j]:
            ok = False 
            break
        level += dif 
    print("YES" if ok else "NO")
