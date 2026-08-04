# https://codeforces.com/contest/2065/problem/D

t = int(input())
for _ in range(t):
    n,m =  [int(i) for i in input().split()]
    A = list()
    for _ in range(n): A.append([int(i) for i in input().split()])
    A = [i for j in sorted(A, key = lambda x:-sum(x)) for i in j]
    print(sum((i+1)*A[~i] for i in range(len(A))))
