# https://codeforces.com/contest/2225/problem/B
def f(A, start):
    left = 0
    t = start
    while left < len(A) and A[left] == t:
        left += 1 
        t ^= 1 
    right = len(A) - 1 
    t = start if len(A)%2 else start^1 
    while right >= left and A[right] == t:
        right -= 1 
        t ^= 1 
    return left >= right or all(A[i] != A[i+1] for i in range(left, right))
    

t = int(input())
for _ in range(t):
    A = [1 if ch == 'a' else 0 for ch in input()]
    x = f(A, 0) or f(A, 1)
    print("YES" if x else "NO")
