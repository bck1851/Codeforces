# https://codeforces.com/contest/1889/problem/A

from collections import deque

def f(s,n):
    s = deque(list(s))
    res = list()
    x = 0
    while s and len(res) <= 300:
        if s[0] != s[-1]:
            s.pop()
            s.popleft()
        elif s[0] == 0:
            res.append(len(s)+x)
            s.append(0)
            s.popleft()
        else:
            res.append(x)
            s.appendleft(1)
            s.pop()
        x += 1 
    return [res, 1] if len(res) <= 300 else [[],0] 

t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(i) for i in input()]
    if n%2 == 1:
        print(-1)
        continue 
    res, ok = f(s,n)
    if not ok:
        print(-1)
    else:
        print(len(res))
        print(*res)
