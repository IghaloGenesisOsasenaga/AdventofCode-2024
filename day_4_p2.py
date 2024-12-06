# m s  s m  m m  s s
#  a    a    a    a
# m s  s m  s s  m m
def check(i,a,c,b):
    return A[i+1][c] == 'A' and (
        (A[i][a] == A[i+2][a] == 'M' and
         A[i][b] == A[i+2][b] == 'S') or
        (A[i][b] == A[i+2][b] == 'M' and
         A[i][a] == A[i+2][a] == 'S') or
        (A[i][a] == A[i][b] == 'S' and
         A[i+2][a] == A[i+2][b] == 'M') or
        (A[i][a] == A[i][b] == 'M' and
         A[i+2][a] == A[i+2][b] == 'S'))

ans = 0
A = []
curr = '.'
while curr:
    curr = input()
    if curr:
        A.append(curr)
n = len(A[0])
for x in range(n-2):
    for y in range(n-2):
        ans += check(x,y,y+1,y+2)
print(ans)