# https://codeforces.com/contest/2175/problem/B
t = int(input())
for _ in range(t):
    n,l,r = [int(i) for i in input().split()]
    l,r = l-1, r-1
    xor = [0]*n
    for i in range(n):
        xor[i] = i+1 if i != r else xor[l-1] if l > 0 else 0
    res = [1 if i == 0 else xor[i]^xor[i-1] for i in range(n)]
    print(*res)
