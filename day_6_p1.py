G = []
curr = '.'
gp = []
i = 0
while curr:
    curr = input()
    if curr:
        if '^' in curr:
            gp = [i, curr.index('^')]
        G.append(list(curr))
        i += 1
n = len(G[0])
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up, right, down, left
di = 0
G[gp[0]][gp[1]] = 'X'
vis = set()
while 0 <= gp[0] < n and 0 <= gp[1] < n:
    while 0 <= gp[abs(dxy[di][1])] < n:
        nxt = [gp[0]+dxy[di][0], gp[1]+dxy[di][1]]
        if 0 <= nxt[abs(dxy[di][1])] < n and G[nxt[0]][nxt[1]] == '#':
            di = (di+1)%4
        else:
            vis.add(f'{gp}')
            gp[0] += dxy[di][0]
            gp[1] += dxy[di][1]
print(len(vis))