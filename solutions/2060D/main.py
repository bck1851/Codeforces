# https://codeforces.com/contest/2060/problem/D

 
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    inc = [False]*(n-1) + [True] 
    for i in range(n-2,-1,-1):
        if A[i] > A[i+1]:
            break 
        inc[i] = True 
    for i in range(n-1):
        if inc[i]: break 
        a,b = A[i], A[i+1]
        A[i] -= min(a,b)
        A[i+1] -= min(a,b)
    res = all(A[i] >= A[i-1] for i in range(1,n))
    print("YES" if res else "NO")
