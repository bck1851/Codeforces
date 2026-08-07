# https://codeforces.com/problemset/problem/1927/E
t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    res = [0]*n 
    cur = 1 
    for i in range(0,k,2):
        for j in range(i, n, k):
            res[j] = cur 
            cur += 1 
    cur = n 
    for i in range(1,k,2):
        for j in range(i, n, k):
            res[j] = cur 
            cur -= 1 
    print(*res)
