# https://codeforces.com/contest/2226/problem/B
import math 
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    res = 0
    for i in range(1, len(A)):
        res += math.gcd(A[i], A[i-1]) == abs(A[i] - A[i-1])
    print(res)
