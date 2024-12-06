from collections import Counter

left_list, right_list = [], Counter()
curr = '.'
while curr:
    curr = *map(int, input().split()),
    if curr:
        left_list.append(curr[0])
        right_list[curr[-1]] += 1

n = len(left_list)
ans = 0
for i in range(n):
    ans += left_list[i] * right_list[left_list[i]]

print(ans)