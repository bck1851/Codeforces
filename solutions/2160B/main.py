# https://codeforces.com/contest/2160/problem/B
 
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    res = [-1]*n
    elem = 1 
    for i in range(n):
        inc = A[i] - (0 if i == 0 else A[i-1])
        pre = i - inc
        if pre < 0:
            res[i] = elem 
            elem += 1 
        else:
            res[i] = res[pre]
    print(*res)
    
