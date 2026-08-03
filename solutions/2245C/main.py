#https://codeforces.com/problemset/problem/2245/C
t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    xor = n^k
    mexes = [1<<i for i in range(32) if (xor>>i)&1]
    set_mexes = set(mexes)
    if any(i >= n for i in mexes):
        print("NO")
        continue 
    res = [i for i in range(1,n) if i not in set_mexes] + [0] + mexes
    print("YES")
    print(*res)
