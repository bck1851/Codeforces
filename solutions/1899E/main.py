#https://codeforces.com/contest/1899/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    ptr = A.index(min(A))
    print(ptr if A[ptr:] == sorted(A[ptr:]) else -1)
