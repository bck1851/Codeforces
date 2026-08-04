# https://codeforces.com/contest/1988/problem/C
t = int(input())
for _ in range(t):
    n = int(input())
    bits = [i for i in range(65) if (n>>i)&1]
    m = n.bit_count()
    res = [(1<<m)-1]
    while True:
        pre = res[-1]
        cur = sum(1<<i for i in range(m) if not (pre>>i)&1)
        x = 0 
        for i in range(m-1,-1,-1):
            if (cur>>i)&1:
                break 
            x = i 
        cur += sum(1<<i for i in range(m) if i != x and not (cur)>>i&1)
        if cur > 0:
            res.append(cur)
        if not (cur>>(m-1))&1:
            break 
    z = [sum(1<<bits[i] for i in range(m) if (num>>i)&1) for num in reversed(res)]
    print(len(z))
    print(*z)
