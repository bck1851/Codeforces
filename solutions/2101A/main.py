# https://codeforces.com/contest/2101/problem/A

def f(n):
    d = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}
    arr = [[-1]*n for _ in range(n)]
    cur = n*n -1 
    i = j = 0
    arr[i][j] = cur
    cur -= 1
    di, dj = 0, 1 
    while cur >= 0:
        if i + di >= n or j + dj >= n or arr[i+di][j+dj] != -1:
            di, dj = d[(di, dj)]
            continue 
        i,j = i+di, j+dj 
        arr[i][j] = cur 
        cur -= 1 
    return arr

t = int(input())
for _ in range(t):
    n = int(input())
    arr = f(n)
    for i in arr:
        print(*i)
