# https://codeforces.com/contest/2236/problem/A
num_inputs = int(input())
for _ in range(num_inputs):
    n = int(input())
    H = [int(i) for i in input().split()]
    mx = max(H)
    print(1 + max(abs(mx-i) for i in H))
