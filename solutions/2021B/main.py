# https://codeforces.com/contest/2021/problem/B

from collections import Counter

t = int(input())
for _ in range(t):
    n,x = [int(i) for i in input().split()]
    cnt = Counter([int(i) for i in input().split()])
    mex = 0 
    for i in range(2*(10**5)+2):
        cnt[i] += max(0, cnt[i-x] - 1)
        if cnt[i]:
            mex += 1 
        else:
            break
    print(mex)
