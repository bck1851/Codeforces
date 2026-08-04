# https://codeforces.com/contest/2131/problem/C

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    for i in range(n):
        a = S[i]%k 
        b = k - a 
        S[i] = min(a,b)
        a = T[i]%k 
        b = k - a 
        T[i] = min(a,b)
    print("YES" if sorted(S) == sorted(T) else "NO")
