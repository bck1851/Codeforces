# https://codeforces.com/contest/2136/problem/B
from collections import deque

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    s = [int(i) for i in input()]
    one = 0 
    ok = 1
    for i in s:
        one = one + 1 if i == 1 else 0
        if one == k:
            ok = False 
            break
    print("NO" if not ok else "YES")
    if ok == 1:
        q = deque(list(range(1, n+1)))
        res = list()
        for i in s:
            res.append(q.pop() if i == 0 else q.popleft())
        print(*res)
