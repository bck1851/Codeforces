# https://codeforces.com/contest/1923/problem/B

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    health = [int(i) for i in input().split()]
    point = [abs(int(i)) for i in input().split()]
    A = sorted([j,i] for i,j in zip(health,point))
    ok = True
    ptr = 0
    for i in range(1,n+1):
        rem = k 
        while ptr < n and rem:
            x = min(A[ptr][1], rem)
            A[ptr][1] -= x 
            rem -= x 
            if A[ptr][1]: break
            ptr += 1
        if ptr < n and A[ptr][0] <= i:
            ok = False 
            break 
    print("YES" if ok else "NO")
