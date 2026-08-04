# https://codeforces.com/contest/1913/problem/C

bits = [0]*32

t = int(input())
for _ in range(t):
    a,b = [int(i) for i in input().split()]
    if a == 1:
        bits[b] += 1
    else:
        for i in range(31, -1, -1):
            num = 1 << i
            if num*bits[i] > b:
                b %= num 
            else:
                b -= num*bits[i]
        print("YES" if not b else "NO")
