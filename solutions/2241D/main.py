# https://codeforces.com/contest/2241/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    pre = 0 
    for i in range(n-1,-1,-1):
        A[i] += pre 
        pre = max(0, A[i] - B[i])
    print("YES" if pre == 0 else "NO")
