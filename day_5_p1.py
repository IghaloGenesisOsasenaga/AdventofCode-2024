A = set()
curr = '.'
while curr:
    curr = input()
    if curr:
        A.add(curr)

curr = '.'
ans = 0
while curr:
    curr = input()
    if curr:
        curr = curr.split(',')
        n = len(curr)
        f = 1
        for i in range(n):
            for j in range(i+1, n):
                f &= (curr[i] + '|' +curr[j]) in A
        if f:
            ans += int(curr[n//2])
print(ans)