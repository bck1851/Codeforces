# https://codeforces.com/problemset/problem/2120/C
from collections import Counter
 
t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    vals = list()
    rem_nodes = cur = n 
    rem_tot = m 
    cnt = Counter()
    while rem_nodes and rem_tot and cur:
        if rem_tot >= (rem_nodes-1) + cur and len(vals) <= (n - cur):
            vals.append(cur)
            cnt[cur] += 1 
            rem_tot -= cur 
            rem_nodes -= 1 
        else:
            cur -= 1 
    if rem_nodes or rem_tot:
        print(-1)
        continue
    tree = [0]*(n + 1)
    used = [0]*(n + 1)
    pre = -1
    for i in range(n):
        node = i + 1 
        val = vals[i]
        if val != pre:
            tree[node] = val 
            used[val] = 1 
        pre = val 
    j = n
    for i in range(1, n+1):
        if tree[i] != 0:
            continue
        while used[j]: 
            j -= 1 
        tree[i] = j  
        j -= 1 
    print(tree[1])
    for i in range(2, n+1):
        print(tree[i-1], tree[i])
