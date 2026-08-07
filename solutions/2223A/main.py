# https://codeforces.com/contest/2233/problem/A
num_inputs = int(input())
for _ in range(num_inputs):
    n,x,y,z = [int(i) for i in input().split()]
    left, right = 1, n
    while left < right:
        mid = (left + right)//2
        a = mid*x   
        b = max(0, mid-z)*10*y
        c = mid*y
        if a + b >= n or a + c >= n: 
            right = mid 
        else:
            left = mid + 1
    print(left)
        
