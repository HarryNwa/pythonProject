a = [1, 0, 1, 2, 3, 4, 1, 1, 4]
c = []
for v in a:
    if v not in c:
        c += [v]
print(c)


