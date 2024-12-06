ans = 0
curr = '.'
while curr:
    *curr, = map(int, input().split())
    if curr:
        cond1 = sorted(curr, reverse=curr[0]>curr[1]) == curr
        cond2 = all(1 <= abs(curr[i]-curr[i+1]) <= 3 for i in range(len(curr)-1))
        if cond1 and cond2:
            ans += 1
        else:
            for i in range(len(curr)):
                temp = curr[:i] + curr[i+1:]
                cond1 = sorted(temp, reverse=temp[0]>temp[1]) == temp
                cond2 = all(1 <= abs(temp[i]-temp[i+1]) <= 3 for i in range(len(temp)-1))
                if cond1 and cond2:
                    ans += 1; break
print(ans)