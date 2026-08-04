# https://codeforces.com/contest/1931/problem/D

from collections import Counter

t = int(input())
for _ in range(t):
    n,x,y = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    res = 0 
    cnt = Counter()
    for i in A:
        dx = i%x 
        dy = i%y   
        if dx == 0:
            res += cnt[0, dy]
        else:
            res += cnt[x-dx, dy]
        cnt[dx,dy] += 1 
    print(res)
