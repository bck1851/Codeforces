# https://codeforces.com/contest/2229/problem/C1
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    res = list()
    for i in range(n):
        if i + 1 < n and A[i]*A[i+1] < 0 or A[i] > 0 and i == n - 1:
            res.append(i+1)
    print(len(res))
    if res: print(*res[::-1])
