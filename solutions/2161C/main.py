# https://codeforces.com/contest/2161/problem/C

t = int(input())
for _ in range(t):
    n,x = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()])
    tot = res = 0 
    left = 0 
    B = list()
    for right in range(n-1, -1, -1):
        if left > right:
            break 
        while left <= right and tot//x == (tot + A[right])//x:
            tot += A[left]
            B.append(A[left])
            left += 1 
        if left <= right:
            res += A[right]
            B.append(A[right])
            tot += A[right]
    print(res)
    print(*B)
