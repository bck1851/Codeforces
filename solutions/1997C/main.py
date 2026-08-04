# https://codeforces.com/contest/1997/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = [i for i in input()]
    bal = 0 
    for idx,i in enumerate(s):
        if i == '(':
            bal += 1 
        elif i == ')':
            bal += -1 
        elif bal > 0:
            s[idx] = ')'
            bal -= 1 
        else:
            s[idx] = '('
            bal += 1 
    res = 0 
    stack = list()
    for idx,i in enumerate(s):
        if i == '(':
            stack.append(idx)
        else:
            res += idx - stack.pop()
    print(res)
