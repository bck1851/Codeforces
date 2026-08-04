# https://codeforces.com/contest/1902/problem/B

t = int(input())
for _ in range(t):
    n,P,l,t = [int(i) for i in input().split()]
    left,right,res = 0, n, 0 
    total_tasks = (n-1)//7 + 1
    while left <= right:
        mid = (left + right)//2 
        rem = n - mid 
        points = l*rem + min(total_tasks,2*rem)*t  
        if points >= P:
            left = mid + 1 
            res = mid 
        else:
            right = mid - 1 
    print(res)
