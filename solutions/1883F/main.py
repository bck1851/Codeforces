#https://codeforces.com/problemset/problem/1883/F
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    last = set()
    seen = set()
    for i in range(n-1, -1, -1):
        if A[i] not in seen:
            last.add(i)
        seen.add(A[i])
    res = 0
    first = set() 
    for idx,i in enumerate(A):
        first.add(i)
        if idx  in last:
            res += len(first)
    print(res)
