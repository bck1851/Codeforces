# https://codeforces.com/contest/2072/problem/C

t = int(input())
for _ in range(t):
    n, x = [int(i) for i in input().split()]
    res = list()
    OR = 0 
    for i in range(n-1):
        if i & (~x):
            break 
        OR |= i 
        res.append(i)
    if len(res) < n - 1:
        res += [x]*(n - len(res))
        print(*res)
    else:
        if (n-1) & (~x) or OR | (n-1) != x:
            res.append(x)
        else:
            res.append(n-1)
        print(*res)
        
    
