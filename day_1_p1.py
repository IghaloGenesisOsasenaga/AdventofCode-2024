left_list, right_list = [], []
curr = '.'
while curr:
    curr = *map(int, input().split()),
    if curr:
        left_list.append(curr[0])
        right_list.append(curr[-1])

left_list.sort()
right_list.sort()
n = len(left_list)
ans = 0
for i in range(n):
    ans += abs(left_list[i] - right_list[i])

print(ans)