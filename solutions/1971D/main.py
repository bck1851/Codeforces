# https://codeforces.com/contest/1971/problem/D

from functools import cache

def f(s):
    n = len(s)
    @cache
    def y(idx, pre, d):
        limit = -1 if d == -1 else n 
        if idx == limit:
            return 0 
        turn = int(pre != s[idx])
        return turn + y(idx+d, s[idx], d)
    
    res = n 
    for i in range(n):
        a = y(i, s[i], -1) + 1 
        b = (y(i+1, s[i+1], 1) + 1) if i + 1 < n else 0 
        res = min(res, a + b)
        j = i
        while j < n and s[j] == '0':
            j += 1 
        while j < n and s[j] == '1':
            j += 1 
        a = (1 + y(i-1, s[i-1], -1)) if i > 0 else 0 
        b = (1 + y(j, s[j], 1)) if j < n else 0 
        res = min(res, a + b + 1)
        
    return res
    
t = int(input())
for _ in range(t):
    s = input()
    print(f(s))
