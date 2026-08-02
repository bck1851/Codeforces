#https://codeforces.com/problemset/problem/1895/C
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
    for length in [2,4,6,8,10]:
        for first in A:
            if len(first) > length:
                continue
            n = len(first)
            half = length//2
            if n > half:
                s1 = s2 = 0  
                for idx,i in enumerate(first):
                    s1 += int(i)*(1 if idx < half else -1)
                    s2 += int(i)*(1 if idx >= n - half else -1)
                if s1 >= 0:
                    res += B[length-n][s1]
                if s2 >= 0:
                    res += B[length-n][s2]
            elif n == length//2:
                sa = sum(int(i) for i in first)
                res += B[length-n][sa]
    print(res)
