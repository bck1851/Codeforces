# https://codeforces.com/contest/1927/problem/D

def f(n,q,A,Q):
    par = list(range(n))
    rank = [1]*n 
    
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]
        
    def union(x,y):
        px,py = find(x), find(y)
        if px == py: return 
        if rank[py] > rank[px]:
            px,py = py,px 
        rank[px] += rank[py]
        par[py] = px 
        
    for i in range(1, n):
        if A[i] == A[i-1]:
            union(i, i-1)
            
    ids = [-1]*n
    cur = 0 
    for i in range(n):
        if i > 0 and A[i] == A[i-1]:
            ids[i] = ids[i-1]
        else:
            ids[i] = cur 
            cur += 1 
        
    select = [0]*(cur+1)
    for idx, elem in enumerate(A):
        select[ids[idx]] = idx
        
    res = list()
    for i,j in Q:
        i,j = i-1, j-1
        if ids[i] == ids[j]:
            res.append([-1,-1])
        elif A[i] == A[j]:
            t_idx = ids[j] - 1
            res.append([i, select[t_idx]])
        else:
            res.append([i,j])
            
    for i,j in res:
        if i != -1:
            print(i+1, " ", j+1)
        else:
            print(-1, " ", -1)
 

t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    q = int(input())
    Q = []
    for _ in range(q): 
        Q.append([int(i) for i in input().split()])
    f(n,q,A,Q)
