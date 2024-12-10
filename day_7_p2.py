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
    for i in range(1, n):
        if oprt[i-1] == 0:
            curr *= opds[i]
        elif oprt[i-1] == 1:
            curr += opds[i]
        else:
            curr = int(f'{curr}{opds[i]}')
    return trgt == curr

def convert(x, length):
    rems = [0]*length
    i = length-1
    while x:
        rems[i] = x%3
        x //= 3
        i -= 1
    return rems

ans = 0

length = len(equations)
counter = 1
for equation in equations:
    trgt, opds = equation
    mx_comb = len(opds)
    for oprt in range(3 ** (mx_comb-1)):
        if check(trgt, opds, convert(oprt, mx_comb-1)):
            ans += trgt
            break
    print(f'{100 * (counter/length):.2f}% complete', end='\r')
    counter += 1

print(f'\n{ans}')