# https://codeforces.com/problemset/problem/2146/A
t = int(input())
for _ in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    cnt = [0]*(n+1)
    for i in A:
        cnt[i] += 1 
    freq = [0]*(n+1)
    for i in cnt:
        freq[i] += 1 
    for i in range(len(freq)-2,-1,-1):
        freq[i] += freq[i+1]
    print(max(i*freq[i] for i in range(n+1)))
