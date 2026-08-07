# https://codeforces.com/contest/2237/problem/A
import itertools

num_inputs = int(input())
for _ in range(num_inputs):
    n = int(input())
    towers = [int(i) for i in input().split()]
    print(sum(list(itertools.accumulate(towers, lambda a,b: min(a,b)))))
