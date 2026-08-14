# https://codeforces.com/problemset/problem/1790/C
t = int(input())
for _ in range(t):
    n = int(input())
    A = list()
    for _ in range(n):
        A.append([int(i) for i in input().split()])
    s0 = set(A[0])
    start = -1 
    for i in range(1, n+1):
        if i not in s0:
            start = i 
            break 
    idx_map = [0]*(n+1)
    for idx,i in enumerate(A[0]):
        idx_map[i] = idx
    p = 0
    for a in A[1:]:
        for j in a:
            if j == start: break 
            p = max(p, idx_map[j] + 1)
    A[0].insert(p, start)
    print(*A[0])
