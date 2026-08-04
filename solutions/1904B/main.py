# https://codeforces.com/contest/1904/problem/B

from itertools import accumulate

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    sA = sorted((i,idx) for idx,i in enumerate(A))
    acc = list(accumulate(i[0] for i in sA))
    ptr = 0
    res = [0]*n
    for idx,[i,j] in enumerate(sA):
        while ptr < len(acc):
            tot = acc[ptr]
            if ptr < idx: 
                tot += i 
            if ptr + 1 < n and tot >= sA[ptr+1][0]:
                ptr += 1 
            else:
                break 
        res[j] = ptr  
    print(*res)
