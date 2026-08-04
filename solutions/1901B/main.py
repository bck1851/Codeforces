# https://codeforces.com/contest/1901/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    res = 0 
    pre = 0 
    for i in A:
        res += max(i-pre,0)
        pre = i 
    print(res - 1)
