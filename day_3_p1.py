from re import findall as find

ans = 0
curr = "."
while curr:
    curr = input()
    if curr:
        list_ = *map(lambda x: map(int, find(r"\d+", x)), find(r"mul\(\d+,\d+\)", curr)),
        for x, y in list_:
            ans += x*y
print(ans)