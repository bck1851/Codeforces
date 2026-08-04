# https://codeforces.com/contest/2224/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted([int(i) for i in input().split()])
    A = [A.pop()] + sorted(set(A)) 
    res = MAX = MEX = 0 
    seen = set()
    for i in A:
        seen.add(i)
        MAX = max(MAX,i)
        while MEX in seen: MEX += 1 
        res += MAX + MEX 
    res += (MAX + MEX)*(n - len(A))
    print(res)
