# https://codeforces.com/contest/2231/problem/A
# 1 2 3 4 5 6 7 8
# 2n 2n-1 2n-2 ... n+1

num_inputs = int(input())
for _ in range(num_inputs):
    n = int(input())
    print(*list(reversed(range(n+1,2*n+1))))
