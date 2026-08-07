# https://codeforces.com/contest/2185/problem/C
t = int(input())
for _ in range(t):
    n = input()
    A = sorted(set([int(i) for i in input().split()]))
    cur = 1
    res = 1
    for i in range(1, len(A)):
        cur = 1 if A[i] != A[i-1] + 1 else cur + 1
        res = max(res, cur)
    print(res)
