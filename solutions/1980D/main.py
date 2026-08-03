from math import gcd
from math import inf
 
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    if n == 1:
        print("YES")
        continue
    forw, back = [False]*n, [False]*n
    forw[0] = back[-1] = True
    pre = 0 
    for i in range(1,n):
        g = gcd(A[i], A[i-1])
        if g < pre: break 
        forw[i] = True
        pre = g 
    pre = inf
    for i in range(n-2,-1,-1):
        g = gcd(A[i], A[i+1])
        if g > pre: break 
        back[i] = True 
        pre = g 
    ok = forw[-2] or back[1]
    for i in range(1,n-1):
        if ok: 
            break
        g = gcd(A[i-1], A[i+1])
        if not forw[i-1] or not back[i+1]:
            continue 
        x = 0 if i - 2 < 0 else gcd(A[i-2],A[i-1])
        y = inf if i + 2 >= n else gcd(A[i+1], A[i+2])
        if x <= g <= y: 
            ok = True 
    print("Yes" if ok else "No")
