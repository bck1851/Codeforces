# https://codeforces.com/contest/2160/problem/C

 
# a1  a2  a3 ....a31 a32 
# a32 a31 a30 .. a2  a1 
# b32 b31 b30 .. b2  b1

# a3 a2 a1 
# a1 a2 a3

def f(num, bits):
    a = [0]*bits
    for i in range(bits):
        bit = (num >> i)&1 
        a[~i] = bit
    res = all(a[i] == a[~i] for i in range(bits//2))
    if bits&1:
        res &= a[bits//2] == 0 
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    res = any(f(n,bits) for bits in range(n.bit_length(), 65))
    print("YES" if res else "NO")
