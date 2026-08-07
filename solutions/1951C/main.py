# https://codeforces.com/problemset/problem/1951/C

def f(A,k):
    sA = sorted(enumerate(A), key = lambda x:x[1])
    elems = 0
    res = list()
    for idx, elem in sA:
        if elems >= k: break  
        res.append([idx, elem])
        elems += m 
    return [i[1] for i in sorted(res)]

t = int(input())
for _ in range(t):
    n,m,k = [int(i) for i in input().split()]
    A = f([int(i) for i in input().split()], k)
    tot = pre = res = 0
    for i in A:
        rem = k - pre 
        tot += (i + pre)*min(m,rem)
        pre += min(m,rem)
    e = k%m 
    res = tot
    if e:
        for i in range(len(A)-1, -1, -1):
            # m e 
            # e m 
            # (pre + a[i-1]) * m + (pre + m + a[i])*e 
            # (pre + a[i-1]) * e + (pre + e + a[i])*m 
            tot = tot + m*(A[i]-A[i-1]+e) + e*(A[i-1] - A[i] - m) 
            res = min(tot, res)
    print(res)
