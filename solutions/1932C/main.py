# https://codeforces.com/problemset/problem/1932/C

t = int(input())
for _ in range(t):
    n,m= [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    s = input()
    l,r = 0, n-1 
    for i in s:
        if i == 'L':
            l += 1 
        else:
            r -= 1 
    c = 1 
    res = list()
    for i in reversed(s):
        if i == 'L':
            l -= 1 
            c = c*A[l]
        else:
            r += 1 
            c = c*A[r]
        c %= m
        res.append(c)
    print(*res[::-1])
        
