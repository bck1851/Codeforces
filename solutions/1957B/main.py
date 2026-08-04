# https://codeforces.com/contest/1957/problem/B

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    length = k.bit_length()
    if n > 1:
        res = [(1<<(length-1))-1]
        res.append(k-res[-1])
        res += [0]*(n-len(res))
        print(*res)
    else:
        print(k)
