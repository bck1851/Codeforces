# https://codeforces.com/contest/2230/problem/A
num_inputs = int(input())
for _ in range(num_inputs):
    n,a,b = [int(i) for i in input().split()]
    res = 0
    if b <= 3*a:
        res += b*(n//3)
        n %= 3
        res += min(n*a, b)
    else:
        res = n*a
    print(res)
