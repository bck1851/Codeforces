# https://codeforces.com/problemset/problem/1768/B
t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    sA = sorted(A)
    match = j = 0
    for i in sA:
        while j < n and A[j] != i:
            j += 1 
        if j < n:
            match += 1 
            j += 1 
    rem = n - match 
    print(rem//k if not rem%k else rem//k + 1)
