# https://codeforces.com/contest/2145/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    bal = 0 
    for i in s: 
        bal += 1 if i == 'a' else -1 
    pre = {0:-1} 
    res = n if bal != 0 else 0
    cbal = 0
    tar = bal
    for idx,i in enumerate(s):
        cbal += 1 if i == 'a' else -1 
        if cbal - tar in pre:
            res = min(res, idx - pre[cbal - tar])
        pre[cbal] = idx 
    print(res if res != n else -1)
