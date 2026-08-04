#https://codeforces.com/contest/1870/problem/C

import sys

def f(A,n,k):
    sA = sorted(enumerate(A), key = lambda x: -x[1])
    setA = set(A)
    ptr, mn, mx = 0, n, -1 
    res = list()
    for i in range(k, 0, -1):
        while ptr < n and sA[ptr][1] >= i:
            x = sA[ptr][0]
            if x < mn: mn = x
            if x > mx: mx = x
            ptr += 1 
        res.append(2*(mx - mn + 1)*(i in setA))
    return reversed(res)

t = int(input())
ans = list()
for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans.append(" ".join(map(str, f(A,n,k))))

sys.stdout.write("\n".join(ans))
  
