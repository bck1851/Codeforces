import bisect
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    res = 0 
    A = list()
    for i in arr:
        if not A or i > A[-1]:
            A.append(i)
            res += len(A) == 2
        else:
            j = bisect.bisect_left(A, i)
            A[j] = i
            res += j == 1
    print(res)
