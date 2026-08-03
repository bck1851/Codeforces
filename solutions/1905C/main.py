# https://codeforces.com/problemset/problem/1905/C 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    stack = list()
    for idx,i in enumerate(a):
        while stack and stack[-1][1] < i:
            stack.pop()
        stack.append([idx,i])
    indexes = [i[0] for i in stack]
    elems = [i[1] for i in stack]
    for idx, elem in zip(indexes, sorted(elems)):
        a[idx] = elem
    if a != sorted(a):
        print(-1)
        continue
    m = len(elems)
    t1 = [True]*m 
    t2 = [True]*m 
    for i in range(1, m):
        t1[i] = t1[i-1] and elems[i] >= elems[i-1]
    for i in range(m-2, -1, -1):
        t2[i] = t2[i+1] and elems[i] >= elems[i+1]
    res = -1 
    if t2[0]: res = m 
    if t1[-1]: res = 0 
    for i in range(m-1, 0, -1):
        if t2[i] and t1[i-1] and elems[i] <= elems[0]:
            res = min(res, m - i)
            break  
    print(res)
