# https://codeforces.com/problemset/problem/2032/C
import bisect
 
t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted([int(i) for i in input().split()])
    res = n 
    for idx in range(n-2):
        i = A[idx]
        j = bisect.bisect_left(A, i + i)
        dif = i != A[idx+1]
        res = min(res, idx + n - j + dif)
        j = bisect.bisect_left(A, i + A[idx+1])
        res = min(res, idx + n - j)
    print(res)
