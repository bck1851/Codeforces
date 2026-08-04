 # https://codeforces.com/contest/2174/problem/A

from collections import Counter

def merge(A,t):
    i = j = 0 
    m,n = len(A), len(t)
    res = list()
    while i < m or j < n:
        if i < m and (j == n or A[i] < t[j]):
            res.append(A[i])
            i += 1 
        else:
            res.append(t[j])
            j += 1 
    return "".join(res)

t = int(input())
for _ in range(t):
    t = input()
    s = input()
    cnt = [0]*26
    for i in t:
        cnt[ord(i)-97] += 1
    A = list()
    for ch in sorted(s):
        if cnt[ord(ch)-97]:
            cnt[ord(ch)-97] -= 1 
        else:
            A.append(ch)
    print(merge(A,t) if all(i == 0 for i in cnt) else "Impossible")
    
