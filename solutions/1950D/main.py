# https://codeforces.com/contest/1950/problem/D

from functools import cache

h = [[],[],[],[],[],[]]

def backtrack(idx, tar, res):
    if idx == tar:
        h[tar].append(res)
        return 
    for j in [0,1]:
        if idx == j == 0: continue
        backtrack(idx+1, tar, res*10 + j)
        
for i in range(1, 6):
    backtrack(0,i,0)

def f(n):
    @cache
    def y(n):
        if all(int(i) < 2 for i in str(n)):
            return True 
        res = False 
        for p in range(1,len(str(n))+1):
            for q in h[p]:
                if q != 1 and q != n and not n%q:
                    res |= y(n//q)
        return res
    return y(n)

t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if f(n) else "NO")
