# https://codeforces.com/contest/2231/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    mn = 0 
    pre = A[0]
    for i in A[1:]:
        mn = max(mn, pre - i)
        pre = max(pre, i)
    for i in range(1, n):
        if A[i] < A[i-1]:
            A[i] += mn 
    res = all(A[i] >= A[i-1] for i in range(1,n))
    print("YES" if res else "NO")
