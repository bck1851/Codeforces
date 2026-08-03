#https://codeforces.com/contest/1896/problem/C
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    enA = sorted(enumerate(map(int, input().split())), key = lambda x:x[1])
    B = sorted(map(int, input().split()))
    enB = B[k:] + B[:k]
    if sum(enA[i][1] > enB[i] for i in range(n)) != k:
        print("NO")
    else:
        print("YES")
        res = [0]*n
        for i in range(n):
            idx = enA[i][0]
            res[idx] = enB[i]
        print(*res)
