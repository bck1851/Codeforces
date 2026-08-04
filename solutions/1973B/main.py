# https://codeforces.com/contest/1973/problem/B

def f(A,k):
    cnt = [0]*21 
    start = 0 
    for i in A[:k]:
        start |= i
    cur = 0
    for idx,i in enumerate(A):
        for j in range(21):
            bit = (i>>j)&1 
            cnt[j] += bit
            if bit: cur |= 1<<j 
        if idx >= k-1:
            if cur != start: return False 
            elem = A[idx-k+1]
            for j in range(21):
                bit = (elem>>j)&1 
                cnt[j] -= bit 
                if bit and not cnt[j]:
                    cur ^= 1<<j 
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    left, right = 1, n 
    while left < right:
        mid = (left + right)//2 
        if f(A,mid):
            right = mid 
        else:
            left = mid + 1 
    print(left)
