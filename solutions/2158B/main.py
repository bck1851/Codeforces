# https://codeforces.com/contest/2158/problem/B

cnt = [0]*400001
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    for i in A:
        cnt[i] = 0 
    for i in A:
        cnt[i] += 1 
    res = odd = even = 0 
    for i in set(A):
        if cnt[i]&1:
            odd += 1 
            res += 1 
        elif (cnt[i]//2)&1:
            res += 2 
        else:
            even += 1 
    res += 4*(even//2)
    if even%2 and odd >= 2:
        res += 2 
    print(res)
