# https://codeforces.com/contest/1870/problem/B

t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()]) 
    B = sorted([int(i) for i in input().split()]) 
    a = 0 
    for i in B: a |= i 
    mn = 0 
    for i in A: mn ^= (i | a)
    mx = 0 
    for i in A: mx ^= i 
    print(min(mn,mx), max(mn,mx))
