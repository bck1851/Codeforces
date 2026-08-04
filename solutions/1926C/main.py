# https://codeforces.com/contest/1926/problem/C

from functools import cache

def h(limit):
    limit = [int(i) for i in str(limit)]
    @cache 
    def f(idx, free):
        if idx == len(limit):
            return 1,0 
        tot = count = 0 
        for j in range(10):
            if not free and j > limit[idx]:
                break 
            new_free = free or (j < limit[idx])
            nxt_count, nxt_tot = f(idx+1, new_free)
            tot += nxt_tot + nxt_count*j
            count += nxt_count
        return count,tot
    return f(0,0)[1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(h(n))
