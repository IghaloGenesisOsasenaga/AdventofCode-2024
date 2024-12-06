A = []
curr = '.'
while curr:
    curr = input()
    if curr:
        A.append(curr)

n = len(A[0])
S = ""
for i in range(n):
    tmp1, tmp2, tmp3, tmp4, tmp5, = '','','','',''
    for j in range(n):
        tmp1 += A[j][i]
    k = 0
    for j in range(i, n):
        tmp2 += A[n-j-1][k]
        tmp5 += A[j][k]
        if i: # not the main diagonal i.e i!=0
            tmp3 += A[n-k-1][j]
            tmp4 += A[k][j]
        k += 1
    S += A[i]+ '.' +A[i][::-1]+ '.' # horizontal 
    S += tmp1+ '.' +tmp1[::-1]+ '.' # vertical
    S += tmp2+ '.' +tmp2[::-1]+ '.' # upper right diagonal (⁰/)
    S += tmp3+ '.' +tmp3[::-1]+ '.' # lower right diagonal (/₀)
    S += tmp4+ '.' +tmp4[::-1]+ '.' # upper left diagonal (\⁰)
    S += tmp5+ '.' +tmp5[::-1]+ '.' # lower left diagonal (₀\)

print(S.count("XMAS"))