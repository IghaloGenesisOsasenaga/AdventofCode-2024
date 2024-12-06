from re import findall as find

ans = 0
curr = "."
list_ = []
while curr:
    curr = input()
    if curr:
        # possible outcomes are
        # (do(),'','') or ('',don't(),'') or ('','',mul(123,123))
        # here 123 is just an example
        list_ += find(r"(do\(\))|(don't\(\))|(mul\(\d+,\d+\))", curr)

flag = 1 # True initially
print(list_)
for x in list_:
    flag = 1 if x[0] else 0 if x[1] else flag
    if flag and x[2]:
        a, b = map(int, find(r"\d+", x[2]))
        ans += a*b
print(ans)