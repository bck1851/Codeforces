#https://codeforces.com/problemset/problem/1895/C
L = [2,4,6,8,10]
B = [[0]*51 for _ in range(6)]

for _ in range(1):
    n = int(input())
    A = [i for i in input().split()]
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = 0
    res = 0
    for s in A:
        B[len(s)][sum(int(i) for i in s)] += 1
    for length in L:
        for first in A:
            if len(first) > length:
                continue
            n = len(first)
            if n > length//2:
                sa = sb = 0 
                for i in range(n):
                    if i < length//2:
                        sa += int(first[i])
                    else:
                        sb += int(first[i])
                if sa >= sb:
                    res += B[length-n][sa-sb]
                sa = sb = 0 
                for i in range(n):
                    if i < n - length//2:
                        sb += int(first[i])
                    else:
                        sa += int(first[i])
                if sa >= sb:
                    res += B[length-n][sa-sb]
            elif n == length//2:
                sa = sum(int(i) for i in first)
                res += B[length-n][sa]
    print(res)
