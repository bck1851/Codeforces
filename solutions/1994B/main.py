# https://codeforces.com/contest/1994/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(i) for i in input()]
    t = [int(i) for i in input()]
    ok = True 
    for i,j in zip(s,t):
        if i == 1:
            break 
        if j == 1:
            ok = False 
            break 
    print("YES" if ok else "NO")
