#https://codeforces.com/contest/2123/problem/E
from itertools import accumulate
 
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    mx = max(A)
    cnt = [0]*(mx+2)
    for i in A: 
        cnt[i] += 1 
    arr = [0]*(n+1)
    for i in range(mx+2):
        start = cnt[i]
        end = n - i
        arr[start] += 1 
        if end + 1 < len(arr):
            arr[end+1] -= 1 
        if not cnt[i]:
            break
    arr = list(accumulate(arr))
    print(*arr)
