# https://codeforces.com/contest/1903/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    mat = list()
    for _ in range(n):
        mat.append([int(i) for i in input().split()])
    nums = [0]*n 
    for i in range(n):
        x = (1<<30) - 1
        for j in range(n):
            if i == j: continue
            x &= mat[i][j]
        for j in range(n): 
            if i == j: continue
            x &= mat[j][i]  
        nums[i] = x 
    res = all(nums[i] | nums[j] == mat[i][j] for i in range(n) for j in range(i+1, n))
    if res:
        print("YES")
        print(*nums)
    else:
        print("NO")
