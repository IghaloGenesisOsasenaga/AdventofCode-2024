equations = []
curr = '.'
while curr:
    curr = input()
    if curr:
        trgt, opds = curr.split(': ')
        equations.append((int(trgt), tuple(map(int, opds.split()))))

def check(targ, opds, oprt):
    curr = opds[0]
    n = len(opds)
    for i in range(n-1, 0, -1):
        if oprt & (1 << (i-1)):
            curr *= opds[n-i]
        else:
            curr += opds[n-i]
    return trgt == curr
ans = 0

length = len(equations)
counter = 1
for equation in equations:
    trgt, opds = equation
    mx_comb = len(opds)
    for oprt in range(2 ** (mx_comb-1)):
        if check(trgt, opds, oprt):
            ans += trgt
            break
    print(f'{100 * (counter/length):.2f}% complete', end='\r')
    counter += 1

print(f'\n{ans}')