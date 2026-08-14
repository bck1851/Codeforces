# https://codeforces.com/problemset/problem/1796/B

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    res = ""
    if a[0] == b[0]:
        res = a[0] + "*"
    elif a[-1] == b[-1]:
        res = "*" + a[-1]
    else:
        for i in range(len(a) - 1):
            if res: break
            for j in range(len(b) - 1):
                if a[i] == b[j] and a[i+1] == b[j+1]:
                    res = "*" + a[i] + a[i+1] + "*"
                    break
    if res != "":
        print("YES")
        print(res)
    else:
        print("NO")
