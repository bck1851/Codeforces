#https://codeforces.com/contest/1882/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    A = list()
    S = 0
    for _ in range(n):
        cur = 0 
        for num in [int(i) for i in input().split()][1:]:
            cur |= 1 << num 
            S |= 1 << num
        A.append(cur)
    res = 0 
    for bit in range(50, -1, -1):
        if not (S >> bit)&1: continue 
        cur_or = 0
        for num in A:
            if not (num >> bit)&1:
                cur_or |= num
        res = max(res, cur_or.bit_count())
    print(res)
