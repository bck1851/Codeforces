# https://codeforces.com/contest/2184/problem/C
 
from functools import cache
from math import inf

def f(n,k):
    @cache
    def y(cur):
        if cur <= k:
            return inf if cur < k else 0 
        a = cur//2 
        b = cur - a 
        return 1 + min(y(a),y(b))
    return y(n) if y(n) != inf else -1
    
t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    print(f(n,k))
