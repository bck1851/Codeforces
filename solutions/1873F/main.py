# https://codeforces.com/contest/1873/problem/F

def f(length, a, h, k):
    left = tot = 0
    n = len(a)
    for right in range(n):
        tot += a[right]
        if right > 0 and h[right-1]%h[right]:
            tot = a[right]
            left = right 
        while tot > k:
            tot -= a[left]
            left += 1 
        if right - left + 1 >= length:
            return True 
    return False

t = int(input())
for _ in range(t):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    h = [int(i) for i in input().split()]
    left, right, res = 1, n, 0 
    while left <= right:
        mid = (left + right)//2
        if f(mid, a, h, k):
            res = mid 
            left = mid + 1 
        else:
            right = mid - 1 
    print(res)
    
    
