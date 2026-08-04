# https://codeforces.com/contest/2008/problem/D

def f(n,P,s):
    group = [-1]*n 
    idx = 0
    blacks = [0]*n
    global_seen = set()
    for i in range(n):
        if i in global_seen:
            continue
        seen = set()
        cur = i 
        while cur not in seen:
            seen.add(cur)
            global_seen.add(cur)
            cur = P[cur]
        black = 0
        for i in seen:
            group[i] = idx 
            black += int(s[i])^1
        blacks[idx] = black
        idx += 1 
    return [blacks[group[i]] for i in range(n)]

t = int(input())
for _ in range(t):
    n = int(input())
    P = [int(i) - 1 for i in input().split()]
    s = input()
    print(*f(n,P,s))
