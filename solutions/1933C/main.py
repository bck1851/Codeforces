# https://codeforces.com/contest/1933/problem/C

t = int(input())
for _ in range(t):
    a,b,l = [int(i) for i in input().split()]
    tot = set()
    for x in range(32):
        ax = a**x
        if ax > l: break 
        for y in range(32):
            by = b**y 
            if ax*by > l: break 
            if not l%(ax*by): tot.add(l//(ax*by)) 
    print(len(tot))
