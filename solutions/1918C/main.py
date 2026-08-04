#https://codeforces.com/contest/1918/problem/C
from math import inf

def f(a,b,r,c):
    bal = 0
    for i in range(63,-1,-1):
        bit_a = (a>>i)&1 
        bit_b = (b>>i)&1 
        if bit_a == bit_b: 
            continue
        if bal == 0:
            tar_bit = (bit_a^1) if c == 0 else (bit_b^1)
            cand = 1 << i 
            if tar_bit and cand > r: 
                return inf 
            bal += cand if c == 0 else -cand
            if tar_bit: r -= cand 
        else:
            tar_bit =  (bit_a^1) if bal < 0 else (bit_b^1)
            cand = 1 << i
            if not tar_bit or cand <= r:
                bal += cand if bal < 0 else -cand 
                if tar_bit: r -= cand 
            else:
                bal += -cand if bal < 0 else cand
    return abs(bal)

t = int(input())
for _ in range(t):
    a,b,r = [int(i) for i in input().split()]
    print(min(f(a,b,r,0),f(a,b,r,1)))
