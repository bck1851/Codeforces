# https://codeforces.com/contest/2171/problem/B
t = int(input())
for _ in range(t):
    n = input()
    A = [int(i) for i in input().split()]
    x,y = A[0], A[-1]
    if x == -1 or y == -1:
        A[0] = A[-1] = (0 if x == y == -1 else x if y == -1 else y)
    A = [i if i != -1 else 0 for i in A]
    print(abs(sum(A[i] - A[i-1] for i in range(1, len(A)))))
    print(*A)
        
