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
poss_obs = set()
while 0 <= gp[0] < n and 0 <= gp[1] < n:
    while 0 <= gp[abs(dxy[di][1])] < n:
        nxt = [gp[0]+dxy[di][0], gp[1]+dxy[di][1]]
        if 0 <= nxt[abs(dxy[di][1])] < n and G[nxt[0]][nxt[1]] == '#':
            di = (di+1)%4
        else:
            if abs(dxy[di][0]): # if the row is changing
                vis.add(f'{di} {gp[1]}') # moving along a column
            else: # the colummn is changing
                vis.add(f'{di} {gp[0]}') # moving along a row
            gp[0] += dxy[di][0]
            gp[1] += dxy[di][1]
            if 0 <= gp[abs(dxy[di][1])] < n:
                nxt_di = (di+1)%4
                if nxt_di == 0 or nxt_di == 2: # up or down
                    if f'{nxt_di} {gp[1]-dxy[di][1]}' in vis:
                        poss_obs.add(f'{gp}')
                else: # right or left
                    if f'{nxt_di} {gp[0]-dxy[di][0]}' in vis:
                        poss_obs.add(f'{gp}')
print(len(poss_obs))
