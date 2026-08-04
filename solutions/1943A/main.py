# https://codeforces.com/contest/1943/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    mx = max(A)
    cnt = [0]*(mx+2)
    for i in A:
        cnt[i] += 1 
    mex = 0 
    ones = 0 
    for i in range(mx+1):
        if not cnt[i]:
            break 
        if cnt[i] == 1:
            ones += 1 
        if ones > 1:
            break 
        mex  = i + 1
    print(mex)
