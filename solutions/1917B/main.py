# https://codeforces.com/contest/1917/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    res = 0
    a = set()
    for i in s:
        res += len(a)
        a.add(i)
    print(res + len(a))
