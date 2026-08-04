# https://codeforces.com/contest/1853/problem/B

# a b a+b 2a+3b 3a+5b 5a+8b....

# 2a + 3b = 22
# 2(11 - a) = 3b

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    pa, ca = 0,1 
    pb, cb = 1,1
    ok = True 
    for _ in range(k-2):
        pa, ca = ca, ca + pa 
        pb, cb = cb, cb + pb 
        if pa > n or pb > n: 
            ok = False
            break 
    if not ok:
        print(0)
        continue 
    res = 0 
    for a in range(0, n+1):
       first = ca*a 
       second = n - first 
       if second >= 0 and not second%cb:
           res += 1 
    print(res)
