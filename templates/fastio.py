import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

# to read all input at once
import sys
# input contains only integers
it = map(int, sys.stdin.read().split())
II = lambda: next(it)
# input contains strings
it = iter(sys.stdin.read().split())
SI = lambda: next(it)
II = lambda: int(SI())

#output
output = []
for _ in range(n):
    ans = solve()
    output.append(ans)
print(*output, sep='\n')
