G = []
curr = '.'
gp = []
i = 0
while curr:
    curr = input()
    if curr:
        G.append(list(curr))
        if '^' in curr:
            gp = [i, curr.index('^')]
            G[i][gp[1]] = '.'
        i += 1
n = len(G[0])
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def check():
    di = 0
    i, j = gp
    vis = set()
    while True:
        nxt_i = i + dxy[di][0]
        nxt_j = j + dxy[di][1]
        if not (0 <= nxt_i < n and 0 <= nxt_j < n):
            return 0
        if (di, nxt_i, nxt_j) in vis:
            return 1
        if G[nxt_i][nxt_j] == '.':
            i = nxt_i
            j = nxt_j
            vis.add((di, i, j))
        else:
            di = (di + 1)%4

ans = 0
di = 0
i, j = gp
range_ = set()
while True:
    nxt_i = i + dxy[di][0]
    nxt_j = j + dxy[di][1]
    if not (0 <= nxt_i < n and 0 <= nxt_j < n):
        break
    if G[nxt_i][nxt_j] == '.':
        i = nxt_i
        j = nxt_j
        range_.add((i, j))
    else:
        di = (di + 1)%4

length = len(range_)
counter = 1
for i,j in range_:
    if [i, j] != gp:
        G[i][j] = '#'
        ans += check()
        G[i][j] = '.'
    print(f'{100 * (counter/length):.2f}% complete', end='\r')
    counter += 1
print(f'\n{ans}')