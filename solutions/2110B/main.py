# https://codeforces.com/contest/2110/problem/B
t = int(input())
for _ in range(t):
    opened = x = 0
    for i in input():
        if i == '(':
            opened += 1 
        else:
            opened -= 1
            x += not opened 
        if x > 1: 
            break
    print("YES" if x > 1 else "NO")
