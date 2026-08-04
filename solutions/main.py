# https://codeforces.com/contest/1915/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    bal,z = 0,-1 
    B = sorted([0] + [bal := bal + (z:= -z)*i for i in A])
    print(["NO", "YES"][any(B[i] == B[i-1] for i in range(1,len(B)))])
