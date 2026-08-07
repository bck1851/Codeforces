# https://codeforces.com/contest/2236/problem/B
num_inputs = int(input())
for _ in range(num_inputs):
    n,k = [int(i) for i in input().split()]
    A = list([int(i) for i in input()])
    ok = True
    for i in range(len(A)):
        if not A[i]: 
            continue
        if i + k >= len(A):
            ok = False
            break 
        A[i+k] ^= 1
    print("YES" if ok else "NO")
