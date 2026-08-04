#https://codeforces.com/contest/2200/problem/D

t = int(input())
for _ in range(t):
    n,x,y = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    left = A[:x] + A[y:]
    mid = A[x:y]
    idx = mid.index(min(mid))
    mid = mid[idx:] + mid[:idx]
    res = list()
    i = j = 0
    while i < len(left) or j < len(mid):
        if i < len(left) and (j == len(mid) or left[i] <= mid[j]):
            res.append(left[i])
            i += 1 
        else:
            res.extend(mid[j:])
            j = len(mid)
    print(*res)
    
