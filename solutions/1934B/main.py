# https://codeforces.com/contest/1934/problem/B

from math import inf

A = [1,3,6,10,15]
lim = [2, 1, 4, 2]

def f(idx, tot, tar):
    if idx == len(lim):
        if tot > tar: return inf
        rem = tar - tot
        return inf if rem%15 else rem//15 
    res = inf 
    for i in range(lim[idx]+1):
        res = min(res, i + f(idx+1, tot + i*A[idx], tar))
    return res

t = int(input())
res = list()
for _ in range(t):
    n = int(input())
    res.append(f(0, 0, n))
    
for i in res:
    print(i)
