# https://codeforces.com/contest/1922/problem/C

from math import inf

mx = 10**5
forward = [0]*mx
backward = [0]*mx
ans = list()

def f(A,Q,n):
    for i in range(n):
        forward[i] = backward[i] = 0
    for i in range(n-1):
        x = (A[i] - A[i-1]) if i > 0 else inf
        y = A[i+1] - A[i]
        forward[i+1] = forward[i] +(1 if y < x else y)  
    for i in range(n-1,0,-1):
        x = (A[i+1] - A[i]) if i+1 < n else inf 
        y = A[i] - A[i-1]
        backward[i-1] = backward[i] + (1 if y < x else y)
    for i,j in Q:
        if i < j:
            ans.append(forward[j-1] - forward[i-1])
        else:
            ans.append(backward[j-1] - backward[i-1])

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    q = int(input())
    Q = []
    for _ in range(q):
        Q.append([int(i) for i in input().split()])
    f(A,Q,n)
    
for x in ans:
    print(x)
    
