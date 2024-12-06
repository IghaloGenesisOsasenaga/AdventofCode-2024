ans = 0
curr = '.'
while curr:
    *curr, = map(int, input().split())
    if curr:
        cond1 = sorted(curr, reverse=curr[0]>curr[1]) == curr
        cond2 = all(1 <= abs(curr[i]-curr[i+1]) <= 3 for i in range(len(curr)-1))
        ans += cond1 and cond2 # True is 1 False is 0
print(ans)