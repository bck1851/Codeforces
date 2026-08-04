# https://codeforces.com/contest/1981/problem/B

t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    start = max(0, n-m)
    end = n + m 
    s_bits = start.bit_length()
    e_bits = end.bit_length()
    if e_bits > s_bits:
        print((1<<e_bits)-1)
    else:
        x = 0 
        for j in range(e_bits-1, -1, -1):
            if (end>>j)&1 and not (start>>j)&1:
                x = j 
                break 
        end |= (1<<x)-1 
        print(end)
