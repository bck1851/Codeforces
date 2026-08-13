# https://codeforces.com/problemset/problem/2191/B

def f(A):
    res = list()
    seen = set()
    mex = 0 
    for i in A:
        seen.add(i)
        while mex in seen:
            mex += 1 
        res.append(mex)
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    A = sorted(map(int, input().split()), reverse = True)
    mex_F, mex_B = f(A), f(A[::-1])[::-1]
    ok = not any(mex_F[i] == mex_B[i+1] for i in range(n-1))
    print("Yes" if ok else "No")
