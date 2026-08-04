# https://codeforces.com/contest/1993/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    E,O = list(), list()
    for i in input().split():
        i = int(i)
        if i%2: 
            O.append(i)
        else: 
            E.append(i)
    if not O or not E:
        print(0)
        continue
    odd = max(O)
    E.sort()
    res = 0 
    for i in E:
        if odd > i:
            odd += i
            res += 1 
        else:
            odd += E[-1] 
            res += 2 
    print(res)
