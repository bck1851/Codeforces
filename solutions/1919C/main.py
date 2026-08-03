#https://codeforces.com/contest/1919/problem/C
def f(A):
    res = a = b = 0
    for i in reversed(A):
        if i >= a and i >= b or i < a and i < b:
            res += i < a and i < b
            if a >= b: 
                a = i 
            else: 
                b = i
        elif i >= a and i < b:
            a = i  
        elif i < a and i >= b:
            b = i 
    return res
 
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    print(f(A))
