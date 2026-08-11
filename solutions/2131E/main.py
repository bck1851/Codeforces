# https://codeforces.com/contest/2131/problem/E
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    accA = [i for i in A]
    for i in range(n-2, -1, -1):
        accA[i] ^= accA[i+1]
    last_idx = [n]*n 
    seen = {0: n} 
    ok = True
    for i in range(n-1, -1, -1):
        tar = B[i] ^ accA[i]
        if tar not in seen:
            ok = False 
            break 
        last_idx[i] = seen[tar] - 1
        seen[accA[i]] = i 
    right = -1 
    for i in range(n):
        j = last_idx[i]
        if right <= i:
            right = j 
        elif right == j:
            continue 
        else:
            ok = False
    print("Yes" if ok else "No")
