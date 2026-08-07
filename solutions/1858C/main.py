# https://codeforces.com/contest/1858/problem/C
t = int(input())
for _ in range(t):
    n = int(input())
    res = [0]*n
    used = [0]*(n+1)
    x = 0
    for i in range(1, n + 1):
        cur = i 
        if used[cur]: 
            continue
        for j in range(1, n+1):
            res[x] = cur
            x += 1 
            used[cur] = 1
            cur <<= 1 
            if cur > n or used[cur]: 
                break 
    print(*res)
