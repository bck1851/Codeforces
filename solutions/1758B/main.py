# https://codeforces.com/problemset/problem/1758/B
def f(n):
    if n&1:
        return [1]*n 
    elif n == 2:
        return [1,3]
    else:
        # k*(n-2) = (n-1)*sum (sum have at least two bits)
        # k = n - 1 
        # k*(n-2)*cur = (n-1)*sum
        cur = 1 
        while (cur*(n-2)).bit_count() <= 1:
            cur += 1 
        sm = cur*(n-2)
        other_elem = (n-1)*cur 
        first = 0 
        for i in range(31, -1, -1):
            if (sm >> i)&1:
                first = i 
                break 
        return [other_elem]*(n-2) + [1<<i, sm - (1<<i)]

t = int(input())
for _ in range(t):
    n = int(input())
    res = f(n)
    print(*res)
