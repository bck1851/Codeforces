# https://codeforces.com/contest/2114/problem/B
t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    A = [int(i) for i in input()]
    one, zero = A.count(1), A.count(0)
    if one > zero: 
        one,zero = zero,one
    p = (zero - one)//2
    ans = "YES" if p <= k and p + one >= k and p&1 == k&1 else "NO"
    print(ans)
