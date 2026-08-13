# https://codeforces.com/problemset/problem/1775/C
def f(l,r):
    if l.bit_length() < r.bit_length():
        return 0 
    cur = 0 
    start = r.bit_length()
    for i in range(start-1, -1, -1):
        if ((l >> i) &1) != ((r >> i) & 1):
            break 
        if (l >> i) & 1:
            cur += 1 << i 
    return cur

t = int(input())
for _ in range(t):
    n,x = [int(i) for i in input().split()]
    left, right, res = n, 10**20, -1 
    while left <= right:
        mid = (left + right)//2
        if f(n, mid) > x:
            left = mid + 1 
        elif f(n, mid) < x:
            right = mid - 1 
        else:
            res = min(res, mid) if res != -1 else mid
            right = mid - 1
    print(res)
