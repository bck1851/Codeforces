# https://codeforces.com/problemset/problem/1921/D

from itertools import accumulate

def first(A, i):
    return 0 if i == 0 else A[i - 1]

def last(A, i):
    return 0 if i == 0 else A[-1] - (A[-i - 1] if i < len(A) else 0)

t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()])
    B = sorted([int(i) for i in input().split()])
    A = list(accumulate(A))
    B = list(accumulate(B))
    res = 0
    for i in range(n+1):
        last_a = last(A, i) 
        first_a = first(A, n-i) 
        last_b = last(B, n-i) 
        first_b = first(B, i)
        res = max(res, last_a - first_b + last_b - first_a)
    print(res)
